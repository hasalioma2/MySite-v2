from django.contrib import admin
from .models import Branch, Tonermodels, Toners

admin.site.register(Branch)
admin.site.register(Tonermodels)
admin.site.register(Toners)

class TonersAdmin(admin.ModelAdmin):
    list_display = ('tonermodels','created_by')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()