# authentication/views.py
from django.contrib.auth import login, logout, authenticate  # import des fonctions login et authenticate
from django.shortcuts import render, redirect
from django.conf import settings
from . import forms


def logout_user(request):
    #utilise la fonction logout puis redirect redirige vers la page login.
    logout(request)
    return redirect('login')


def login_page(request):
    message=""
    # affiche le formulaire créer grace à abstractuser.
    form = forms.LoginForm()
    # vérifie si le formulaire est complet et si il est complet effectue la methode post.
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        # vérifie si les champs sont valide ou non-valide et envoie un message en conséquence.
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f'Bienvenue {user.username}, vous êtes connecté(e){{/hanasu_home}}'
                return redirect ('home')
            else:
                message = 'Identifiants invalide, veuillez recommencer.'
                return redirect ('index')
    css = "authentication/login_style.css"
    return render(request, 'authentication/login.html', context = {'form': form , "css":css , 'message': message}) 

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        #condition si le formulaire est valide, on sauve le formulaire et on le login
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('home')
    css = "authentication/inscrip_style.css"
    return render(request, 'authentication/inscription.html', context={'form': form, "css":css})