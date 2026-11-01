from django.shortcuts import render
from .models import Book, Student, Product

def book_list(request):
    books = Book.objects.all()
    return render(request, 'blog/book_list.html', {'books': books})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'blog/student_list.html', {'students': students})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product_list.html', {'products': products})
