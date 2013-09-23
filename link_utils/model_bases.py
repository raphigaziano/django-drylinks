"""

link_utils.model_bases.py
=========================

Abstract models for django-link-utils.

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractLinkType(models.Model):
    """
    Regroup common attributes that will be shared by all links pointing
    to the same LinkType instance.

    :name: The name of this link type, i.e. 'Facebook'

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class AbstractLink(models.Model):
    """
    Abstract base class for link objects.

    :link_type: The type of this link.
    :name:      The display name for this link.
    :url:       The href attribute of this link.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    url = models.CharField(
        max_length=4000,
        verbose_name=_('URL'),
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

