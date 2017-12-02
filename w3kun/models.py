from django.db import models

# Create your models here.

class Author(models.Model):
	ursName = models.CharField(max_length=50,default='Name')
	ursPassword = models.CharField(max_length=50,default='******')
	email = models.EmailField(blank=True)
	

	def __str__(self):
		return self.ursName
		
class Article(models.Model):
	title = models.CharField(max_length=50,default='Title',null=True)
	content = models.TextField(null=True)
	time = models.DateTimeField('最后修改日期', auto_now = True)
	
	
	author = models.ForeignKey(Author,related_name='author',null=True)
	def __str__(self):
		return self.title
class Comment(models.Model):
	comment = models.TextField(null=True)
	
	launchtime = models.DateTimeField('发布日期', auto_now = True)
	writer = models.ForeignKey(Author,related_name='writer',null=True)
	article = models.ForeignKey(Article,related_name='article')
	def __str__(self):
		return self.writer +"|" +self.launchtime