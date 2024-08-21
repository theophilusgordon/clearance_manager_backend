from rest_framework import serializers
from .models import Student, Admin

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'reference_number', 'gender', 'level', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        student = Student.objects.create(**validated_data)
        if password:
            student.set_password(password)
        student.save()
        return student

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
