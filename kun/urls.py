"""kun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import w3kun.views as x

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^index1/$',x.indexPage,name='index1'),
	url(r'^register/$',x.registerPage,name='register'),
	url(r'^register1/$',x.registerPage1,name='register1'),
	url(r'^Register/$',x.RegisterPage,name='Register'),
	url(r'^Register1/$',x.RegisterPage1,name='Register1'),
	url(r'^author/(?P<pk>[0-9]+)/$',x.mainPage,name='author')
	url(r'^message/$',x.message,name='message')
]
