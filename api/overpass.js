const MIRRORS = [
  'https://overpass-api.de/api/interpreter',
  'https://overpass.kumi.systems/api/interpreter',
  'https://maps.mail.ru/osm/tools/overpass/api/interpreter',
  'https://overpass.osm.ch/api/interpreter'
];

function extractQuery(reqBody) {
  if (typeof reqBody === 'string') return reqBody;
  if (reqBody && typeof reqBody === 'object') {
    if (typeof reqBody.data === 'string') return 'data=' + reqBody.data;
  }
  return reqBody;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    let body = req.body;
    if (typeof body !== 'string') {
      body = await new Promise((resolve, reject) => {
        let data = '';
        req.on('data', (chunk) => (data += chunk));
        req.on('end', () => resolve(data));
        req.on('error', reject);
      });
    }

    if (typeof body === 'object') {
      body = typeof body.data === 'string' ? 'data=' + body.data : JSON.stringify(body);
    }

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 9500);

    const attempts = MIRRORS.map(async (url) => {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Referer': 'https://overpass-turbo.eu/',
          'User-Agent': 'HealthQuestApp/3.1'
        },
        body: body,
        signal: controller.signal
      });
      if (!response.ok) throw new Error('Overpass ' + url + ' responded with status: ' + response.status);
      return response.json();
    });

    const data = await Promise.any(attempts);
    clearTimeout(timer);
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}