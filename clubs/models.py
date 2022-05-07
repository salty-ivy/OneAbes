from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=200,blank=False,null=True)
    description = models.TextField(max_length=300,null=True)

    def __str__(self):
        return f'{self.pk}--{self.name}'

