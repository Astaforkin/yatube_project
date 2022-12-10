from django.shortcuts import render, get_object_or_404
from .models import Post, Group

last_ten_posts = 10


def index(request):
    posts = Post.objects.all()[:last_ten_posts]
    return render(request, 'posts/index.html', {'posts': posts, })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('author')[:last_ten_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
