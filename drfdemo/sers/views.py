# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.http.response import JsonResponse
from sers.serializers import StudentSerializer
from students.models import Student
import json


class StudentView(View):
    def get1(self,request):
        student = Student.objects.get(pk=1)
        serializer = StudentSerializer(instance=student)
        print(serializer.data)
        return JsonResponse(serializer.data)

    def get2(self,request):
        pk = request.GET.get("pk")
        student = Student.objects.filter(pk=pk).first()
        serializer = StudentSerializer(instance=student)
        print(serializer.data)
        return JsonResponse(serializer.data)

    def get(self,request):
        pk = request.GET.get("id")
        if pk:
            student = Student.objects.filter(pk = pk).first()
            serializer = StudentSerializer(instance=student)
            return JsonResponse(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students,many=True)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        student = json.loads(request.body.decode())
        serializer=StudentSerializer(data=student)
        print(serializer)
        if serializer.is_valid():
            stu = serializer.save()
            serializer = StudentSerializer(instance=stu)
            print(stu)
            return JsonResponse(serializer.data)
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.error_messages)

    def put(self,request):
        str = request.body.decode()
        newstudent = json.loads(str)
        print('>>>>>',str)
        print(newstudent)

        oldStudent = Student.objects.filter(pk = newstudent.get('id')).first()
        serializer = StudentSerializer(instance=oldStudent,data=newstudent,partial=True)
        if not serializer.is_valid():
            print(serializer.errors)
            print(serializer.error_messages)
            if serializer.errors:
                jsonShuju = serializer.errors
            else:jsonShuju = serializer.error_messages
            return JsonResponse(jsonShuju)
        else:
            newStudent = serializer.save()
            print(newStudent)
            newSerializer = StudentSerializer(instance=newStudent)
            print(newSerializer)
            return JsonResponse(newSerializer.data)






















