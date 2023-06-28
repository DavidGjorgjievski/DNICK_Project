from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    exclude = ("owner",)
    list_display = ('name', 'manufacturer', 'color', 'storage', 'used', 'price', 'image', 'location')
    list_filter = ('manufacturer', 'color', 'used')
    search_fields = ('name', 'manufacturer')

    # Customize the form fields displayed in the admin add/edit pages
    fieldsets = (
        (None, {
            'fields': ('name', 'manufacturer', 'color', 'storage', 'used', 'price')
        }),
        ('Images', {
            'fields': ('image','location'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Phone, PhoneAdmin)