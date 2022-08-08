from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', lambda req: __import__('django.http', fromlist=['http']).JsonResponse({"user": req.user.email})),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
