from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token),
    path('', include('home.urls', namespace='home')),
    path('todo/', include('todo.urls', namespace='todo')),
]
