from django.views.generic import ListView
from django.shortcuts import redirect, render
from lexique.models import Blog, Comment
from lexique.forms import BlogForm


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