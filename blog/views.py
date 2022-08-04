from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_at')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# .filter(status=1)