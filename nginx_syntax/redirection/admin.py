from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import (
    Redirection
)

classes = [Redirection]


class ModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            messages.error(request, "Only superusers can change models")
            return False
        return super(ModelAdmin, self).save_model(request, obj, form, change)


for c in classes:
    admin.site.register(c, ModelAdmin)
