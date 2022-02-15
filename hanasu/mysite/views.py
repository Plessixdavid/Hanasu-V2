from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Ideogramm, Ideotype, Documentary, Maneki, Score
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
    css2 = "mysite/menu.css"
    context = {
        "css": css,
        "css2": css2,
        "scores" : score,
    }

    return render(request, "mysite/user_page.html", context)


@login_required
def hanasuhome(request):
    css = "mysite/home_style.css"
    css2 = "mysite/menu.css"

    context = {
        "css": css,
        "css2": css2,
    }

    return render(request, "mysite/home_page.html", context)

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


    random_ideogramms = random.choices(ideogramms, k=2)
    random_documentary = random.choice(documentary)
    css = "mysite/maneki_style.css"
    css2 = "mysite/menu.css"
    score = Score.objects.get(user_id=request.user.id)


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
