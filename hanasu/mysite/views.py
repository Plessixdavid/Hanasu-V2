from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Ideogramm, Ideotype, Documentary, Maneki, Score, Trophy
from authentication.models import User


import random




# Create your views here.

def index(request):
    css = "mysite/style.css"
    return render(request, "mysite/index.html", {"css":css})


def hanasuregister(request):
    
    css = "mysite/inscrip_style.css"
    return render(request, "mysite/inscription.html", {"css":css})

@login_required
def user_page(request):
    all_trophy = Trophy.objects.all()
    score = Score.objects.get(user_id=request.user.id)
    css = "mysite/user_page.css"
    css2 = "mysite/menu.css"

    for trophy in all_trophy:
        if score.scores_max >= trophy.trophy_score:
            # i want to check if the trophy is already in the user_trophy m2m field
            if trophy.user_trophy.filter(id=request.user.id).exists():
                print("already exists")
            else:
                trophy.user_trophy.add(request.user)
                print("does not exist")

    trophy_for_the_current_user = Trophy.objects.filter(user_trophy = request.user.id)

    print(trophy_for_the_current_user)
    context = {
        "css": css,
        "css2": css2,
        "scores" : score,
        "user_trophy" : trophy_for_the_current_user
        
    }

    return render(request, "mysite/user_page.html", context)


@login_required
def hanasuhome(request):
    css = "mysite/home_style.css"
    css2 = "mysite/menu.css"
    css3 = "mysite/flip.css"

    context = {
        "css": css,
        "css2": css2,
        "css3": css3,
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
    correct_ideogramm = random.choice(random_ideogramms)
   
    context = {
        "scores" : score,
        "correct_ideogramm" : correct_ideogramm,
        "ideogramms": random_ideogramms,
        "random_documentary": random_documentary,
        "css":css,
        "css2": css2,
        "hiragana": hiragana,
        "katakana": katakana,
        
       
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
            
            if hiragana == "on" and katakana == "off":
                score.score_hiragana +=1
            elif katakana == "on" and hiragana == "off":
                score.score_katakana +=1
            elif katakana == "on" and hiragana == "on":
                score.score_katakana +=1
                score.score_hiragana +=1
            score.save()

        # si réponse n'est pas la bonne, ajoute 1 dans le nombre de 
        # question posé et saugarde dans la table score.
        else:
            score.total_questions += 1
            score.save()
        # permet de rajouter quelque chose dans le context .
            
            context['scores'] = score
        
            
    return render(request, "mysite/maneki.html",context )
