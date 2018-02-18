from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from .views import *
from django.urls import reverse_lazy

urlpatterns = [
        url(r'^$', allPostsListView.as_view(), name='posts'),
        url(r'^myposts/$', myPostsListView.as_view(), name='myposts'),
        url(r'^post/add/', postCreate.as_view(success_url=reverse_lazy('post:posts')), name='post-add', ),
        url(r'^post/(?P<pk>[\w-]+)/', postUpdate.as_view(success_url=reverse_lazy('post:posts')), name='post-update'),
        url(r'^posts/delete/(?P<pk>[\w-]+)', postDelete.as_view(), name='post-delete'),
]
