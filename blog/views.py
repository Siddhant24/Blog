from django.shortcuts import render

# Create your views here.
from .models import Blogger, Blogpost, Comment
from django.views import generic

def index(request):
	return render(request, 'index.html')

class BloggerListView(generic.ListView):
	model = Blogger

class BloggerDetailView(generic.DetailView):
	model = Blogger

class BlogListView(generic.ListView):
	model = Blogpost
	paginate_by = 5

class BlogDetailView(generic.DetailView):
	model = Blogpost