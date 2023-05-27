from django.contrib import admin
from django.urls import path, include
import todo_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_app/', include('todo_app.urls')),
]
