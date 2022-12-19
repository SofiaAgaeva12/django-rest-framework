
from rest_framework import viewsets, filters, status, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Book, Author
from snippets.serializers import BookSerializer


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class = Book
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "genre", "author__name"]
