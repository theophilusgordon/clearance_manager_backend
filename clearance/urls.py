from django.urls import path
from .views import StudentLoginView, AdminLoginView, StudentListView, StudentRegistrationView, DepartmentListView, UserDetailView, UserDeleteView, PasswordUpdateView

urlpatterns = [
    path('student-login/', StudentLoginView.as_view(), name='student-login'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
		path('students/', StudentListView.as_view(), name='student-list'),
		path('register-student/', StudentRegistrationView.as_view(), name='register-student'),
		path('departments/', DepartmentListView.as_view(), name='department-list'),
		path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
		path('users/user-delete/<str:user_id>/', UserDeleteView.as_view(), name='user-delete'),
    path('users/update-password/<int:user_id>/', PasswordUpdateView.as_view(), name='update-password'),
]
