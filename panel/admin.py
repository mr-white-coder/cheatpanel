from django.contrib import admin

# Register your models here.
from .models import Client, LicenseKey, Product

admin.site.site_header = 'Cheats administration'

class LicenseKeyInline(admin.TabularInline):
    model = LicenseKey


class LicenseKeyAdmin(admin.ModelAdmin):
    list_display = ('product', 'time_left', 'expire_date', 'client', )
    list_filter = ('product', 'client',)


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        LicenseKeyInline,
    ]


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        LicenseKeyInline,
    ]


admin.site.register(LicenseKey, LicenseKeyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)