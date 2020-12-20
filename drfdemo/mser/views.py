from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from mser.serializers import StudentSerializer
from django.http import JsonResponse
from students import models

class StudentView(APIView):

    def get(self,request):
        all_student = models.Student.objects.all()
        serializer_obj = StudentSerializer(instance=all_student,many=True)

        return JsonResponse(serializer_obj,safe=False)



    def post(self,request):
        serializer_obj = StudentSerializer(data=request.data)
        if serializer_obj.is_valid():
            obj = serializer_obj.save()
            new_obj = StudentSerializer(instance=obj)
            return JsonResponse(new_obj)

        else:
            return JsonResponse({'error':'校验失败'})
