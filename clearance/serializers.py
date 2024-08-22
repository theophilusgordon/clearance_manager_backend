from rest_framework import serializers
from .models import Student, Admin, Department, DepartmentClearance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'reference_number', 'department', 'gender', 'level', 'phone_number', 'password']
        extra_kwargs = {
					'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.set_password(password)
        student.save()
        return student

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'code']
        
class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
class DepartmentClearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentClearance
        fields = ['id', 'clearance_start_date', 'description', 'department', 'user', 'status']