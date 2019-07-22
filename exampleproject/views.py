from django.shortcuts import render
from .models import New_Post
from django.utils import timezone

def new_post(request):
	posts = New_Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'example/new_post.html', {'posts': posts})
