from django.db import models


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

    score_hiragana = models.IntegerField(null=True, blank=True)
    score_katakana = models.IntegerField(null=True, blank=True)
    ideogramm = models.ForeignKey(Ideogramm, null=True, on_delete=models.SET_NULL)
    description = models.ForeignKey(Documentary, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.score_hiragana}-{self.score_katakana}-{self.ideogramm}"
    
