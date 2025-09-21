from django import template
from django_jalali.templatetags import jformat

register = template.Library()


@register.filter
def jalali_date(value, date_format="%Y/%m/%d"):
    if value:
        return jformat.jstrftime(value, date_format)
    return ""
