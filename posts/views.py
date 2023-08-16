from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()

    return render(request, 'index.html',{'posts': posts})


def post(request, id):

    post = Post.objects.get(id=id)

    return render (request, 'blog-page.html', {'post': post})
