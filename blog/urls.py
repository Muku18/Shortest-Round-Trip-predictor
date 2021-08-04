from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.abt, name='abt'),
    path('working', views.work, name='work'),
    path('result', views.minpath, name='minpath'),

]