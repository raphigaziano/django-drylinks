"""

drylinks.mixins.py
==================

Model mixins for django-drylinks.
Use & combine those to add basic fields & functionality to your custom
Link objects.

"""
from collections import Iterable

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import lazy


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
            self.__get_choices, tuple   # Should check for an iterator,
        )()                             # but collections.Iterable doesn't work...
                                        # (not listed in list or tuple's mro)

    class Meta:
        abstract = True

    def __get_choices(self):
        if getattr(self, '__CHOICES__', None) is None:
            pass  # TODO: Raise ImroperConfig
        return self.__CHOICES__
