from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from snippets import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]