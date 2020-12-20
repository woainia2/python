from django.urls import path,re_path,include
from students.views import StudentAPIView

urlpatterns = []
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("stu",StudentAPIView)
urlpatterns+=router.urls