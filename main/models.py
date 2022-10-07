from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    klass = models.CharField(max_length=10, blank=True, null=True)
    python_access = models.BooleanField(default=False)
    ege_access = models.BooleanField(default=False)
    bots_access = models.BooleanField(default=False)
    last_lesson_python = models.CharField(max_length=50, default='tipy-dannyh/')  # адрес первого урока
    last_lesson_ege = models.CharField(max_length=50, default='testovyj-ege/')
    last_lesson_bots = models.CharField(max_length=50, default='nastrojka-bota/')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Категория')
    slug = models.SlugField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    price = models.CharField(max_length=20, blank=True, verbose_name='Стоимость')
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание курса')
    tutor = models.CharField(max_length=100, blank=True, verbose_name='Преподаватель')
    number_of_members = models.CharField(max_length=10, blank=True, verbose_name='Размер группы')
    category_landing = models.TextField(max_length=5000, blank=True, verbose_name='Лендинг курса')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Lesson(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Урок')
    slug = models.SlugField(max_length=30, blank=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='lessons')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class AccessBaseClass(models.Model):
    pass
