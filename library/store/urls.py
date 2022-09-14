from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views
from . views import  LibrarianAPIView

urlpatterns = [
    path('list/', views.BookList.as_view()),
    path('store/<int:pk>/', views.BookDetail.as_view()),
    path('book/',LibrarianAPIView.as_view()),
    path('book/<int:pk>/', LibrarianAPIView.as_view()),
    path('return/', views.ReturnBook.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)