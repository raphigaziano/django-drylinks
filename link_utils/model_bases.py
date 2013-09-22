from django.db import models
from django.utils.translation import ugettext_lazy as _


### Helper Mixins ###


class LinkManagerOptsMixin(models.Model):
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


class LinkOptsMixin(LinkManagerOptsMixin):
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


class IconMixin(models.Model):
    """
    Provide an icon field to subclasses.

    :icon: An image associated to this link object. Could be used for an actual 
        icon, a clickable image, etc...

    """
    icon = models.ImageField(
        upload_to='link_utils/icons',
        verbose_name=_('Icon'),
        blank=True, null=True,
    )

    class Meta:
        abstract = True


### Abstract Models ###


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

