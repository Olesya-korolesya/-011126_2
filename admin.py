from django.contrib import admin
from .models import Book, Student, Product

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'published')
    search_fields = ('title', 'author')
    list_filter = ('published',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'birth_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


