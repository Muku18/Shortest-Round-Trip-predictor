from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('working', views.work, name='work'),
    path('result', views.minpath, name='minpath'),

]