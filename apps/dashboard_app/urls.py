"""courses_project URL Configuration

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
from . import views

def test(request, id):
    print "@@@@@@@@@@@@@@@@@"
    print id

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signinPage$', views.signinPage),
    url(r'^signin$', views.signin),
    url(r'^registerPage$', views.registerPage),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.displayUsers),
    url(r'^users/(?P<id>\d+)/edit$', views.editUserPage),
    url(r'^(?P<id>\d+)/edit/info$', views.editUserInfo),
    url(r'^(?P<id>\d+)/edit/password$', views.editUserPass),
    url(r'^dashboard/(?P<id>\d+)$', views.displayWall),
    url(r'^comment/(?P<user_id>\d+)/(?P<message_id>\d+)/(?P<owner_id>\d+)$', views.newComment),
    url(r'^message/(?P<user_id>\d+)/(?P<owner_id>\d+)$', views.newMessage),

]
