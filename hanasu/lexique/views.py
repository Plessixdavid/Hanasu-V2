
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect, render
from . import models
from . import forms


# Create your views here.
@login_required
def blog(request):
    blogs = models.Blog.objects.all()
    css = "lexique/blog.css"
    return render(request, "lexique/blog.html", context={'blogs': blogs, "css":css})

@login_required
def lexique(request):
    photos = models.Lexique.objects.all()
    css = "lexique/lexique_style.css"
    return render(request, "lexique/lexique.html", context={'photos': photos, "css":css})

@login_required
def lexique_upload(request):
    form = forms.LexiqueForm()
    if request.method == 'POST':
        # nous avons besoin du formulaire contenu dans Photo.
        form = forms.LexiqueForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            lexique.save()
            return redirect('home')
    css = "lexique/lexique_style.css"
    return render(request, 'lexique/lexique_upload.html', context={'form': form, 'css':css})

@login_required
def lexique_update(request, id):
    lexique = models.Lexique.objects.get(id=id)
    form = forms.LexiqueForm(instance=lexique)
    if form.is_valid():
            # mettre à jour le mot existant dans la base de données
        form.save()
            # rediriger vers la page lexique que nous venons de mettre à jour
        return redirect('hanasu_lexique')
    else:
        form = forms.LexiqueForm(instance=lexique)  # on pré-remplir le formulaire avec un mot existant
    css = "lexique/lexique_style.css"
    return render(request,'lexique/lexique_update.html',{'form': form, 'css':css})

@login_required
def lexique_delete(request, id):
    lexique = models.Lexique.objects.get(id=id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        lexique.delete()
        # rediriger vers la liste des groupes
        return redirect('lexique')
    css = "lexique/lexique_style.css"
    return render(request,'lexique/lexique_delete.html',{'lexique': lexique, 'css': css})