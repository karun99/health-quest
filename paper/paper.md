---
title: 'Health Quest: an ethics-first food-literacy game with a transparent Health Score for school students'
tags:
  - JavaScript
  - education
  - food literacy
  - health score
  - gamification
  - ethics
authors:
  - name: Sai Karun Nandipati
    orcid: 0009-0007-9218-9750
    affiliation: 1
  - name: K Subramanya Satyanarayana
    affiliation: 2
affiliations:
  - name: Department of Data Science and Artificial Intelligence, PB Siddhartha College of Arts and Science
    index: 1
  - name: St. John's English Medium School
    index: 2
date: 25 September 2026
bibliography: paper.bib
---

# Summary

Health Quest is an ethics-first, browser-based food-literacy game that teaches
school students (Classes 8-12) how to identify the healthiest food. Every
choice a player makes is answered with a transparent, Michelin-style
**Health Score**: the player sees the exact criteria (sugar, salt, fibre,
protein, ultra-processed ingredients, serving cost, and optional
environmental impact) that produced the rating, and can open a "Why this
rating" breakdown for every food and nearby eatery. A **Locate Nearby**
feature queries real restaurants from OpenStreetMap and scores them with the
same visible criteria, using a consent-first flow with no silent location
tracking. The entire application is a single dependency-free HTML file plus a
small serverless API, deployable to any static host, and every gameplay
mechanic is aligned to IEEE ethics and requirements standards.

# Statement of need

Food-habit learning tools for children typically fall into one of two traps:
they use manipulative game mechanics (streak pressure, timers, forced
location tracking) copied from viral mobile games such as Pokémon Go and Blue
Whale, or they present nutrition "scores" as opaque numbers with no auditable
derivation, which teaches children to trust labels rather than understand
them. There is a need for an educational game that is simultaneously
*engaging*, *explainable*, and *ethically designed*. Health Quest addresses
all three: the scoring engine is a single auditable function with a visible
breakdown, no timer or streak mechanic pressures the player, and location
consent is explicit with a pincode fallback. The same architecture maps every
requirement to IEEE 7000 (ethics by design) and IEEE 29148 (requirements
engineering), so classroom- or jury-reviewable evidence of the design's
intent is stored with the code, not in a separate slide deck.

# State of the field

Nutrition and food-education games range from quiz-style lesson apps to
open-ended "food kings" simulators. The most effective existing tools adopt
the transparency lesson of the Michelin Guide: published, criteria-based
ratings create trust [@michelin2024]. Meanwhile, the game-design literature
demonstrates that location features and streak mechanics borrowed from
commercial mobile games can expose children to real harm, and that
consent-first, pressure-free design is the defensive standard (as codified in
IEEE 7000 [@ieee7000]). OpenStreetMap's public data has become a reliable
source for live food-geography education [@osm2024]. Health Quest is, to the
authors' knowledge, the first food-literacy game that combines a fully
transparent, Michelin-style scoring engine with a consent-first live-eatery
locator and an explicit IEEE standards alignment, while remaining a
single-file deployable.

# Software design

The implementation is deliberately small and auditable. `health-quest.html`
contains the entire game client (vanilla JavaScript, no framework, no build
step): a local food database; the scoring engine that maps every food and
eatery to criteria weights and emits a 0-100 Health Score with a visible
breakdown; consent-first location capture with a pincode fallback; and a
single OpenRouter-to-NVIDIA-NIM path for optional AI hints with a fully
offline fallback. Keys are Bring-Your-Own-Key and live only in the player's
`localStorage`. The `api/` directory holds a minimal serverless handler that
proxies the OpenStreetMap Overpass query so eatery lookup works from any
static host. Four companion pages document the project for different
audiences: the explainer (project pitch and score formula), the IEEE brief
(standards mapping to IEEE 7000/29148/12207/1012/730/828 [@ieee29148]),
and a presenter deck for demo sessions.

# Research impact statement

The reproducibility argument of Health Quest is that learning outcomes
depend on the *transparency of the evaluation mechanism*, and that mechanism
is one auditable function in a file a reviewer can open in any browser. The
project is therefore useful as a reference implementation of an
ethics-first, standards-mapped educational game: every design decision that
affects child safety is encoded, versioned, and mapped to a standard. The
game was developed for the PanIIT Andhra Pradesh Social Innovation Ideathon
2026, and its IEEE 7000 alignment and consent-first mechanics serve as a
worked example that other EdTech projects can reuse rather than reinvent.

# AI usage disclosure

The code, documentation, and IEEE-brief structure were drafted with
generative-AI assistance (scaffolding, copy-editing, and requirements
mapping). All assisted artifacts were reviewed, edited, and validated by the
human authors, who made the design decisions. No AI rendered evaluative
decisions in this submission.

# Acknowledgements

No direct funding was received. The authors thank the PanIIT Andhra Pradesh
Summit 2026 organisers for the opportunity to present this project.

# References