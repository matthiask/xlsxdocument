from datetime import date
from decimal import Decimal
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from django.http import HttpResponse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


__all__ = ('XLSXDocument', 'create_export_selected', 'export_selected')


class XLSXDocument(object):
    def __init__(self):
        self.workbook = Workbook(write_only=True)
        self.sheet = None

    def add_sheet(self, title=None):
        self.sheet = self.workbook.create_sheet(title=title)

    def table(self, titles, rows):
        if titles:
            self.sheet.append(titles)

        for row in rows:
            processed = []
            for i, value in enumerate(row):
                if isinstance(value, date):
                    processed.append(value.strftime('%Y-%m-%d'))
                elif isinstance(value, (int, float, Decimal)):
                    processed.append(value)
                elif value is None:
                    processed.append('-')
                else:
                    processed.append(('%s' % value).strip())

            self.sheet.append(processed)

    def table_from_queryset(self, queryset, additional=()):
        opts = queryset.model._meta

        titles = ['str']
        titles.extend(field.name for field in opts.fields)
        titles.extend(a[0] for a in additional)

        data = []
        for instance in queryset:
            row = ['%s' % instance]
            for field in opts.fields:
                if field.choices:
                    row.append(
                        getattr(instance, 'get_%s_display' % field.name)())
                else:
                    row.append(getattr(instance, field.name))

            row.extend(a[1](instance) for a in additional)
            data.append(row)

        self.add_sheet(slugify('%s' % opts.verbose_name_plural))
        self.table(titles, data)

    def to_response(self, filename):
        response = HttpResponse(
            save_virtual_workbook(self.workbook),
            content_type=(
                'application/vnd.openxmlformats-officedocument.'
                'spreadsheetml.sheet'),
        )
        response['Content-Disposition'] = 'attachment; filename="%s"' % (
            filename,
        )
        return response


def create_export_selected(
        additional=(),
        short_description=_('export selected')):
    def export_selected(modeladmin, request, queryset):
        xlsx = XLSXDocument()
        xlsx.table_from_queryset(queryset, additional=additional)
        return xlsx.to_response('%s.xlsx' % modeladmin.model._meta.label_lower)
    export_selected.short_description = short_description

    return export_selected


export_selected = create_export_selected()
