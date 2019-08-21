from django.shortcuts import render
from django.utils import timezone
from django.db import models

from .models import Post


def post_list(request):
    posts = Post.objects \
        .filter(published_at__lte=timezone.now()) \
        .order_by('published_at')
    return (render(request, 'blog/post_list.html', {
        'posts': posts
    }))
