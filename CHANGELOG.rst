==========
Change log
==========

Next version
============

* Switched to ``pyproject.toml`` and hatchling, added tests.
* Dropped support for Python < 3.10.
* **Security fix:** Strings starting with ``=`` are written as text instead of
  formulas so that untrusted data cannot inject formulas into exports. Wrap
  intentional formulas in ``xlsxdocument.Formula``. Titles passed to
  ``table()`` are processed the same way as rows now.
