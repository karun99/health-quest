# 🥗 Health Quest — Deployment & Live Search Guide

**Project:** Health Quest v3.1
**Purpose:** Social Innovation Ideathon · PanIIT Andhra Pradesh Summit 2026
**Author:** K Subramanya Satyanarayana · Class 9 · St. John's English Medium School
**License:** [MIT](./LICENSE)
**Date:** 22 September 2026

---

## 0 · Live pages

| Page | URL | What it is for |
| --- | --- | --- |
| 🎮 Game | `/` (`health-quest.html`) | The playable app — judges scan the QR and play in 10 seconds |
| 📖 Explainer | `/explainer` | The full project pitch: problem, score formula, ethics, stack |
| ⚙️ IEEE brief | `/ieee` | Standards mapping (IEEE 7000/29148/12207/1012/730/828) + paper config |
| 🎤 Presenter deck | `/presenter` | Demo script, cue cards and a 3-minute timer for the presenter |

---

## 1. Project Summary

Health Quest is an educational web game that helps school students (Classes 8–12) learn to identify the healthiest food. Every answer explains why using a transparent, Michelin-style Health Score. A "Locate Nearby" feature shows real eateries from OpenStreetMap with a visible, criteria-based rating.

**Core principles (from case studies)**

| Case study | What we learned | How Health Quest applies it |
| --- | --- | --- |
| Pokémon Go | Location features can cause real harm | Consent-first flow, no silent tracking, pincode alternative |
| Blue Whale | Manipulative mechanics harm vulnerable kids | No timers, no streak pressure, no "you must go" |
| Michelin Guide | Trust comes from transparent criteria | Visible score breakdown, "Why this rating" button |

**Engineering (IEEE alignment)** — see [`/ieee`](explainer-ieee.html) for the full mapping:

| Standard | What it satisfies | Visible proof |
| --- | --- | --- |
| IEEE 7000-2021 | Ethics-by-design | Safety promise banner · consent-first flow · no timers |
| IEEE 29148-2018 | Requirements | This README acts as the requirements/SRS record |
| IEEE 12207-2017 | Life-cycle process | Documented build → verify → deploy → roadmap |
| IEEE 1012-2016 | Verification & validation | Post-deploy test checklist (section 8) |
| IEEE 730-2014 | Quality assurance | Single-source scoring engine + markdown round-trip |
| IEEE 828-2012 | Configuration management | Versioned single file + importable database |

**Tech stack (all free)**

- **Frontend:** Single HTML file (vanilla JS, no framework)
- **Data:** Local food database + OpenStreetMap Overpass API
- **AI hints (optional):** OpenRouter → NVIDIA NIM → Offline fallback
- **Hosting:** Netlify or Vercel (free tier)
- **Keys:** BYOK (Bring Your Own Key) — stored in localStorage only

---

## 2. Repository Structure

```
health-quest/
├── health-quest.html          ← Main app (single file)
├── explainer.html             ← Project explainer page
├── explainer-ieee.html        ← IEEE configuration brief
├── presenter.html             ← Presenter demo deck
├── LICENSE                    ← MIT License (author + school)
├── netlify/
│   └── functions/
│       └── overpass.js        ← Serverless proxy (Netlify)
├── api/
│   └── overpass.js            ← Serverless proxy (Vercel)
├── netlify.toml               ← Netlify config (optional)
├── vercel.json                ← Vercel config
└── README.md                  ← This document
```

Note: You only need one of the two proxy folders, depending on which platform you deploy to. Both are included so you can switch.

---

## 3. Pre-Deployment Checklist

Before deploying, confirm each item:

- [ ] health-quest.html opens locally and the game works offline
- [ ] All 4 cuisine levels have at least 3 foods (South Indian, North Indian, Indian, International)
- [ ] Markdown export downloads a valid .md file
- [ ] Markdown import re-loads the food database
- [ ] BYOK modal saves keys in localStorage (check DevTools → Application → Local Storage)
- [ ] Hints work with no keys (offline fallback)
- [ ] Hints work with keys (OpenRouter / NVIDIA)
- [ ] At least 10 real eateries verified in your area with photos and hours

⚠️ **Do not deploy with sample eateries.** Judges will dismiss the project instantly.

---

## 4. Serverless Proxy — Why It's Needed

**The problem**

When you open health-quest.html from your computer (`file://`), the browser treats the origin as `null`. When the app tries to fetch from overpass-api.de, the browser blocks it:

