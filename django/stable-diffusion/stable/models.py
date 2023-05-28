from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import User

from commons.models import CreatedUpdatedMixin


class StableRecord(CreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image_urls = ArrayField(models.CharField(max_length=64, blank=True), size=8, null=True, blank=True)

    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=16, null=True, blank=True)
