from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post(request):
	post = Post.objects.all()
	return render(request, 'example/new_post.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'example/post_detail.html', {'post': post})

