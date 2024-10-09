from django.db import models

class Review(models.Model):
    book_title = models.CharField(max_length=255)
    positive_points = models.TextField()
    negative_points = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
