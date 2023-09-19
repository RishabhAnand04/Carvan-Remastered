# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacesViewSet,VisitingViewSet,signup,login_view,ChatBot,generate_qr_code_and_pdf,GenerateTicketPDF

router = DefaultRouter()
router.register(r'Places', PlacesViewSet)
router.register(r'Visiting', VisitingViewSet)
# router.register(r'Chat', ChatBot)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('generate/', generate_qr_code_and_pdf, name='generate'),
    path('generate_ticket/', GenerateTicketPDF.as_view(), name='generate_ticket'),
]
