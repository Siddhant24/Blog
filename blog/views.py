from django.shortcuts import render
from .models import Blogger, Blogpost, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

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

from .forms import AddCommentForm

def add_comment(request, pk):
	blog = get_object_or_404(Blogpost, pk = pk)
	if request.method == 'POST':
		form = AddCommentForm(request.POST)

		if form.is_valid():
			comment = Comment.objects.create(commenter=request.user,description=form.cleaned_data['description'],blogpost=blog,post_date=datetime.date.today(),post_time=datetime.datetime.now().time())
			comment.save()

			return HttpResponseRedirect('/blog/%s' % (pk))

	else:
		form = AddCommentForm()

	return render(request, 'blog/add_comment.html', {'form': form})

