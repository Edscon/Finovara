from django.contrib import admin
from .models import ApiToken


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'encrypted_api_key')


admin.site.register(ApiToken)