from django.shortcuts import render
from django.views import generic
from .models import Post

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


class PostListView(generic.ListView):
    queryset = Post.objects.all().order_by('-created_at')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

from django.http import HttpResponseRedirect
@method_decorator(login_required, name='dispatch')
class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'slug', 'body',]
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


