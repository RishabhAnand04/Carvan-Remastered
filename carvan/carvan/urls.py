# project/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import login_view,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]
