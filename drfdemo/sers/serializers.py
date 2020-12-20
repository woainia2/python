from rest_framework import serializers
from students import models
import re


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     age = serializers.IntegerField()
#     sex = serializers.BooleanField()
#     description = serializers.CharField()
#






class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=1,max_length=8)
    age = serializers.IntegerField(max_value=200,error_messages={'max_value':'年龄不能大于200岁'})
    sex = serializers.BooleanField()
    description = serializers.CharField(required=True)



    def validate_name(self,data):
        if '666' in data:
            raise serializers.ValidationError('光喊666是不行滴')
        return data
    def validate_age(self,data):
        if data < 0:
            raise serializers.ValidationError('年龄不能为零')
        return data



    def validate(self, data):
        name = data.get('name')
        description= data.get('description')
        if name == description:
            raise serializers.ValidationError('名称不能和签名一直')
        return data

    def create(self, validated_data):
        print(">>>>>>>>>>>>>>>>>",validated_data)
        new_obj = models.Student.objects.create(**validated_data)
        return new_obj


    def update(self, instance, validated_data):
        print(validated_data)
        if validated_data.get('name'):
            instance.name = validated_data.get('name')
        if validated_data.get('age'):
            instance.age = validated_data.get('age')
        if validated_data.get('sex'):
            instance.sex = validated_data.get('sex')
        if validated_data.get('description'):
            instance.description = validated_data.get('description')

        instance.save()

        return instance