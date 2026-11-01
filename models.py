from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    published = models.DateField(verbose_name="Дата публикации")

    def __str__(self):
        return f"{self.title} — {self.author}"

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"
