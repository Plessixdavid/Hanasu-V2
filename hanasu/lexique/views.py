from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import ListView
from lexique.models import Lexique, Blog, Comment
from lexique.forms import BlogForm
from lexique import forms


# Create your views here.
# blogs permets de recuperer tous les objets contenue dans la table Blog


# photos permets de recuperer tous les objets contenue dans la table Photos
def lexique(request):
    # lexiques va recupérer les objets contenue dans la table appartenant à l'utilisateur connecté
    lexiques = Lexique.objects.filter(user=request.user)

    lexique_paginator = Paginator(lexiques, 6)

    page_number = request.GET.get('page')

    page = lexique_paginator.get_page(page_number)

    page_range = lexique_paginator.page_range

    context ={
    "photos": lexique_paginator.count,
    "css" : "lexique/lexique_style.css",
    "css2" : "mysite/menu.css",
    "page" : page,
    'page_range': page_range
    }
    
    return render(request, "lexique/lexique.html", context)

@login_required
def lexique_upload(request):
    form = forms.LexiqueForm()
    css = "lexique/lexique_style.css"
    css2 = "mysite/menu.css"
    if request.method == 'POST':
        # nous avons besoin du formulaire contenu dans Photo.
        form = forms.LexiqueForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.user = request.user
            # now we can save
            photo.save()
            return redirect('home')

    return render(request, 'lexique/lexique_upload.html', context={'form': form, 'css':css, 'css2':css2})

@login_required
def lexique_update(request, id):
    lexique = Lexique.objects.get(id=id)
    form = forms.LexiqueForm(instance=lexique)
    css = "lexique/lexique_style.css"
    css2 = "mysite/menu.css"
    if form.is_valid():
            # mettre à jour le mot existant dans la base de données
        form.save()
            # rediriger vers la page lexique que nous venons de mettre à jour
        return redirect('hanasu_lexique')
    else:
        form = forms.LexiqueForm(instance=lexique)  # on pré-remplir le formulaire avec un mot existant

    return render(request,'lexique/lexique_update.html',{'form': form, 'css':css, 'css2':css2})

@login_required
def lexique_delete(request, id):
    lexique = Lexique.objects.get(id=id)
    css = "lexique/lexique_style.css"
    css2 = "mysite/menu.css"

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        lexique.delete()
        # rediriger vers la liste des groupes
        return redirect('lexique')

    return render(request,'lexique/lexique_delete.html',{'lexique': lexique, 'css': css, 'css2': css2})

class List(ListView):
    template_name = 'lexique/blog.html'
    queryset = Blog.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['css'] = "lexique/blog.css"
        context['css2'] = "mysite/menu.css"

        return context

def detailView(request, id):
    post = Blog.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    css = "lexique/blog.css"
    css2 = "mysite/menu.css"
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()
            return redirect('detailView', id=post.id)
    else:
        form = BlogForm()

    context = {
        'css':css,
        'css2': css2,
        'article':post,
        'comments':comments,
        'form':form,

    }
    return render(request, 'lexique/update_blog.html', context)