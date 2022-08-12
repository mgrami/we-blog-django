from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, LikePost

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


class PostListView(generic.ListView):
  queryset = Post.objects.all().order_by('-created_at')
  template_name = 'blog/post_list.html'
  context_object_name = 'posts'

  def get_queryset(self):
    query = self.request.GET.get('q')
    if query:
        result = Post.objects.filter(title__icontains=query)
    else:
        result = Post.objects.all()
    return result


class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  context_object_name = 'post'

  def get_context_data(self, **kwargs):
    post_slug = self.kwargs['slug']
    context = super(PostDetailView, self).get_context_data(**kwargs)
    context['total_likes'] = LikePost.objects.filter(post__slug=post_slug, liked=True).count()
    return context


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


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
@login_required(login_url='/accounts/login/')
def like_the_post(request, slug):
  user = request.user
  print('submitted')
  print(request)
  print(request.user)
  if request.method == 'POST':
    post_id = int(request.POST.get('post_id'))
    post = get_object_or_404(Post, pk=post_id)

    try:
      like_post = LikePost.objects.get(user=request.user, post_id=post_id)
      like_post.liked = not like_post.liked
      like_post.save()
    except LikePost.DoesNotExist:
      like_post = LikePost(user=request.user, post_id=post_id, liked=True)
      like_post.save()

    total_likes = LikePost.objects.filter(post__id=post_id).count()

    return redirect('/'+slug+'/')



