# books/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('/', views.IndexView.as_view(), name='index'),
    # path('', views.book_index, name='book_index'),
    path('api/books/', views.books_list, name='books_list'),
    path('api/books/<str:pk>/', views.book_detail, name='book_detail'),
    path('books/list/', views.books_list, name='books_list'),
    
    
    
]
