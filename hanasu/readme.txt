# Hanasu

## Introduction

Summary: Develop a web application using all the knowledge acquired during the course.
Objectives: The final project must reflect your new knowledge and your ability to implement it for 
the benefit of the greatest number of people, i.e. deal with a social / associative / community / 
humanist / environmental / health issue, in short, be useful to a maximum number of people, to the
planet.
Or provide a direct benefit for a member of your family (for example, support or help in the creation of an artistic activity or a micro-business).
In all cases it must be free and non-commercial software.

Hanasu is a web and mobile web application for learning Japanese.

## Installation

Download Python 3.9 or newer
Create a virtual environment with the command: py -m venv my_env
Activate the virtual environment with the command: my_env/Scripts/activate
Install the dependencies with the command: pip install -r requirements.txt

## Code Samples

Several features are available: A registration and login system (Django has a password security 
system via hashing), a "home" page with a menu and different links leading to the application pages.

The "Maneki Neko Game" is a memory game that allows to associate images with their respective names. 
If the answer is correct the player gets 1 point, if the player is wrong the page refreshes to display 
a new question.

The Lexicon allowing to add, modify or delete words or notions of Japanese in a database.

The Blog allowing to add, modify or delete information or articles (only usable by the Web-Master 
in a database.)

A "My Account" page allowing to access the players' data.

class Ideogramm(models.Model):
    
    romanji = models.CharField(max_length=50, null=True)
    Img_link = models.CharField(max_length=100, null=True)
    # faire foreign pour joindre les types d'ideogramm
    ideotype = models.ForeignKey(Ideotype, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.romanji} - {self.Img_link} - {self.ideotype}"


@login_required

def hanasugame(request):

    documentary = Documentary.objects.all()

    # hiragana = "on" ou "off"
    hiragana = request.GET.get("hiragana", "off")
    # katakana = "on" ou "off"
    katakana = request.GET.get("katakana", "off")
    
    # si hiragana est "on" et katakana est "off" filtre pour avoir que les hiragana.
    if hiragana == "on" and katakana == "off":
        ideogramms = Ideogramm.objects.filter(ideotype_id = Ideotype.objects.get(Name = "Hiragana"))
    # si katakana est "on" et hiragana est "off" alors on filtre pour avoir que les katakana.
    elif katakana == "on" and hiragana == "off":
        ideogramms = Ideogramm.objects.filter(ideotype_id = Ideotype.objects.get(Name = "Katakana"))
    # sinon prendre toute la table ideogramm.
    else:
        ideogramms = Ideogramm.objects.all() 

    # choisi 2 ideogramm dans la liste ideogramm
    random_ideogramms = random.choices(ideogramms, k=2)
    # choisi 1 documentary dans la liste documentary
    random_documentary = random.choice(documentary)
    css = "mysite/maneki_style.css"
    css2 = "mysite/menu.css"
    score = Score.objects.get(user_id=request.user.id)

    #permet d'afficher dans le html les informations désirés
    context = {
        "scores" : score,
        "correct_ideogramm" : random.choice(random_ideogramms),
        "ideogramms": random_ideogramms,
        "random_documentary": random_documentary,
        "css":css,
        "css2": css2,
        "hiragana": hiragana,
        "katakana": katakana
    }
    #si la method est post (envoie) 
    if request.method == "POST":
        # ID de la réponse qui vient d'etre cliqué
        current = request.POST['current']
        
        # L'ID de la bonne réponse
        correct = request.POST['correct']
        
        # si la reponse est la bonne: ajout du point dans les colonnes score 
        # et ajoute 1 dans le nombre de question posé.
        if correct == current:
            score.total_questions += 1
            score.current_score += 1
            score.scores_max += 1
            # sauvegarde les données dans la table score.
            score.save()
        # si réponse n'est pas la bonne, ajoute 1 dans le nombre de 
        # question posé et saugarde dans la table score.
        else:
            score.total_questions += 1
            score.save()
        # permet de rajouter quelque chose dans le context .
            context['score'] = score
            
    return render(request, "mysite/maneki.html",context )


class Lexique(models.Model):

    image = models.ImageField()
    romanji = models.CharField(max_length=128, blank=True)
    traduction = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=300, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True ,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)

## author

Plessix David.