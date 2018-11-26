from django.urls import path

from . import views

app_name = 'ciphers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:caesar_id>/', views.show, name='show'),
    path('create/', views.create, name='create'),
    path('<int:caesar_id>/update/', views.update, name='update'),
    path('<int:caesar_id>/delete/', views.delete, name='delete'),
]
