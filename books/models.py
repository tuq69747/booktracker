from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)  # Ensure this field exists
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    

    def __str__(self):
        return self.title
