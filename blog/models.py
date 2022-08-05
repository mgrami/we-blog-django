from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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



# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

class Post(models.Model):

  title = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=255, unique=True)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # status = models.IntegerField(choices=STATUS, default=0)
  author = models.ForeignKey(User, on_delete=models.PROTECT)
  # tags = models.ManyToManyField(Tag, blank=True, null=True)

  class Meta:
    ordering = ["-created_at"]

  def __str__(self):
    return self.title



