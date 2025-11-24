from django.contrib import admin
from .models import Book, Author, Category

#========================================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)

#========================================
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'website', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('birth_date',)
    ordering = ('last_name', 'first_name')

#========================================
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'stock', 'published_date', 'created_at')
    search_fields = ('title', 'isbn', 'author__first_name', 'author__last_name', 'category__name')
    list_filter = ('category', 'author', 'published_date')
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')
