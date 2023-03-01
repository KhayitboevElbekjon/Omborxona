
from django.urls import path
# from statistika.views import *

from .views import *

urlpatterns = [
path('',StatistikaView.as_view()),
    path('st_del/<int:son>',StatistikaDelView.as_view())
]