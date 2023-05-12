from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.CharField(verbose_name="작성자", max_length = 30)
    title = models.TextField(verbose_name="제목", max_length = 100)
    contents = models.TextField(verbose_name="내용")

