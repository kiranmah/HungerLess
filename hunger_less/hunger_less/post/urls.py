from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from .views import *

urlpatterns = [
        url(r'^$', allPostsListView.as_view(), name='posts'),
        url(r'^post/add/', postCreate.as_view(), name='post-add'),
        url(r'^post/<int:pk>/', postUpdate.as_view(), name='post-update'),
]
