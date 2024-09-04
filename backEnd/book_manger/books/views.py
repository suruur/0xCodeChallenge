from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.db_connection import books_collection  
from bson.objectid import ObjectId

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'  # Vue.js main HTML file

@api_view(['GET'])
def book_index(request):
     books = list(books_collection.find({}))
     for book in books:
        book["_id"] = str(book["_id"])
     return Response(books)
    # return Response({'message': 'Hello, World! index'}, status=status.HTTP_200_OK)
    
    
    


@api_view(['GET', 'POST'])
def books_list(request):
    if request.method == 'GET':
        # Query MongoDB and return books as a list of dictionaries
        books = list(books_collection.find({}))
        for book in books:
            book["_id"] = str(book["_id"])  # Convert ObjectId to string
        return Response(books)

    elif request.method == 'POST':
        # Extract book details from the request data
        book = {
            "title": request.data.get("title"),
            "author": request.data.get("author"),
            "published_date": request.data.get("published_date"),
            "isbn": request.data.get("isbn"),
            "genre": request.data.get("genre"),
        }
        
        # Basic validation: Check if all fields are provided
        if not all(book.values()):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Check if a book with the same title already exists
            existing_book = books_collection.find_one({"title": book["title"]})
            if not existing_book:
                # Insert the new book into the collection
                result = books_collection.insert_one(book)
                book["_id"] = str(result.inserted_id)  # Convert ObjectId to string
                return Response(book, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Book with this title already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Return any errors encountered during insertion
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = books_collection.find_one({"_id": ObjectId(pk)})
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book["_id"] = str(book["_id"])
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(book)

    elif request.method == 'PUT':
        updated_data = {
            "title": request.data.get("title"),
            "author": request.data.get("author"),
            "published_date": request.data.get("published_date"),
            "isbn": request.data.get("isbn"),
            "genre": request.data.get("genre"),
        }
        books_collection.update_one({"_id": ObjectId(pk)}, {"$set": updated_data})
        return Response(updated_data)

    elif request.method == 'DELETE':
        try :
             books_collection.delete_one({"_id": ObjectId(pk)})
             
             return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    