from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('usuarios.urls')),
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', views.home, name='home'),
    #path('api-log', include(u'django_api_log.urls'), name='django_api_log')
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('home2/', TemplateView.as_view(template_name='home2.html'), name='home2'),
]
