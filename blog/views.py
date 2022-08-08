from django.shortcuts import render
from django.views import generic
from .models import Post, LikeModel

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


def like_it(request):
    user = request.user
    if request.method == 'POST':
        ObjectId = int(request.POST['objectid'])
        Tip = str(request.POST['contentType'])

        # in here we filtered the particular post with its id
        likes = LikeModel.objects.filter(object_id=ObjectId, content_object=Tip)
        if likes: # if the particular post is there
            if str(user) in str(likes): # then we check the user which is us, in there
                #if we there and we returned this data, this part for saving data,
                # I mean if this data is already created than we dont have to delete and
                # create again, we just change LikeModel.liked true or false state,
                # so that if you create like and it will never delete, it just change liked or like state
                like_obj = LikeModel.objects.get(user=user,object_id=ObjectId, content_object=Tip)
            else:
                pass

        if Tip == 'Post':
            post_content_type_by = Post.objects.all().first()

            if str(user) not in str(likes):
                like = LikeModel.objects.create(user=user, liked=True, content_object=ContentType.objects.get_for_model(Tip), object_id=ObjectId)
                like.save() # if data is created then we say 'new'
                okey = 'new'

            elif str(user) in str(likes) and like_obj.liked:
                like_obj.liked = False
                like_obj.save() # if data is already there, then we save it False
                okey = 'false'

            elif str(user) in str(likes) and like_obj.liked == False:
                like_obj.liked = True
                like_obj.save() # if data is already changed to False and we save again to True
                okey = 'true'


    return render(request,'ajaxlike.html',{'likes':likes,'okey':okey})