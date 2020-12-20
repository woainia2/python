from rest_framework import serializers
from students import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        # fields = '__all__'
        # fields = ['name','age']
        exclude = ['name','age']  #排除某些字段
        extra_kwargs = {
            'id':{'read_only':True},
            'name':{'max_length':10}
        }  #自定义参数
