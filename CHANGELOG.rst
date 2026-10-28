Change log
==========

Next version
------------

* Switched to ``pyproject.toml`` and hatchling, added tests.
* Dropped support for Python < 3.10.
* **Security fix:** Strings starting with ``=`` are written as text instead of
  formulas so that untrusted data cannot inject formulas into exports. Wrap
  intentional formulas in ``xlsxdocument.Formula``. Titles passed to
  ``table()`` are processed the same way as rows now.

1.3.10 (2022-09-26)
-------------------

* Fixed a crash when exporting naive datetimes with ``USE_TZ = True``.

1.3.9 (2021-04-30)
------------------

* Fixed exporting dates, only datetimes are converted to naive datetimes.

1.3.8 (2021-04-18)
------------------

* Exported dates and datetimes as real values instead of ``YYYY-MM-DD``
  strings. Aware datetimes are converted to naive datetimes in the current
  time zone.

1.3.7 (2020-12-21)
------------------

* Removed control characters openpyxl cannot write.

1.3.6 (2020-03-11)
------------------

* Capitalized the column titles in ``table_from_queryset()``.

1.3.5 (2019-11-29)
------------------

* Used the fields' ``verbose_name`` as column titles in
  ``table_from_queryset()``.

1.3.4 (2019-10-15)
------------------

* Replaced ``ugettext_lazy`` with ``gettext_lazy`` to avoid a deprecation
  warning with Django 3.0.

1.3.3 (2019-02-25)
------------------

* Stopped using openpyxl's deprecated ``save_virtual_workbook()``.

1.3.2 (2018-09-27)
------------------

* Fixed ``export_selected`` with older Django versions which do not have
  ``Options.label_lower``.

1.3.1 (2018-03-11)
------------------

* Fixed slugifying lazy ``verbose_name_plural`` values.

1.3 (2018-03-11)
----------------

* Slugified the sheet title in ``table_from_queryset()``.

1.2 (2017-11-09)
----------------

* Added ``create_export_selected()`` for export actions with additional
  columns.
* Allowed overriding the ``short_description`` of ``export_selected``.

1.1 (2017-06-30)
----------------

* Added the ``additional`` argument to ``table_from_queryset()`` for appending
  cells.

1.0 (2016-11-30)
----------------

* Initial release.
