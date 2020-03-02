from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from crud import models, forms

def home(request):
    posts = models.Post.objects.all().order_by('-updated')
    context = {
        'posts': posts,
    }
    return render(request, 'crud/home.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = forms.PostForm()
    context = {
        'form': form,
    }
    return render(request, 'crud/create_post.html', context)


def post_detail(request, slug=None, *args, **kwargs):
    post = get_object_or_404(models.Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'crud/post_detail.html', context)


@login_required
def update_post(request, slug=None, *args, **kwargs):
    obj = get_object_or_404(models.Post, slug=slug)
    if request.method == "POST":
        form = forms.PostForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('home')
    else:
        form = forms.PostForm()
    context = {
        'post': obj,
        'form': form,
    }
    return render(request, 'crud/post_update.html', context)


@login_required
def delete_post(request, slug=None, *args, **kwargs):
    obj = get_object_or_404(models.Post, slug=slug)
    if request.user.is_authenticated:
        if obj.user == request.user:
            obj.delete()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')

    
def search(request):
    if request.method == 'GET':
        query = request.GET.get("search")
        results = models.Post.objects.filter(
            Q(title__icontains=query) | 
            Q(slug__icontains=query) |
            Q(summary__icontains=query) |
            Q(description__icontains=query) |
            Q(user__username__icontains=query)
        )
        context = {
            'posts': results,
            'query': query,
        }
        return render(request, 'crud/search.html', context)