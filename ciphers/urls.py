from django.urls import path

from . import views

app_name = 'ciphers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:caesar_id>/', views.show, name='show'),
    path('create/', views.create, name='create'),
]
