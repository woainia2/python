from rest_framework import serializers
from students import models

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"
