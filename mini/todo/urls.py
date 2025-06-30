from .views import TodoCreateList, TodoListview, TodoDeleteView, TodoUpdateView
from django.urls import path


urlpatterns = [
    path("", TodoListview.as_view(), name="todo_list"),
    path("create/", TodoCreateList.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),]