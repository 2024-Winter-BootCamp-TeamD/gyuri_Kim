from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:task_id>', views.task_list, name='task_list'),
    path('<int:task_id>/create/', views.create, name='create'),
]