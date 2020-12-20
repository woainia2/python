from django.shortcuts import render

# Create your views here.
from unsers.models import BookInfo
from django.views import View
from django.http.response import JsonResponse
from unsers.serializer import BookInfoSerializer

class BookInfoView(View):
    def post1(self,request):
        serializer = BookInfoSerializer(data=request.POST)
        result = serializer.is_valid()
        print(result)
        if not result:
            print(serializer.errors)
            print(serializer.error_messages)
            return JsonResponse(serializer.error_messages)
        else:
            print(serializer.validated_data)

            instance = BookInfo.objects.create(**serializer.validated_data)
            serializer = BookInfoSerializer(instance=instance)
            return JsonResponse(serializer.data)


from unsers.serializer import BookInfoModelSerializer

class BookInfo2View(View):
    def get(self,request):
        book_list=BookInfo.objects.all()
        serializer=BookInfoModelSerializer(instance=book_list,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        data = request.body
        import json
        data = json.loads(data.decode())

        serialize = BookInfoModelSerializer(data=data)
        serialize.is_valid()
        instance = serialize.save()
        serialize = BookInfoModelSerializer(instance=instance)
        return JsonResponse(serialize.data)

