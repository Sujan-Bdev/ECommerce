from django.contrib import admin

from .models import Book, Category, BookLinkAuthor, Author, Customer


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'stock', 'price', 'available']
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

admin.site.register(Author)


class BookLinkAuthorAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']

    class Meta:
        model = Book


admin.site.register(BookLinkAuthor, BookLinkAuthorAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Customer, CustomerAdmin)
