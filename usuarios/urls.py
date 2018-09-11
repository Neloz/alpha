from django.urls import path, include
from . import views


urlpatterns = [
    #path('registro/', views.signup_view, name="registro"),
    path('login/', views.LoginIn.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    #path('list/', views.Lista.as_view(), name="list"),
    #path('api/', views.UserAPI.as_view(), name="apiusuario"),
    #path('apilist/', views.Userlist.as_view(), name="apilist"),
#    path('useapi/', views.UserViewSet)
]
