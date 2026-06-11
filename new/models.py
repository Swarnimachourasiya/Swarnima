from django.db import models

# Create your models here.
class New(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=50)
    news_image = models.FileField( upload_to="news/", max_length=250,null=True,default=None)


