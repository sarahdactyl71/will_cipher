from django.urls import path

from . import views

app_name = 'ciphers'
urlpatterns = [
    #urls for caesar
    path('', views.index, name='index'),
    path('caesar/<int:caesar_id>/', views.caesar_show, name='caesar_show'),
    path('create/', views.create, name='create'),
    path('<int:caesar_id>/update/', views.update, name='update'),
    path('<int:caesar_id>/delete/', views.delete, name='delete'),
    #urls for atbash
    path('atbash/<int:atbash_id>/', views.atbash_show, name='atbash_show'),
    #urls for alphanumeric
    path('alphanumeric/<int:alphanumeric_id>/', views.alphanumeric_show, name='alphanumeric_show'),
]
