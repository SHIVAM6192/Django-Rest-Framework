from django.urls import path
from .views import TaskListCreateView, AllTasksAdminView

urlpatterns = [
    # Normal user
    path('', TaskListCreateView.as_view(), name='tasks'),
    
    # Admin only
    path('admin/tasks/', AllTasksAdminView.as_view(), name='admin-tasks'),
]
