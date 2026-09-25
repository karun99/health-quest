# Contributing to health-quest

Thanks for wanting to help. This project is intentionally small, auditable,
and ethics-first because it teaches school students.

## Ground rules

- Keep the application **single-file and dependency-free** (`health-quest.html`).
- **No manipulative mechanics.** Never add timers, streaks, social pressure,
  or silent location tracking; consent-first flows are a hard requirement.
- Every scoring change must keep the visible "Why this rating" breakdown
  consistent with the README's criteria and the IEEE brief.
- Open an issue before opening a pull request so the design is discussed once.

## Verifying

Run the self-check before pushing (tests live in `tests/` and run on CI):

```sh
python3 tests/check_site.py
```

## Reporting bugs

Search the issues list first. Include the page/URL affected, the expected and
observed Health Score, and the browser you used.

## Support expectations

Maintained by a small team in spare time. Issues are the channel for help;
expect answers within a week, not minutes.

## License

By contributing you agree that your contributions are licensed under the same
MIT license as the rest of the project.