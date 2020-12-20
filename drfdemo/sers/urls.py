from sers import views
from django.urls import path,re_path
urlpatterns = [
    path("students1/",views.StudentView.as_view())
]
