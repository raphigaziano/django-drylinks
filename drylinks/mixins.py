"""

drylinks.mixins.py
==================

Model mixins for django-drylinks.
Use & combine those to add basic fields & functionality to your custom
Link objects.

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import lazy


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


class InternalUrlMixin(models.Model):
    """
    A mixin providing internal links based on a set of models.

    Classes implementing this mixin need to define a ``__CHOICES__`` field,
    which must be an iterable of available models.
    Models listed in the ``__CHOICES__`` field can be either actual model
    objects or "app_name.model_name" strings.

    """

    # Lazy loading inspired by this article:
    # http://blog.yawd.eu/2011/allow-lazy-dynamic-choices-djangos-model-fields/

    def __init__(self, *args, **kwargs):
        super(InternalUrlMixin, self).__init__(*args, **kwargs)
        self._meta.get_field_by_name('url')[0]._choices = lazy(
            self.__get_choices, list
        )()

    class Meta:
        abstract = True

    def __get_choices(self):
        if getattr(self, '__CHOICES__', None) is None:
            pass # TODO: Raise ImroperConfig
        return [('foo', 'bar')]


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
