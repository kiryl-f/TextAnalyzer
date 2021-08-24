from django.contrib import admin

from .models import Text, Language


class TextAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Text, TextAdmin)
admin.site.register(Language)
