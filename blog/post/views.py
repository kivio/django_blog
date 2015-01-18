from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from post.models import *

# Create your views here.
def hello(request):
	return HttpResponse("hello")


def list(request):
	posty = Post.objects.all()
	return render(request, "list.html", {'posty':posty})

def show(request, id):
	post = Post.objects.get(id=id)
	url = reverse('lista')
	return render(request, "show.html", {'post': post, 'url': url})
