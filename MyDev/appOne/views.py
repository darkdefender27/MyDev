from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from appOne.models import Blog, Customer

def hello(request):
   return HttpResponse("Hello..")

def say_hi(request):
   return render_to_response("say_hi.html")
   
def index(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = Customer(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/index/')
	else:
		form = Customer()
		
	form_dict = {'form' : form}
	return render_to_response("appOne/index.html", context, form_dict)
	
def blog(request):
	context = RequestContext(request)
	blogs = Blog.objects.all()
	context_dict = {
		'blogs' : blogs,
	}
	return render_to_response("appOne/blog.html", context_dict, context)
	
