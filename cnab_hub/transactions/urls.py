from django.urls import path
from transactions import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/', views.upload, name='upload'),
    path('lista_operacoes/', views.lista_operacoes, name='lista_operacoes'),
]