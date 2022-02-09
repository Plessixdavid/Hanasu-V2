from django.conf import settings
from django.db import models

# création de la table bdd qui contient une photo, une legende,une description une foreignkey vers le user.
class Lexique(models.Model):
    image = models.ImageField()
    romanji = models.CharField(max_length=128, blank=True)
    traduction = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=300, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
 
 
class Blog(models.Model):
    
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)