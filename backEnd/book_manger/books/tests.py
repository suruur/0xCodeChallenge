from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import MagicMock, patch
from bson.objectid import ObjectId


class BooksAPITestCase(APITestCase):

    def setUp(self):
        # Sample data for testing
        self.book_data = {
            "title": "Test Book",
            "author": "Author Name",
            "published_date": "2024-01-01",
            "isbn": "1234567890123",
            "genre": "Fiction"
        }
        self.book_id = str(ObjectId())
        self.book_data_with_id = {**self.book_data, "_id": self.book_id}

    @patch('books.views.books_collection.find')
    def test_book_index(self, mock_find):
        mock_find.return_value = [self.book_data_with_id]  # Mock the find method
        url = reverse('book_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book_data['title'])

    
    
    
    
    @patch('books.views.books_collection.find_one')
    @patch('books.views.books_collection.insert_one')
    def test_books_list_post(self, mock_insert_one, mock_find_one):
        # Mock find_one to simulate no existing books with the same title
        mock_find_one.return_value = None
        
        # Mock insert_one to simulate a successful insert
        mock_insert_result = MagicMock()
        mock_insert_result.inserted_id = "mock_id"  # Mock ObjectId as a string
        mock_insert_one.return_value = mock_insert_result

        # Set up the data for the post request
        url = reverse('books_list')
        self.book_data = {
            "title": "Test Book",
            "author": "Author Name",
            "published_date": "2024-01-01",
            "isbn": "1234567890",
            "genre": "Fiction"
        }
        
        # Perform the post request
        response = self.client.post(url, self.book_data, format='json')
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
    
    
    

    @patch('books.views.books_collection.find')
    def test_books_list_get(self, mock_find):
        mock_find.return_value = [self.book_data_with_id]  # Mock the find method
        url = reverse('books_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['_id'], self.book_id)

    @patch('books.views.books_collection.find_one')
    @patch('books.views.books_collection.update_one')
    def test_book_detail_put(self, mock_update_one, mock_find_one):
        mock_find_one.return_value = self.book_data_with_id  # Mock find_one
        mock_update_one.return_value = None  # Mock update_one
        url = reverse('book_detail', args=[self.book_id])
        updated_data = {**self.book_data, "title": "Updated Title"}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    @patch('books.views.books_collection.find_one')
    @patch('books.views.books_collection.delete_one')
    def test_book_detail_delete(self, mock_delete_one, mock_find_one):
        mock_find_one.return_value = self.book_data_with_id  # Mock find_one
        mock_delete_one.return_value = None  # Mock delete_one
        url = reverse('book_detail', args=[self.book_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @patch('books.views.books_collection.find_one')
    def test_book_detail_get(self, mock_find_one):
        mock_find_one.return_value = self.book_data_with_id  # Mock find_one
        url = reverse('book_detail', args=[self.book_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['_id'], self.book_id)

    @patch('books.views.books_collection.find_one')
    def test_book_detail_get_not_found(self, mock_find_one):
        mock_find_one.return_value = None  # Mock find_one returning None
        url = reverse('book_detail', args=[self.book_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)