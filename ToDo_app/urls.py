from django.urls import path,include
from ToDo_app import views

urlpatterns = [
    path('',views.Add_Task,name='Add_Task'),
    path('todo/',views.Task,name='Task'),
    path('delete/<int:id>',views.Delete,name='delete'),
]