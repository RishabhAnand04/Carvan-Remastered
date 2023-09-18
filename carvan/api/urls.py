# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacesViewSet,VisitingViewSet,signup,login_view,ChatBot

router = DefaultRouter()
router.register(r'Places', PlacesViewSet)
router.register(r'Visiting', VisitingViewSet)
# router.register(r'Chat', ChatBot)

urlpatterns = [
    path('', include(router.urls)),
]
