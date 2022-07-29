from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class SoccerNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class WorldSoccerNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class BaseballNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class WorldBaseballNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class BasketballNewsData(models.Model):
    index = models.CharField(max_length=4, null=True, default='')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")

class EsportsNewsData(models.Model):
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
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.content

class Encourage(models.Model):
    content = models.CharField(max_length=30)
    def __str__(self):
        return self.content

class Game(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
