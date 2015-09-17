from django import template
from cms.models import *

register = template.Library()

@register.inclusion_tag('cms/tags/header_links.html', takes_context=True)
def header_links(context):
    return {
        'header_links': HeaderLink.objects.order_by('sort_order', 'text').all(),
        'request': context['request'],
    }
