from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Author
from django.urls import reverse
from .forms import AuthorForm
# Create your views here.
from .import models

	
def indexPage(request):
	comment_query = models.Comment.objects.order_by('-launchtime')[:5]
	return render(
		request,
		'new1.html',
		context={
			'comment_list':comment_query,
			}
		)

def RegisterPage(request):
	return render(request,'register2.html')
	
def RegisterPage1(request):
	
	if request.method =='POST':
		form = AuthorForm(request.POST)
		all=models.Author.objects.all()
		bool_1=0
		bool_2=0
		
		if form.is_valid():
			author = form.save(commit=False)
			for name in all:
				if author.ursName == name.ursName:
						bool_1=1
						if author.ursPassword == name.ursPassword:
							bool_2=1
							pk = name.id
			if bool_2==1:
				return HttpResponseRedirect(reverse('author',kwargs={'pk':pk}))
			elif bool_1==1:
				return render(request,'register2.html',context={'warnning':'密码错误'})
			else :
				return render(request,'register2.html',context={'warnning':'用户名不存在'})
	else:
		return render(request,'register2.html')
	
def registerPage(request):
	return render(request,'register.html')
		
def registerPage1(request):
	
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		all=models.Author.objects.all()
		bool = 0
		account = 0
		if form.is_valid():
			author = form.save(commit=False)
			for name in all:
					account = account+1
					if author.ursName == name.ursName:
						bool=1
			if bool == 1:
				return render(
						request,
						'register.html',
						context={'warnning':'用户名已被注册'},
						)
			if bool == 0:
				author.save()
				pk = account+1
				return HttpResponseRedirect(
					reverse('author',kwargs={'pk':pk})
						)
	else:
		return render(request,'register.html')

def mainPage(request,pk):
	comment_query = models.Comment.objects.order_by('-launchtime')[:5]
	a = Author.objects.get(id=pk)
	return render(
			request,
			'mainPage.html',
			context={'author':a,'comment_list':comment_query,},
			)
			