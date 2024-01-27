from django.db import models

class StoreBookModel(models.Model):
    CHOICES = (
        ('Humor','Humor'),
        ('Sifi','Sifi'),
        ('Romantic','Romantic'),
        ('Drama','Drama'),
        ('Action','Action'),
        ('Thriller','Thriller'),
    )
    book_id = models.IntegerField(primary_key = True)
    book_name = models.CharField(max_length = 255)
    author_name = models.CharField(max_length = 255)
    book_price = models.IntegerField()
    category = models.CharField(max_length = 255,choices = CHOICES)
    first_pub = models.DateTimeField(auto_now_add = True)
    last_pub = models.DateTimeField(auto_now = True)
    book_description = models.TextField()
    
    def __str__(self):
        return f'{self.book_name}'
