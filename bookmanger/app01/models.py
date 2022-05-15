from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(verbose_name="书名",max_length=16)

    def __str__(self):
        return self.name
