from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.views import APIView
from students import models
from req.serializer import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse

from django.http.request import HttpRequest
from rest_framework.response import Response

class Studentview(View):
    def get(self,request):
        print(request)
        response = HttpResponse("ok")
        print(response)
        return response


class StudentsView(APIView):



    def get(self,request):
        print(request)
        response = Response("ok")
        return response

    def get1(self,request):
        print(request.query_params)
        print(request.data)

        students = models.Student.objects.all()
        serializer = StudentModelSerializer(instance=students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            new_obj = models.Student.objects.create(**serializer.validated_data)
            obj  = StudentModelSerializer(instance=new_obj)
            return Response(obj.data)


class StudentView(APIView):

    def get(self,request,pk):

        students = models.Student.objects.filter(pk=pk).first()
        serializer = StudentModelSerializer(instance=students)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            new_obj = models.Student.objects.create(**serializer.validated_data)
            obj  = StudentModelSerializer(instance=new_obj)
            return Response(obj.data)
        else:return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        students = models.Student.objects.filter(pk=pk).first()
        data = request.data
        serializer = StudentModelSerializer(instance=students,data=data,partial=True)
        if serializer.is_valid():
            instance = serializer.save()
            new_serializer = StudentModelSerializer(instance=instance)

            return Response(new_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:return Response(serializer.error_messages)


    def delete(self,request,pk):
        models.Student.objects.filter(pk=pk).first().delect()
        return Response('', status=status.HTTP_204_NO_CONTENT)