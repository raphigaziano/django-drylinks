"""

drylinks.mixins.py
==================

Model mixins for django-link-utils.
Use & combine those to add basic fields & functionality to your custom
Link objects.

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class HtmlAttrsMixin(models.Model):
    """
    Common options that can be applied to a Link, LinkType or LinkCategory.

    :css_classes:   Set of classes than can be used when generating the html
                    markup for this object

    """
    css_classes = models.CharField(
        max_length=256,
        verbose_name=_('CSS Classes'),
        blank=True,
    )

    class Meta:
        abstract = True


class LinkHtmlAttrsMixin(HtmlAttrsMixin):
    """
    Common options than can be applied to an individual Link object.

    :target_blank:  Whether or not this link should open in a new tab/window
                    (generated <a> element will include a "target="blank"
                    attribute)
    :title:         The title attribute of this link.

    """
    target_blank = models.BooleanField(
        default=False,
        verbose_name=_('Open in a new window / tab'),
    )
    title = models.CharField(
        max_length=512,
        verbose_name=_('Title'),
        blank=True,
    )

    class Meta:
        abstract = True


class ExternalUrlMixin(models.Model):
    """
    A basic mixin providing a single URLField to store external urls.

    :url:       Django validated URLField.

    """
    url = models.URLField(
        verbose_name=_('URL'),
    )

    class Meta:
        abstract = True


class InternalUrlMixin(ExternalUrlMixin): # ?? URLField ok ?
    """
    A mixin providing internal links based on a set of models.

    Classes implementing this mixin need to define a QUERYSET field, which
    must be an iterable of available models.

    """

    def __new__(cls, *args, **kwargs):
        super(InternalUrlMixin, cls).__new__(*args, **kwargs)
        cls._Meta.fields['url'].choices = (('foo', 'bar'))

    class Meta:
        abstract = True


class IconMixin(models.Model):
    """
    Provide an icon field to subclasses.

    :icon: An image associated to this link object. Could be used for an actual 
        icon, a clickable image, etc...

    """
    icon = models.ImageField(
        upload_to='drylinks/icons',
        verbose_name=_('Icon'),
        blank=True, null=True,
    )

    class Meta:
        abstract = True
