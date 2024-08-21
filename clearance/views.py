from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializer, DepartmentSerializer
from .models import Student, Admin, Department

class CustomObtainAuthToken(ObtainAuthToken):
    user_model = None

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        try:
            token = Token.objects.get(key=response.data['token'])
            user = self.user_model.objects.get(username=request.data['username'])
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'full_name': user.full_name,
                'email': user.email,
            })
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except self.user_model.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)

class StudentLoginView(CustomObtainAuthToken):
    user_model = Student

class AdminLoginView(CustomObtainAuthToken):
    user_model = Admin

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
class StudentRegistrationView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DepartmentListView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can access this view

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can access this view

    def get(self, request, user_id):
        try:
            user = Student.objects.get(id=user_id)
            serializer = StudentSerializer(user)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)