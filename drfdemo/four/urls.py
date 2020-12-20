from req import views
from django.urls import path,re_path
urlpatterns = [
    path("student/",views.StudentView.as_view()),
    path("students/",views.StudentsView.as_view()),
    re_path("students/(?P<pk>\d+)/",views.StudentView.as_view())
]
