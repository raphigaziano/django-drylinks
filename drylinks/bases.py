"""

drylinks.model_bases.py
=======================

Abstract models for django-drylinks.

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import mixins

class AbstractLink(models.Model):
    """
    Abstract base class for link objects.

    :link_type: The type of this link.
    :label:     The display name for this link.
    :url:       The href attribute of this link.

    """
    label = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
        blank=True,
    )
    url = models.CharField(
        max_length=4000,
        verbose_name=_('URL'),
        blank=True,
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.label


