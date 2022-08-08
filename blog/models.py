from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )
class Post(models.Model):

  title = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=255, unique=True)
  body = RichTextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # status = models.IntegerField(choices=STATUS, default=0)
  author = models.ForeignKey(User, on_delete=models.PROTECT)
  # tags = models.ManyToManyField(Tag, blank=True, null=True)

  class Meta:
    ordering = ["-created_at"]

  def __str__(self):
    return self.title


class LikeModel(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL, null=True)
  liked = models.BooleanField()
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

  timestamp = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return str(self.user.username)



# class Profile(models.Model):
#   user = models.OneToOneField(
#     settings.AUTH_USER_MODEL,
#     on_delete=models.PROTECT,
#   )
#   website = models.URLField(blank=True)
#   bio = models.CharField(max_length=240, blank=True)

#   def __str__(self):
#     return self.user.get_username()


# class Tag(models.Model):
#   name = models.CharField(max_length=50, unique=True)

#   def __str__(self):
#     return self.name