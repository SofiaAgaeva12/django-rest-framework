from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, generics, serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from snippets.models import Book, Author
from snippets.serializers import BookSerializer, AuthorSerializer



class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        item = BookSerializer(data=request.data)

        translated_artist = 'Художественное произведение переведенное с другого языка'
        textbook = 'Учебник'

        if Book.objects.filter(category=translated_artist,
                               publisher=request.data.get('publisher'),
                               author=request.data.get('author'),
                               title=request.data.get('title')).exist():
            raise serializers.ValidationError(
                'У этого издательства уже существует такое художественное произведение переведенное с другого языка'
            )
        if Book.objects.filter(category=textbook,
                               yearOfRel=request.data.get('yearOfRel'),
                               author=request.data.get('author'),
                               title=request.data.get('title')).exist():
            raise serializers.ValidationError(
                'Этот учебник уже был выпущен в этом издании'
            )
        if item.is_valid():
            item.save()
            return Response('Книга добавлена')
        else:
            print(item.errors)
            return Response('Ошибка. Книга недобавлена', status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre', 'author']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]