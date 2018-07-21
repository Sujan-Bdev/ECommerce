from django.contrib import admin

from .models import Book, Category, BookLinkAuthor, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'stock', 'available']
    list_display_links = ['title']
    list_per_page = 50
    ordering = ['title']
    search_fields = ['title']

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_per_page = 20
    search_fields = ['name']


admin.site.register(Author, AuthorAdmin)


class BookLinkAuthorAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']

    class Meta:
        model = Book


admin.site.register(BookLinkAuthor, BookLinkAuthorAdmin)
