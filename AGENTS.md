# Agent instructions

## Tests

Run the test suite with tox, e.g. `tox -e py314-dj52`. Pass test labels as
positional arguments to run a subset: `tox -e py314-dj52 -- tests.test_document`.

Tests live in `tests/` and use Django's test runner with `tests/settings.py`.

CI (`.github/workflows/tests.yml`) runs every `py<version>-*` tox environment
for each Python version in its matrix, so keep the CI matrix and the tox
envlist in sync.

## Commits

- Commit feature by feature: one commit per fix or feature, each including
  its tests.
- No attribution lines (no `Co-Authored-By` etc.).
- Keep commit messages short and don't repeat what the diff already says.
