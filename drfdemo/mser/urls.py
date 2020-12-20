from mser import views
from django.urls import path,re_path
urlpatterns = [
    path("students/",views.StudentView.as_view())
]
