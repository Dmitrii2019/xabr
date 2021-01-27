from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def index(request):
    posts = Post.objects.all().order_by('-create_datetime')
    categories = Category.objects.all()

    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'mainapp/index.html', context)


def post(request, slug):
    posts = Post.objects.filter(slug=slug)
    categories = Category.objects.all()
    context = {
        'page_title': 'хабр',
        'posts': posts,
        'categories': categories
    }
    return render(request, 'mainapp/post.html', context)


def help(request):
    categories = Category.objects.all()
    context = {
        'page_title': 'помощь',
        'categories': categories
    }
    return render(request, 'mainapp/help.html', context)


def category_page(request, slug):
    categories = Category.objects.all()
    if slug == '':
        category = {'slug': '', 'name': 'все'}
        posts = Post.objects.all().order_by('-create_datetime')
    else:
        category = get_object_or_404(Category, slug=slug)
        posts = category.post_set.order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'categories': categories,
        'category': category,
        'posts': posts,
    }
    return render(request, 'mainapp/category_page.html', context)
