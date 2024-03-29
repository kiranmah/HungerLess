from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#Model Imports 
from .models import post, postlink,foodtype
from .tables import PostTable
from .filters import PostFilter
from django_tables2 import SingleTableView,RequestConfig
from django_filters.views import FilterView
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.core import mail
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class allPostsListView(FilterView, SingleTableView):
    queryset = post.objects.all()
    table_class = PostTable
    template_name = "posts/viewposts.html"
    paginate_by = 6
    filterset_class = PostFilter

    def get_table_kwargs(self):
        kwargs = super(allPostsListView, self).get_table_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self, **kwargs):
        qs = super(allPostsListView,self).get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super(allPostsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        print(context)
        return context

@method_decorator(login_required, name='dispatch')
class myPostsListView(FilterView, SingleTableView):
    queryset = post.objects.all()
    table_class = PostTable
    template_name = "posts/viewposts.html"
    paginate_by = 6
    filterset_class = PostFilter

    def get_table_kwargs(self):
        kwargs = super(myPostsListView, self).get_table_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self, **kwargs):
        qs = super(myPostsListView,self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(myPostsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        print(context)
        return context

@method_decorator(staff_member_required, name='dispatch')
class postCreate(CreateView):
    model = post
    template_name = "posts/post_form.html"
    fields = ['date','collectdate','address','description','foodtype','quantity','quality']

    def get_form(self):
        form = super(postCreate, self).get_form()
        form.fields['date'].widget.attrs.update({'class': 'datepicker'})
        return form
        
    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(postCreate, self).form_valid(form)
        
@method_decorator(staff_member_required, name='dispatch')
class postUpdate(UpdateView):
    model = post
    template_name = "posts/post_form.html"
    fields = ['date','collectdate','address','description','foodtype','quantity','quality']

    def get_form(self):
        form = super(postUpdate, self).get_form()
        form.fields['date'].widget.attrs.update({'class': 'datepicker'})
        return form

@method_decorator(staff_member_required, name='dispatch')
class postDelete(DeleteView):
    model = post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy('post:posts')

    def get_success_url(self):
        return reverse_lazy('post:posts')

    