
from rest_framework import viewsets, filters, status, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Book, Author
from snippets.serializers import BookSerializer, AuthorSerializer


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        item = BookSerializer(data=request.data)

        print(request.data.get('title'))
        print(request.data.get('author'))
        print(request.data.get('year_of_rel'))
        print(request.data.get('publishing_office'))
        print(request.data.get('genre'))
        print(request.data.get('category'))

        translated_artist = 'художественное произведение переведенное с другого языка'
        textbook = 'Учебник'


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