```
Access to fetch at 'https://overpass-api.de/api/interpreter'
from origin 'null' has been blocked by CORS policy.
```

**The fix**

A serverless function runs on Netlify's or Vercel's server, calls Overpass on your behalf, and returns the data with the correct CORS header (`Access-Control-Allow-Origin: *`). Your browser only ever talks to your own domain — no CORS block.

```
[Browser]  →  [/api/overpass on Netlify/Vercel]  →  [overpass-api.de]
```

---

## 5. Netlify Deployment

### 5.1 File structure

```
your-project/
├── health-quest.html
└── netlify/
    └── functions/
        └── overpass.js
```

### 5.2 Proxy function — `netlify/functions/overpass.js`

```javascript
export default async (req) => {
  if (req.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
  try {
    const body = await req.text();
    const response = await fetch("https://overpass-api.de/api/interpreter", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://overpass-turbo.eu/",
        "User-Agent": "HealthQuestApp/3.1"
      },
      body
    });
    if (!response.ok) throw new Error(`Overpass API responded with status: ${response.status}`);
    const data = await response.json();
    return new Response(JSON.stringify(data), {
      status: 200,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }
};
```

### 5.3 Frontend proxy URL

The app auto-detects the platform. On Netlify it uses:

```javascript
const proxyUrl = '/.netlify/functions/overpass';
```

On Vercel it uses `/api/overpass`. The app detects which host it is on and picks the right one automatically.

### 5.4 Deploy steps

1. Go to https://app.netlify.com/drop
2. Drag the entire project folder onto the drop zone
3. Wait ~30 seconds
4. Netlify gives you a URL like `https://health-quest-xyz.netlify.app`
5. Test the Locate Nearby feature with a pincode

---

## 6. Vercel Deployment

### 6.1 File structure

```
your-project/
├── health-quest.html
├── explainer.html
├── explainer-ieee.html
├── presenter.html
├── api/
│   └── overpass.js
└── vercel.json
```

### 6.2 Proxy function — `api/overpass.js`

```javascript
export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method Not Allowed' });
  try {
    const response = await fetch("https://overpass-api.de/api/interpreter", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://overpass-turbo.eu/",
        "User-Agent": "HealthQuestApp/3.1"
      },
      body: req.body,
    });
    if (!response.ok) throw new Error(`Overpass API responded with status: ${response.status}`);
    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
```

### 6.3 Clean URLs (vercel.json)

```json
{
  "rewrites": [
    { "source": "/", "destination": "/health-quest.html" },
    { "source": "/explainer", "destination": "/explainer.html" },
    { "source": "/presenter", "destination": "/presenter.html" },
    { "source": "/ieee", "destination": "/explainer-ieee.html" }
  ]
}
```

### 6.4 Deploy steps

1. Install Vercel CLI: `npm i -g vercel`
2. Run in project folder: `vercel` (then `vercel --prod` for production)
3. Follow prompts (link to your account, accept defaults)
4. Get your URL: `https://health-quest-xyz.vercel.app`
5. Test Locate Nearby

### 6.5 Alternative (no CLI)

1. Push project to GitHub
2. Go to https://vercel.com/new
3. Import the repo
4. Vercel auto-detects the `api/` folder
5. Deploy

---

## 7. Local Testing Before Deployment

**Netlify**

```bash
npm install -g netlify-cli
netlify dev
```

**Vercel**

```bash
npm install -g vercel
vercel dev
```

This starts a local server with the function running, so CORS is solved even locally.

---

## 8. Testing Checklist After Deployment

| Test | Expected result |
| --- | --- |
| Open the deployed URL | App loads, ethics banner visible |
| Play one round | Food cards render, answer feedback shows score breakdown |
| Tap Hint with no keys | Offline hint appears |
| Tap Hint with keys | AI hint appears (or falls back gracefully) |
| Tap Locate Nearby → enter pincode | Real eateries appear within 2 km |
| Tap "Why this rating" on a venue | Breakdown appears |
| Tap "Open in Google Maps" | Opens in a new tab |
| Test on mobile | Layout works, buttons tap-able |
| Turn off Wi-Fi, reload | Game works offline; Locate Nearby shows sample |
| Export Markdown | .md file downloads correctly |
| Import Markdown | Food list updates |
| `/explainer` | Explainer page loads |
| `/ieee` | IEEE configuration brief loads |
| `/presenter` | Presenter deck loads, timer runs |

---

## 9. Security & Privacy Notes

