from demo import views
from django.urls import path,re_path
urlpatterns = [
    path("student1/",views.Student1APIView.as_view()),
    re_path("student1/(?P<pk>\d+)/",views.Student2APIView.as_view()),

    # path("students/",views.StudentsView.as_view()),
    # re_path("students/(?P<pk>\d+)/",views.StudentView.as_view())
]
