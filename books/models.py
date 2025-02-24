from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Unknown')  # New field
    photo = models.ImageField(upload_to='book_photos/', blank=True)  # New field
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
