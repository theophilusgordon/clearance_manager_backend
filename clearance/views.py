from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from .serializers import StudentSerializer
from .models import Student, Admin

class StudentLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(StudentLoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        student = Student.objects.get(reference_number=request.data['username'])
        return Response({
            'token': token.key,
            'student_id': student.id,
            'reference_number': student.reference_number,
            'full_name': student.full_name,
            'email': student.email,
        })

class AdminLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(AdminLoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        admin = Admin.objects.get(email=request.data['username'])
        return Response({
            'token': token.key,
            'admin_id': admin.id,
            'username': admin.username,
            'email': admin.email,
            'full_name': admin.full_name,
        })


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]