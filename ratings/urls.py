"""ratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from ratings import views

urlpatterns = [
    url(r'^ratings/$', views.all_ratings), # GET
    url(r'^ratings/(?P<zipcode>[0-9]{5})/$', views.ratings_for_zipcode), # GET
    url(r'^rating/(?P<zipcode>[0-9]{5})/$', views.average_rating_for_zipcode), # GET
    url(r'^rating/(?P<zipcode>[0-9]{5})/(?P<user_id>[0-9]*)/$', views.single_rating), # GET, DELETE
    url(r'^rating/$', views.create_or_update_rating), # POST
]