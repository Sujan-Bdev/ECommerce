from django.contrib import admin

from .models import Book, Category, BookLinkAuthor, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Author, AuthorAdmin)


class BookLinkAuthorAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']

    class Meta:
        model = Book


admin.site.register(BookLinkAuthor, BookLinkAuthorAdmin)
