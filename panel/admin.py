from django.contrib import admin

# Register your models here.
from .models import Client, LicenseKey, Game, Post

admin.site.site_header = 'Cheats administration'

class LicenseKeyInline(admin.TabularInline):
    model = LicenseKey


class LicenseKeyAdmin(admin.ModelAdmin):
    list_display = ('game', 'time_left', 'expire_date', 'client', )
    list_filter = ('game', 'client',)


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        LicenseKeyInline,
    ]


class GameAdmin(admin.ModelAdmin):
    inlines = [
        LicenseKeyInline,
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(LicenseKey, LicenseKeyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Game, GameAdmin)
