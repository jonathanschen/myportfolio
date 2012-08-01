from django.http import HttpResponse
from jonathanschen.models import *
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import time 
from calendar import month_name

def index(request):
	return render_to_response('index.html',{'error': 'try again'})
	
def about(request): 
	return render_to_response('about.html')
		
def portfolio(request): 
	return render_to_response('portfolio.html')
	
def blog(request): 
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)
	
	try: page = int(request.GET.get("page", "1"))
	except ValueError: page = 1
	
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	return render_to_response("blog.html", {'posts': posts, 'user': request.user, 'post_list': posts.object_list, 'months': mkmonth_lst()})

def post(request, pk):
	post = Post.objects.get(pk=int(pk))
	comments = Comment.objects.filter(post=post)
	d = {'post': post, 'comments': comments, 'form': CommentForm(), 'user':request.user}
	d.update(csrf(request))
	return render_to_response("post.html", d)

def month(request, year, month):
	posts = Post.objects.filter(created__year=year, created__month=month)
	return render_to_response("blog.html", {'post_list':posts, 'user':request.user, 'months':mkmonth_lst(), 'archive':True})


def mkmonth_lst():
	if not Post.objects.count(): return []
	#set up vars
	year, month = time.localtime()[:2]
	first = Post.objects.order_by("created")[0]
	fyear = first.created.year
	fmonth = first.created.month
	months = []
	
	for y in range(year, fyear-1, -1):
		start, end = 12, 0
		if y == year: start = month
		if y == fyear: end = fmonth-1
		
		for m in range(start, end, -1):
			months.append((y, m, month_name[m]))
	return months
	
def contact(request):	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			
		
			recipients = ['jonathanschen@gmail.com']
			send_mail(name, message, sender, recipients)	
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form':form,})

def thanks(request):
	thanks = 'Thanks for reaching out, I\'ll be in touch soon!'
	return render_to_response('thanks.html', {'thanks': thanks})

