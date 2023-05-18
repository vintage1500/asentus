from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Service(models.Model):
    title = models.CharField(verbose_name='Название сервиса', max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(verbose_name='Описание сервиса')
    image = models.ImageField(verbose_name='Фото', upload_to='photos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(verbose_name='Название сервиса', max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(verbose_name='Описание сервиса')
    image = models.ImageField(verbose_name='Фото', upload_to='photos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
