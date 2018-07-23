import os
import random

from django.db import models
from django.urls import reverse
from django.utils.timesince import timesince
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
# Create your models here.
from django.utils.encoding import smart_text


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(filepath)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = instance
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "books/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename)


class Category(models.Model):
    title = models.CharField('title', max_length=100, default='')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)

    def get_absolute_url(self):
        pass


class Book(models.Model):
    title = models.CharField("Book Name", max_length=100, blank=False)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category, verbose_name='Category;', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    page = models.IntegerField("Page", null=True)
    publish_date = models.DateField("Published Date", auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return "/book/{slug}/".format(slug=self.slug)

    def age(self):
        return timesince(self.publish_date)


class Author(models.Model):
    name = models.CharField("Name", max_length=100, blank=False)
    email = models.EmailField("Email", max_length=50, blank=False, null=True)


    # image

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class BookLinkAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


def book_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(book_pre_save_receiver, sender=Book)
