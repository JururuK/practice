from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True) #지워도 작성자미상의 글로 남도록.

    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='article',null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)