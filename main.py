#!/usr/bin/env python3
"""Health Quest — local preview server.

Serves the static game (``health-quest.html`` and companions) over HTTP so the
browser app can be run without any build step.

    python main.py            # http://localhost:8000
    PORT=3000 python main.py
"""
from __future__ import annotations

import http.server
import os
import socketserver

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "8000"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):  # noqa: N802
        if self.path in ("/", ""):
            self.path = "/health-quest.html"
        return super().do_GET()

    def log_message(self, *args):  # keep the preview quiet
        pass


def main() -> None:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Health Quest running at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
