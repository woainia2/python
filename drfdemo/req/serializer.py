from rest_framework import serializers
from students import models


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Student
        fields='__all__'
        extra_kwargs={
            'age':{'min_value':0,'error_messages':"年龄不能为负数！"}

        }
        read_only_fields=["id"]
