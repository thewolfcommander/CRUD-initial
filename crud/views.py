from django.shortcuts import render
from crud import models

def home(request):
    posts = models.Post.objects.all().order_by('-updated')
    context = {
        'posts': posts,
    }
    return render(request, 'crud/home.html', context)