from django.db import models

# Create your models here.
from backend.models import Category, upload_image_path


class UpcomingBook(models.Model):
    title = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created_date = models.DateField("Added Date", auto_now=False, auto_now_add=False)
    updated_date = models.DateField("Updated Date", auto_now=False, auto_now_add=False)
    launched_date = models.DateField("Launched Date", auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
