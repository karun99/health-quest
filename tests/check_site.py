#!/usr/bin/env python3
"""Health Quest self-check.

Validates the repository's JOSS-facing invariants without any third-party
dependencies: required files exist, the scoring engine markers are present,
and the license/documentation assertions hold.

Usage: python3 tests/check_site.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FAILURES: list = []


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def _require(cond, msg):
    if not cond:
        FAILURES.append(msg)


_require(os.path.isfile(os.path.join(ROOT, "health-quest.html")),
         "health-quest.html is missing")
app = _read("health-quest.html") if os.path.isfile(
    os.path.join(ROOT, "health-quest.html")) else ""

for marker in ("Health Score", "Locate Nearby", "Why this rating",
               "sugar", "salt", "fibre", "protein"):
    _require(marker.lower() in app.lower(),
             f"health-quest.html is missing scoring marker: {marker!r}")

_require("consent" in app.lower(),
         "health-quest.html has no consent-flow marker")

_require(os.path.isfile(os.path.join(ROOT, "explainer.html")),
         "explainer.html is missing")
_require(os.path.isfile(os.path.join(ROOT, "explainer-ieee.html")),
         "explainer-ieee.html is missing")
_require(os.path.isfile(os.path.join(ROOT, "presenter.html")),
         "presenter.html is missing")

license_text = _read("LICENSE")
_require("MIT" in license_text, "LICENSE does not contain a MIT grant")

readme = _read("README.md")
_require(re.search(r"statement of need", readme, re.I),
         "README lacks a Statement of need section")
_require(re.search(r"ai usage disclosure", readme, re.I),
         "README lacks an AI usage disclosure section")

paper_md = os.path.join(ROOT, "paper", "paper.md")
_require(os.path.isfile(paper_md), "paper/paper.md is missing")

if FAILURES:
    for msg in FAILURES:
        print("FAIL:", msg)
    print(f"\n{len(FAILURES)} check(s) failed")
    sys.exit(1)
print("all Health Quest self-checks passed")
sys.exit(0)