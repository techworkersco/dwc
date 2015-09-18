from django import template
from cms.models import *

register = template.Library()

@register.inclusion_tag('cms/tags/header_links.html', takes_context=True)
def header_links(context):
    return {
        'header_links': HeaderLink.objects.order_by('sort_order', 'text').all(),
        'request': context['request'],
    }

@register.inclusion_tag('cms/tags/footer_copy.html', takes_context=True)
def footer_copy(context):
    return {
        'footer_copy_blocks': FooterCopyBlock.objects.order_by('sort_order').all(),
        'request': context['request'],
    }

@register.inclusion_tag('cms/tags/footer_links.html', takes_context=True)
def footer_links(context):
    return {
        'footer_links': FooterLink.objects.order_by('sort_order').all(),
        'request': context['request'],
    }
