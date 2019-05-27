from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200,unique=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
