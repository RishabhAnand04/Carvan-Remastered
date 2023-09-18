from django.shortcuts import render
from .models import Places,Visiting
from .serializers import PlacesDataSerializer,VisitingDataSerializer
from django.db.models import F, Case, When, Value, IntegerField
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
# @api_view(['GET', 'POST'])
class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesDataSerializer

    def get_queryset(self):
        queryset = Places.objects.all()
        my_type = self.request.query_params.get('type', None)

        order_list = ["Chandigarh", "Delhi"]  # Replace with your list of objects
        order_dict = {obj: index for index, obj in enumerate(order_list)}

        if my_type is not None:
            queryset = queryset.filter(type=my_type)
        
        #     queryset = queryset.annotate(
        #     custom_order=Case(
        #         *[When(id=key, then=Value(value)) for key, value in order_dict.items()],
        #         default=Value(len(order_list)),
        #         output_field=IntegerField()
        #     )
        # )
        queryset = sorted(queryset, key=lambda obj: order_list.index(obj.name))
        # queryset = queryset.order_by('custom_order')

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VisitingViewSet(viewsets.ModelViewSet):
    queryset = Visiting.objects.all()
    serializer_class = VisitingDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'message': 'Signup successful'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)