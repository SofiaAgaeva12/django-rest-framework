from django.urls import path, include
from rest_framework import routers

from snippets import views
from snippets.views import CreateBook

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-book/', CreateBook.as_view(), name='create book')
]

