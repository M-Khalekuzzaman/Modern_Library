from django.db import models

class UpdateUserInfoModel(models.Model):
    CATEGORY = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    user_image = models.ImageField(upload_to='photos/userimg',blank=True)
    phone_number = models.CharField(max_length = 11)
    dob = models.DateField()
    gender = models.CharField(max_length = 200,choices = CATEGORY)
    age = models.IntegerField()
    address = models.CharField(max_length = 255)
    description = models.TextField(max_length = 100)
    
    def __str__(self):
        return f'{self.user_image}'
