from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, '../templates/base.html')


# def posts_list(request):
# 	posts = Post.objects.all()
# 	return render(request, 'blog/index.html', context={'posts': posts})