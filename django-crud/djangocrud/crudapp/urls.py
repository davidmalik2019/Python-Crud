from django.urls import path
from .import views
from .import viewstech

urlpatterns = [
    path('', views.index, name="index"),
    path('teacher/', viewstech.indextech, name='indextech'),
    
]
