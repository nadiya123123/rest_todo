from django.urls import path
from api_test.v1.quickstart.views import TaskListCreate, TaskDetailUpdateDelete

app_name = "quickstart"

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDelete.as_view(), name='task-detail-update-delete'),
]