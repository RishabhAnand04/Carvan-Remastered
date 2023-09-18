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
from carvan.settings import BASE_DIR
import json
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Create your views here.
# @api_view(['GET', 'POST'])
class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesDataSerializer

    def get_queryset(self):
        queryset = Places.objects.all()
        my_type = self.request.query_params.get('type', None)

        if my_type is not None:
            queryset = queryset.filter(type=my_type)

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

    def get_queryset(self):
        queryset = Visiting.objects.all()
        my_type = self.request.query_params.get('type', None)

        order_list = model()

        if my_type is not None:
            queryset = queryset.filter(type=my_type)

        queryset = sorted(queryset, key=lambda obj: order_list.index(obj.name))

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
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
        
def model():
    # Load the dataset
    with open(BASE_DIR/"carvan"/"data"/"places_dataset.json", 'r') as file:
        data = json.load(file)

    # Extract features (rating, visits_per_month, ticket_price, hours_open, family_friendly)
    features = np.array([
        [place["rating"], place["visits_per_month"], place["ticket_price"], place["hours_open"], int(place["family_friendly"])]
        for place in data["places"]
    ])

    # Normalize the features using StandardScaler
    scaler = StandardScaler()
    normalized_features = scaler.fit_transform(features)

    # Create target labels (ranking based on features)
    rankings = np.argsort(np.argsort(-normalized_features.sum(axis=1)))

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(normalized_features, rankings, test_size=0.2, random_state=42)

    # Build a neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')  # Linear activation for regression
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

    # Evaluate the model on the test data
    loss = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}")

    # Make recommendations based on model predictions
    recommendation_scores = model.predict(normalized_features).flatten()
    sorted_indices = np.argsort(recommendation_scores)[::-1]
    recommended_places = [data["places"][i]["name"] for i in sorted_indices]

    result=[]
    # Print the recommended places
    for i, place_name in enumerate(recommended_places):
        result.append(place_name)
    
    return result