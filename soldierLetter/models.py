from django.db import models
from django.utils import timezone

# Create your models here.

class SportNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class FinanceNewsData(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class FinanceData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class Tip(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Encourage(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    def __str__(self):
        return self.title