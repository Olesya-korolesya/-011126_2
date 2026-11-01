from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),

    path('students/', views.student_list, name='student_list'),

    path('products/', views.product_list, name='product_list'),
]