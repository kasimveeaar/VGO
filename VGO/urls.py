from django.contrib import admin
from django.urls import path , include
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('tinymce/' , include('tinymce.urls')),
                  path('', views.home , name="home"),
                  path('about/', views.about, name="about"),
                  path('help/', views.help, name="help"),
                  path('career/', views.career, name="career"),
                  path('post/<slug:url>', views.post, name="post"),

              ] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
