from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('secret_santa_game.urls')),
    path('admin/', admin.site.urls),
]
