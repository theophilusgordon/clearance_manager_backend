from django.urls import path
from .views import StudentLoginView, AdminLoginView, StudentListView, StudentRegistrationView, DepartmentListView

urlpatterns = [
    path('student-login/', StudentLoginView.as_view(), name='student-login'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
		path('students/', StudentListView.as_view(), name='student-list'),
		path('register-student/', StudentRegistrationView.as_view(), name='register-student'),
		path('departments/', DepartmentListView.as_view(), name='department-list'),
]
