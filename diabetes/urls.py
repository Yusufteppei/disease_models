from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('diagnose', views.diagnose, name='diagnose'),
    path('url', views.calculate_bmi, name='bmi')
]
