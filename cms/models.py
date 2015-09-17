from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet


class HomePage(Page):
    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

@register_snippet
class HeaderLink(models.Model):
    url = models.CharField(null=False, blank=False, max_length=2048)
    text = models.CharField(max_length=255)
    sort_order = models.IntegerField(null=False, blank=False, default=9999)

    panels = [
      FieldPanel('url'),
      FieldPanel('text'),
      FieldPanel('sort_order'),
    ]

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Header Link"
