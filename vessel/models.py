from django.db import models
from django.utils.translation import ugettext_lazy as _
from sampletask.utils import choices


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    mode = models.CharField(max_length=1, default='A', choices=choices.MODE)

    class Meta:
        abstract = True


class BlockIP(BaseModel):
    ip = models.GenericIPAddressField(
        verbose_name=_('IP'),
        help_text=_('IP Address'),
        unique=True
    )
    block_status = models.BooleanField(
        verbose_name=_('Status'),
        help_text=_('Block Status'),
        default=False
    )

    def __str__(self):
        """docstring for object"""

        return str(self.ip)


class VesselInfo(BaseModel):

    speed = models.IntegerField(
        verbose_name=_('Speed'),
        null=True,
        blank=True,
        help_text=_('The speed (in knots x10) that the subject vessel is reporting according to AIS transmissions')
    )
    ship_name = models.CharField(
        verbose_name=_('Ship Name'),
        max_length=150,
        null=True,
        blank=True,
        help_text=_('The Shipname of the subject vessel')
    )
    ship_type = models.IntegerField(
        verbose_name=_('Ship Type'),
        null=True,
        blank=True,
        help_text=_('The Shiptype of the subject vessel according to AIS transmissions')
    )
    type_name = models.CharField(
        verbose_name=_('Type Name'),
        max_length=150,
        null=True,
        blank=True,
        help_text=_('The Type of the subject vessel')
    )
    imo = models.BigIntegerField(
        verbose_name=_('IMO'),
        unique=True,
        help_text=_('International Maritime Organisation number - seven-digit number that uniquely identifies vessels')
    )
    length = models.FloatField(
        verbose_name=_('Length'),
        null=True,
        blank=True,
        help_text=_('The overall Length (in metres) of the subject vessel')
    )
    width = models.FloatField(
        verbose_name=_('Width'),
        null=True,
        blank=True,
        help_text=_('The Breadth (in metres) of the subject vessel')
    )
    year_built = models.IntegerField(
        verbose_name=_('Year Built'),
        null=True,
        blank=True,
        help_text=_('The year that the subject vessel was built')
    )

    def __str__(self):
        """docstring for object"""

        return str(self.imo)

