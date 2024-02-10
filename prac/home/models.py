from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Person(models.Model):
    color = models.ForeignKey(Color,null=True,blank=True, on_delete=models.CASCADE, related_name="color")
    name = models.CharField(max_length=100)
    age = models.IntegerField()