- No API keys in the HTML. BYOK only.
- No backend database. Nothing stored on the server.
- No user tracking. No analytics, no cookies, no fingerprinting.
- Location used once, not stored. Sent only to Overpass via the proxy; never logged.
- All keys in localStorage. Cleared when the user clears browser data.

---

## 10. Ideathon Submission Notes

**What to include in the submission**

1. Live URL (from Netlify or Vercel)
2. QR code printed on the poster — judges scan and play in 10 seconds
3. Markdown export — a .md file showing the food database and criteria
4. Field evidence — photos of 10 verified local eateries
5. This document — as the SRS / technical reference
6. IEEE configuration brief — `/ieee` as the engineering-proof layer

**One-line pitch**

> "Health Quest is a static, offline-first web app. No backend, no database, no tracking. Users bring their own AI keys. The whole thing costs ₹0 to run — forever."

**3-minute demo script** (full cue cards in `/presenter`)

1. Show the ethics banner + transparent Health Score formula (20 sec)
2. Play 2 rounds — one wrong on purpose, show the "why" table (60 sec)
3. Open Locate Nearby → enter pincode → show real eateries (30 sec)
4. Tap "Why this rating" on one venue (20 sec)
5. Close: "No timers. No pressure. No tracking. Kids learn by understanding, not by fear." (30 sec)
6. **IEEE bonus (if judges ask the "is this engineered?" question):** open `/ieee` and walk the six-standards mapping (extra depth, no pressure)

---

## 11. IEEE Paper Configuration (for a written submission)

- **Format:** IEEE two-column (conference) or A4 single-column (report), 10-pt Times New Roman, 1-in margins.
- **Title:** *Health Quest: A Transparent, Ethics-By-Design Food-Education Game for School Students*
- **Author:** K Subramanya Satyanarayana, St. John's English Medium School
- **Abstract:** ≤ 250 words (a ready sample lives on the `/ieee` page).
- **Keywords:** health education; nutrition; transparency; ethics-by-design; web application; OpenStreetMap; privacy; K-12 EdTech.
- **Key citations (IEEE numeric style):**

```
[1] K. S. Satyanarayana, "Health Quest: a transparent food-education game…", Ideathon Project, PanIIT AP Summit, 2026.
[2] IEEE Std 7000-2021, Ethical Concerns During System Design. doi: 10.1109/IEEESTD.2021.9536679.
[3] IEEE Std 29148-2018, Requirements Engineering.
[4] IEEE Std 12207-2017, Software Life Cycle Processes.
[5] IEEE Std 1012-2016, Verification and Validation.
[6] OpenStreetMap contributors, "OpenStreetMap". [Online]. Available: https://www.openstreetmap.org
```

---

## 12. Optional Enhancements (Roadmap)

| Idea | Effort | Benefit |
| --- | --- | --- |
| Add Telugu translation | Low | Local relevance for Andhra Pradesh |
| Offline PWA (service worker) | Medium | Works without internet after first load |
| Save favourite eateries to localStorage | Low | Personal use |
| Add "Report outdated info" button | Medium | Crowd-verified data quality |
| Add school-level leaderboard (no names) | Medium | Light competition without pressure |

---

## 13. Troubleshooting

| Problem | Fix |
| --- | --- |
| CORS error persists | Confirm `netlify/functions/overpass.js` or `api/overpass.js` exists and is deployed |
| 404 on `/api/overpass` | Check folder name is exactly `api` (Vercel) or `netlify/functions` (Netlify) |
| Proxy returns 500 | Check Overpass API status at https://overpass-api.de |
| No eateries found | Try a busier pincode, or widen the radius from 2000m to 3000m |
| BYOK keys not saving | Check browser isn't in private/incognito mode |
| AI hint always offline | Keys invalid or rate-limited; test with OpenRouter playground first |

---

## 14. Credits & License

- OpenStreetMap + Overpass API — free, open geodata
- Nominatim — free pincode geocoding
- OpenRouter + NVIDIA NIM — free AI tiers
- Netlify / Vercel — free static hosting with serverless functions
- Case study inspiration — Pokémon Go (safety), Blue Whale (ethics), Michelin Guide (transparency)
- IEEE aligning standards — IEEE 7000, 29148, 12207, 1012, 730, 828

**License:** MIT — © 2026 K Subramanya Satyanarayana, St. John's English Medium School. See [LICENSE](./LICENSE).

---

*End of document. Hand to Ideathon judges as the SRS / technical reference, or include in your GitHub repo.*