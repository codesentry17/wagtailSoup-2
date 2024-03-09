from django.db import models
from wagtail.models import TranslatableMixin


class Team(TranslatableMixin):
    """Adding team mates' details"""

    display_pic = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    full_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=100, blank=True, null=True)
    contact = models.URLField()

    class Meta:
        unique_together = ('translation_key', 'locale')

    def __str__(self) -> str:
        return self.full_name


# Create your models here.