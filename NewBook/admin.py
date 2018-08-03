from django.contrib import admin

# Register your models here.
from NewBook.models import UpcomingBook


class UpcomingBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author','launched_date']
    list_display_links = ['title']
    list_per_page = 50
    ordering = ['title']
    search_fields = ['title']

    class Meta:
        model = UpcomingBook


admin.site.register(UpcomingBook,UpcomingBookAdmin)
