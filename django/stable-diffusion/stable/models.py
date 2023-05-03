from django.db import models
from users.models import User

from commons.models import CreatedUpdatedMixin


class StableRecord(CreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
