# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacesViewSet,VisitingViewSet,signup,login_view,ChatBot,GenerateTicketPDF

router = DefaultRouter()
router.register(r'Places', PlacesViewSet)
router.register(r'Visiting', VisitingViewSet)
# router.register(r'Chat', ChatBot)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('generate_ticket/', GenerateTicketPDF.as_view(), name='generate_ticket'),
]
