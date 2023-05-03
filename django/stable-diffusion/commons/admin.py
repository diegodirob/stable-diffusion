from solo.admin import SingletonModelAdmin

from commons.models import SiteConfiguration
from django.contrib import admin

admin.site.register(SiteConfiguration, SingletonModelAdmin)
