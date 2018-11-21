from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:caesar_id>/', views.show, name='show'),
    path('create/', views.create, name='create'),
]
