from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import snippets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)