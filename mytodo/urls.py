# mytodo/urls.py
from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"), # あとで使う
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path("update/<int:pk>/", mytodo.update, name="update"),
    path("delete/<int:pk>/", mytodo.delete, name="delete"),
    
    
]