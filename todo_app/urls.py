from django.urls import path

from . import views

app_name = "todo_app"
urlpatterns = [
    path('', views.TodoView.as_view(), name="todos"),
    path('todo_create/', views.todo_create, name="todo_create"),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo_edit'),
    path('delete_selected/', views.delete, name='delete_selected'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]