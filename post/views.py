from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, ContactForm
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	contex ={
		"form" : form, 
	}
	return render(request, "post_form.html", contex)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	contex = {
		"title" : "detail",
		"instance" : instance,
		"form" : form
	}
	return render(request,"post_form.html",contex)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return render(request,"post_detail.html")
def post_detail(request, slug, id=None):
	instance = get_object_or_404(Post, id=id)
	contex = {
		"title" : "detail",
		"instance" : instance,
	}
	return render(request,"post.html",contex)

def post_list(request):
	queryset_list = Post.objects.filter(draft=False)
	paginator = Paginator(queryset_list, 10)

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	contex = {
		"object_list" : queryset,
		"title" : "LIST"
	}
	return render(request,"index.html",contex)

def contact_send(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return render(request,"contact.html")

def category(request, id=None):
	queryset_list = Post.objects.filter(draft=False,category=id)
	paginator = Paginator(queryset_list, 10)

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	contex = {
		"object_list" : queryset,
	}
	return render(request,"index.html",contex)