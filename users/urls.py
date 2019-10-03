from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('ajax/users/create/', views.user_create, name='user_create'),
    path('ajax/users/update/<int:pk>', views.user_update, name='user_update'),
    path('ajax/users/delete/<int:pk>', views.user_delete, name='user_delete'),
]