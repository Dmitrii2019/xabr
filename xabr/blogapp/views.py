import json
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views import View

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from authapp.forms import XabrUserEditForm
from blogapp.forms import BlogUserEditForm
from mainapp.models import Post

from mainapp.models import Category

from authapp.models import XabrUser


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['user', 'category', 'name', 'slug', 'description', 'posts_text']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['category', 'name', 'slug', 'description', 'posts_text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:post_list')
