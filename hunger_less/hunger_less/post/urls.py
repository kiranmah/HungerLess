from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from . import views

urlpatterns = [
       url(r'^$', TemplateView.as_view(template_name='posts/viewposts.html'), name='posts'),
       url(r'^$', TemplateView.as_view(template_name='posts/addpost.html'), name='addpost'),

]
