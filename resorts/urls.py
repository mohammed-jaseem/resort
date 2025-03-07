from django.contrib import admin
from django.urls import path, include
from web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls", namespace="web")),
    # path('', views.index, name="index"),
    # path('refer/', views.refer, name="refer"),
]


if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
