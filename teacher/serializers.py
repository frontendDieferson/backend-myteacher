from dataclasses import field
from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Teacher, Classroom

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


# CADASTRAR SERIALIZER AULAS 
#TODO: Criar o serializer de cadastro de Aula

class RegisterClassesSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Deve ter pelo 3 caracteres")
        return value


class ClassroomSerializer(serializers.Serializer):
    class Meta:
        model = Classroom
        fields = '__all__'