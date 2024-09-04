from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import settings

class BookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        books = list(settings.books_collection.find())
        for book in books:
            book['_id'] = str(book['_id'])  # Convert ObjectId to string
        return Response(books)

    def post(self, request):
        new_book = request.data
        settings.books_collection.insert_one(new_book)
        return Response(new_book, status=status.HTTP_201_CREATED)

    def put(self, request, book_id):
        updated_book = request.data
        settings.books_collection.update_one({'_id': book_id}, {'$set': updated_book})
        return Response(updated_book)

    def delete(self, request, book_id):
        settings.books_collection.delete_one({'_id': book_id})
        return Response(status=status.HTTP_204_NO_CONTENT)
