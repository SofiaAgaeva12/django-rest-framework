from rest_framework import viewsets, filters, status, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Book, Author
from snippets.serializers import BookSerializer, AuthorSerializer
from django.core.exceptions import ValidationError


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            if (Book.objects.get(title=request.data['title']).publishing_office != request.data['publishing_office'] and
                    request.data['category'] == 'художественное произведение, переведенное с другого языка'):
                serializer.is_valid()
            if (Book.objects.get(title=request.data['title']).publication != request.data['publication'] and
                    request.data['category'] == 'учебник'):
                serializer.is_valid()
            else:
                raise ValidationError(self.errors)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def create(self, request, *args, **kwargs):
    #     item = BookSerializer(data=request.data)
    #
    #     translated_artist = 'Художественное произведение переведенное с другого языка'
    #     textbook = 'Учебник'
    #
    #     if Book.objects.filter(category=translated_artist,
    #                            publishing_office=request.data.get('publishing_office'),
    #                            author=request.data.get('author'),
    #                            title=request.data.get('title')).exist():
    #         raise serializers.ValidationError(
    #             'У этого издательства уже существует такое художественное произведение переведенное с другого языка'
    #         )
    #     if Book.objects.filter(category=textbook,
    #                            publication=request.data.get('publication'),
    #                            author=request.data.get('author'),
    #                            title=request.data.get('title')).exist():
    #         raise serializers.ValidationError(
    #             'Этот учебник уже был выпущен в этом издании'
    #         )


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
