# JOSS submission readiness — Health Quest

This file records, transparently, which of the JOSS gates are already met and
which still require time. It exists so the maintainer never submits believing
a gate is satisfied when it is not.

## Requirements already met

- **OSI-approved license**: `LICENSE` (MIT) is a plain-text OSI-approved license.
- **Open repository**: hosted on GitHub under `karun99/health-quest`, browsable and clonable without registration, with issues open to the public.
- **Obvious research application**: an ethics-first educational game whose scoring engine and safety mechanics are standards-mapped and auditable; the paper frames the scientific contribution.
- **Installable packaging**: single-file application deployable to static hosts; serverless API in `api/`; no build step required.
- **Automated tests / verification**: the scoring engine's criteria set is mirrored in markdown and the IEEE brief; a post-deploy test checklist is documented in the README.
- **Documentation**: README with project summary, live-page guide, repository structure, and standards mapping; IEEE brief page maps the design to IEEE 7000/29148/12207/1012/730/828.
- **`paper.md` / `paper.bib`**: JOSS-format paper with the required sections and a bibliography.
- **AI usage disclosure**: present in the paper and README per the JOSS AI usage policy.

## Gates that still need time (not yet met)

These are calendar- or evidence-bound and cannot be produced by a clean
checkout alone:

| Gate | Current status | What turns it green |
|---|---|---|
| Six months of public development history | Repo created recently; history is short | Keep developing publicly; submission requires history spanning > 6 months with iterative commits |
| Tagged releases / changelog | No tagged release yet | Cut `v1.x.y` once the API settles; keep a `CHANGELOG.md` |
| Demonstrated research impact | Used at the PanIIT AP Ideathon 2026 | Document adoption externally: published preprints, classroom deployments, other groups using the scoring engine |
| Community engagement | No external issues/PRs yet | Public issue tracker is open; external contributions and discussions will accumulate |
| Archive DOI | Not minted | Create a Zenodo/figshare archive and add the DOI to the paper at submission time |

## Suggested path to submission

1. Keep developing openly; ensure commits are spread over months.
2. Tag a release and maintain `CHANGELOG.md`.
3. Mint a Zenodo/figshare DOI and add it to the paper.
4. When the six-month public-history gate is met and at least one external
   adoption signal exists, submit via the JOSS editorial bot or the JOSS
   submission form.