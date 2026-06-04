from django.shortcuts import render
from .models import blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

class PostListView(ListView):
    model = blog
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = blog
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = blog
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']

class PostUpdateView(UpdateView):
    model = blog
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = blog
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post_list')