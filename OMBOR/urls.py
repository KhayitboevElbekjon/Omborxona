
from django.contrib import admin
from django.urls import path,include
from Asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('logout/',LogautView.as_view()),

    path('Asosiy/',include('Asosiy.urls')),

    path('statistika/',include('statistika.urls')),
]
