from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length=64,help_text='snack title',default='Snack') #the type of this input is char
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE) #to use the defult table "user"and using cascading properity
    description = models.TextField(default='description')#text input

    def __str__(self): #naming the objects when adding to table
        return self.title
    
    def get_absolute_url(self):
        return reverse('snacks_detail', args=[self.id]) #to redirect the user to the snack detail