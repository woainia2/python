# Create your views here.
from rest_framework.views import APIView
from demo.serializer import StudentModelSerializer
from students.models import Student
from rest_framework.response import Response
from rest_framework import status


class Student1APIView(APIView):
    def get(self,request):
        student_all = Student.objects.all()
        serializer = StudentModelSerializer(instance=student_all,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = StudentModelSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = StudentModelSerializer(instance=instance)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class Student2APIView(APIView):
    def get(self,request,pk):
        try:
            student = Student.objects.filter(pk = pk).first()
        except Student.DoesNotExist:
            return Response({"error":"对不起，当前学生不存在"},status=status.HTTP_204_NO_CONTENT)

        serializer = StudentModelSerializer(instance=student)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):

        student = Student.objects.filter(pk = pk).first()
        print(request.data)
        serializer = StudentModelSerializer(instance=student,data=request.data)

        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = StudentModelSerializer(instance=instance)
        return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)

    def delete(self,request,pk):
        try:
            student = Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            return Response({"error":"对不起，无法查询到删除对象！"},status=status.HTTP_204_NO_CONTENT)
        student.delete()
        return Response({"message":"ok"},status=status.HTTP_204_NO_CONTENT)





