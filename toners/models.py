from django.db import models
from django.contrib.auth.models import User
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    storeNo = models.IntegerField(unique=True)
    def __str__(self):
        return self.name

class Tonermodels(models.Model):
    name = models.CharField(max_length=100, unique=True)
    printer = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Toners(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    tonermodels = models.ForeignKey(Tonermodels, on_delete=models.CASCADE,)
    reading = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.DO_NOTHING)
    def __int__(self):
        return self.reading
