from django.db import models
from django.utils.translation import ugettext_lazy as _

from link_utils.model_bases import *


class LinkType(AbstractLinkType, IconMixin, LinkManagerOptsMixin):
    pass


class Link(AbstractLink, LinkOptsMixin):
    link_type = models.ForeignKey(
        LinkType,
        verbose_name=_('Link type'),
        blank=True, null=True,
    )
