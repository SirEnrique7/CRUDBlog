from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'post_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
