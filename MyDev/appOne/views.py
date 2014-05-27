from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from appOne.models import Blog, Customer, Book

def hello(request):
   return HttpResponse("Hello..")

def say_hi(request):
   return render_to_response("say_hi.html")
   
def index(request):
	return render_to_response("appOne/index.html")
	

def search_form(request):
	return render_to_response("search_form.html", request)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search query...')


def register(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = Customer(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/appOne/index/')
	else:
		form = Customer()
		
	form_dict = {
		'form' : form,
	}
	
	return render_to_response("appOne/index.html", context, form_dict)


def blog(request):
	context = RequestContext(request)
	blogs = Blog.objects.all()
	context_dict = {
		'blogs' : blogs,
	}
	return render_to_response("appOne/blog.html", context_dict, context)
	
