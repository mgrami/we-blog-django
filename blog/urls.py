from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    # path('like/', views.like_it, name='post_like'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/like_post/', views.like_the_post, name='like_post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]