from rest_framework import serializers
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Book, Author


