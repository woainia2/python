from rest_framework import serializers
from unsers import models


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True,min_length=1,max_length=20,error_messages={
        "required":"标题不能为空",
        "max_length":'字数超过了最大限制',

    })
    pub_date = serializers.DateField(required=True,write_only=True)
    price = serializers.DecimalField(required=True,max_digits=8,decimal_places=2)
    read = serializers.IntegerField()
    comment = serializers.IntegerField()


    def validate_title(self,data):
        if '草' in data:
            raise serializers.ValidationError("书名不能出现平不次")
        return data

    def validate(self,data):
        read = data.get('read')
        comment = data.get('comment')
        if read < comment:
            raise serializers.ValidationError('评论量不能高于阅读量')
        return data

class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        # text = serializers.IntegerField()
        model = models.BookInfo
        # fields = "__all__"
        fields = ["id","title","price","text","pub_date","read","comment"]
        extra_kwargs={
            "price":{'min_value':0,"error_messages":{"min_value":"价格不能出现负数"}},
        }
        read_only_fields=["id","text"]


























