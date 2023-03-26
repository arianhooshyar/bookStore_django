from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Book_detail_view', args=[self.id])
