from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribe = models.BooleanField(default=False)
    name = models.CharField(max_length=10, blank=True)
    army_type = models.CharField(max_length=15, blank=True)
    unit_type = models.CharField(max_length=15, blank=True)
    birthday = models.CharField(max_length=15, blank=True)
    enter_date = models.CharField(max_length=15, blank=True)
    sub_type1 = models.CharField(max_length=15, blank=True)
    sub_type2 = models.CharField(max_length=15, blank=True)
    stock_type = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, name={self.name}'
    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):        
        if created:          
            Profile.objects.create(user=instance)  
    
    @receiver(post_save, sender=User)  
    def save_user_profile(sender, instance, **kwargs):        
        instance.profile.save()
    
