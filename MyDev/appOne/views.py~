from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from appOne.models import Blog, Customer, Book
from appOne.forms import PostForm

def hello(request):
   return HttpResponse("Hello..")

def say_hi(request):
   return render_to_response("say_hi.html")
   
def index(request):
	return render_to_response("appOne/index.html", request)
	

def search_form(request):
	return render_to_response("search_form.html", request)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'appOne/index.html',
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

def submit_post(request):
	
	"""
		If user clicked 'submit' button(POST)
		Validate form
		Save Form
		Show all posts
		Throw errors (if any)
	"""
	context = RequestContext(request)
	
	if request.POST:
		postform = PostForm(data=request.POST)
		if postform.is_valid():
			postform.save(commit=True)
			return HttpResponseRedirect('/appOne/blog/')
		else:
			print postform.errors 
	else:
		postform = PostForm()
		print postform # Not Neccessary
		
	context_dict = {
		'postform' : postform,
	}
		
	return render_to_response("appOne/submitpost.html", context_dict, context)


