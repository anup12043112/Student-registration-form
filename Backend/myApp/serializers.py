from rest_framework import serializers
from .models import RegisterationForm, Course, Department

class RegistrationFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterationForm
        fields = '__all__'



class Departmenterializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):
    department = Departmenterializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'course', 'department']


class CourseAddingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"