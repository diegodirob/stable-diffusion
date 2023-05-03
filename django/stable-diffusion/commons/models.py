from django.db import models
from solo.models import SingletonModel


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteConfiguration(SingletonModel):
    stability_api_key = models.CharField(null=True, blank=True, max_length=255,)

    def __str__(self):
        return 'Site Configuration'

    class Meta:
        verbose_name = 'Site Configuration'
