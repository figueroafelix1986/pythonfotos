from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.


def blog(request):

    list_post = Post.objects.all()
    return render(request, "BlogwebApp/blog.html", {'lists_post': list_post})


def categoria(request, categoria_id):

    filtara_categoria = Categoria.objects.get(id=categoria_id)
    list_post = Post.objects.filter(categoria=filtara_categoria)
    return render(request, "BlogwebApp/categoria.html", {'filtara_categorias': filtara_categoria, 'lists_post': list_post})
