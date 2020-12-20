from django.urls import path
from unsers import views
urlpatterns = [
    path("books/",views.BookInfoView.as_view()),
    path("books2/",views.BookInfo2View.as_view()),
]