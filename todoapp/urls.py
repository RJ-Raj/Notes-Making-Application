from django.urls import path
from todoapp.views import *

urlpatterns = [
        path('', home),
        path('delete/<id>/',delete, name="delete"),
        path('update-todo/',update_doto,name="update_todo")
]
