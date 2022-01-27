from django.shortcuts import render
from .models import*
# Create your views here.

def index(request):
	return render(request, 'index.html')

def blogs(request):
	blogs = Blogs.objects.filter(user=request.user)
	context = {
		'blogs':blogs
	}
	return render(request, 'blog.html',context)