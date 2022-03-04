from django.db import models
from authentication.models import User



# Create your models here.
# permets de créer des table dans la BDD avec les diférents champs inclus à l'interieur.

# Class Ideogramm contenant un champs : Name, Romanji, Img_link et Id_type_idéo permettant un 
# lien avec la table Ideotype.



class Ideotype(models.Model):
    Name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.Name}"

class Ideogramm(models.Model):
    
    romanji = models.CharField(max_length=50, null=True)
    Img_link = models.CharField(max_length=100, null=True)
    # faire foreign pour joindre les types d'ideogramm
    ideotype = models.ForeignKey(Ideotype, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.romanji} - {self.Img_link} - {self.ideotype}"

class Documentary(models.Model):

    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.description}"

class Maneki(models.Model):

    ideogramm = models.ForeignKey(Ideogramm, null=True, on_delete=models.SET_NULL)
    description = models.ForeignKey(Documentary, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.ideogramm}"

class Score(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)   
    maneki = models.ForeignKey(Maneki, null=True, blank=True, on_delete=models.SET_NULL)
    last_game = models.DateTimeField(null=True)
    current_score = models.IntegerField(null=True, blank=True, default=0)
    score_hiragana = models.IntegerField(null=True,blank=True, default=0)
    score_katakana = models.IntegerField(null=True,blank=True, default=0)
    total_questions = models.IntegerField(null=True, blank=True, default=0)
    scores_max = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.current_score}-{self.scores_max}-{self.user}"

class Trophy(models.Model):
    user_trophy = models.ManyToManyField(User, blank=True)
    trophy_name = models.CharField(max_length=255,null=True , blank=True)
    trophy_score = models.IntegerField(null=True, blank=True, default=0)
    link = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.trophy_name}-{self.trophy_score}-{self.link}"