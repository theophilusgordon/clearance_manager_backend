from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from clearance.models import Admin, Student

class AdminStudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        try:
            user = Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            try:
                user = Student.objects.get(reference_number=username)
            except Student.DoesNotExist:
                return None

        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            try:
                return Student.objects.get(pk=user_id)
            except Student.DoesNotExist:
                return None