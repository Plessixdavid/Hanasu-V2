from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysite.models import Ideogramm, Documentary, Maneki, Score
from authentication import models
import random
from . import models

# Create your views here.

def index(request):
    css = "mysite/style.css"
    return render(request, "mysite/index.html", {"css":css})


def hanasuregister(request):
    
    css = "mysite/inscrip_style.css"
    return render(request, "mysite/inscription.html", {"css":css})

@login_required
def user_page(request):
    score = Score.objects.get(user_id=request.user.id)
    css = "mysite/user_page.css"
    context = {
        "css": css,
        "scores" : score,
    }

    return render(request, "mysite/user_page.html", context)


@login_required
def hanasuhome(request):
    css = "mysite/home_style.css"
    return render(request, "mysite/home_page.html", {"css":css})

@login_required
def hanasugame(request):
    documentary = Documentary.objects.all()
    ideogramms = Ideogramm.objects.all()
    random_ideogramms = random.choices(ideogramms, k=2)
    random_documentary = random.choice(documentary)
    css = "mysite/maneki_style.css"
    score = Score.objects.get(user_id=request.user.id)

    context = {
        "scores" : score,
        "correct_ideogramm" : random.choice(random_ideogramms),
        "ideogramms": random_ideogramms,
        "random_documentary": random_documentary,
        "css":css
    }

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

def contact(request):
    css = "mysite/home_style.css"
    return render(request, "mysite/contact.html", {"css":css})