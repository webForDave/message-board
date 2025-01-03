from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'