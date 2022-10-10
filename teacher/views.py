from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from teacher.models import Classroom, Teacher
from teacher.serializers import TeacherSerializer, ClassroomSerializer, RegisterClassesSerializer


class TeacherAPIView(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True,)
        return Response(serializer.data, status=HTTP_200_OK)


class RegisterClassAPIView(APIView):
    def post(self, request, id, format=None):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = RegisterClassesSerializer(data=request.data)
        if serializer.is_valid():
            classroom = Classroom(
                name=serializer.validated_data.get('name'),
                email=serializer.validated_data.get('email'),
                teacher=teacher
            )
            classroom.save()
            classroom_serializer = ClassroomSerializer(classroom, many=False)
            return Response(classroom_serializer.data, status=HTTP_201_CREATED)
        return Response({"message": "Houveram erros de validação", "erros": serializer.errors}, status=HTTP_400_BAD_REQUEST)
