from typing import Any
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
import nltk
from nltk.chat.util import Chat, reflections
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
import os
import qrcode
from django.views.decorators.http import require_POST
from reportlab.pdfgen import canvas
from django.contrib.auth import get_user_model
User = get_user_model()


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
        city = self.request.query_params.get('city', None)
        if city:
            queryset = queryset.filter(city=Places.objects.get(name=city))
            if city=="Chandigarh":
                order_list = model()
                queryset = sorted(queryset, key=lambda obj: order_list.index(obj.name))
            return queryset

        if my_type is not None:
            queryset = queryset.filter(name=my_type)

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
@csrf_exempt
def login_view(request):
    print("ansuuuuuuuuuul")
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


@csrf_exempt
@api_view(['POST'])
def generate_qr_code_and_pdf(request):
    try:
        user = request.user
        print(request.user)

        # Create a new user object
        # user = User.objects.create(name=name, email=email)

        # Generate a unique filename for the PDF
        pdf_filename = f"user_{user.id}.pdf"
        pdf_path = os.path.join("media", pdf_filename)

        # Create a QR code containing a link to the PDF
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(request.build_absolute_uri(pdf_path))
        qr.make(fit=True)

        # Generate the QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Generate the PDF with user details
        c = canvas.Canvas(pdf_path)
        c.drawString(100, 700, f"Name: {name}")
        c.drawString(100, 680, f"Email: {email}")
        # Add more details as needed
        c.save()

        # Return the QR code image URL in the response
        response_data = {
            "message": "QR code and PDF generated successfully",
            "qr_code_url": request.build_absolute_uri(pdf_path),
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)












def get_weather(city):
    try:
        # Prepare the Google Weather URL
        url = f'https://www.google.com/search?q=weather+in+{city}'

        # Send a GET request to Google
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the temperature and weather description
        temperature = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
        description = soup.find('div', {'class': 'BNeawe tAd8D AP7Wnd'}).text

        return f"The weather in {city} right now: {temperature}, {description}."
    except Exception as e:
        return f"Sorry, I couldn't fetch the weather information for {city}. Please try again later."


# List of recommendations
recommendations = [
    'Le Corbusier Center', 'Butterfly Park', 'Chandigarh Golf Club', 'Capitol Complex',
    'International Dolls Museum', 'FunCity Water Park', 'Government Museum and Art Gallery',
    'Terraced Garden', 'Terrace Garden', 'Rock Garden', 'Chandigarh Botanical Garden and Nature Park',
    'Chhatbir Zoo', 'Gurudwara Nada Sahib', 'Cactus Garden', 'Leisure Valley', 'Elante Mall',
    'Rose Garden', 'Sukhna Lake'
]

# Define a set of rules for the chatbot


# Create a chatbot using the rules and reflections
# chatbot = Chat(rules, reflections)

# # Start the chat
# print("Chatbot: Hello! How can I assist you today?")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'quit':
#         break
#     response = chatbot.respond(user_input)
#     # Combine the responses into a single string
#     chatbot_response = ''.join(response)
#     print("Chatbot:", chatbot_response)

class ChatBot(APIView):
    def post(self,request):
        return Response({'response': "YAY"})



    # def __init__(self):
    #     rules = [
    #     (r'hello|hi|hey', ['Hello!', 'Hi', 'Hey!']),
    #     (r'how are you', ['I am fine, thank you!', 'I am doing well. How about you?']),
    #     (r'(.*) your name', ['I am a chatbot.', 'I go by the name ChatGPT.']),
    #     (r'(.) help (.)', ['I can help you with a variety of tasks. Please specify what you need help with.']),
    #     (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    #     (r'(tell me about|what can you tell me about) Chandigarh', [
    #         "Sure, I can provide information about Chandigarh.",
    #         "I'd be happy to tell you more about Chandigarh.",
    #         "Here's some information about Chandigarh:",
    #         "Chandigarh is a city in India that serves as the capital of two states, Haryana and Punjab. It is known for its well-planned architecture and is often referred to as 'The City Beautiful'.",
    #         "You can find more detailed information on Chandigarh in this Wikipedia article: https://en.wikipedia.org/wiki/Chandigarh"
    #     ]),
    #     (r'(recommend|suggest) (.) (to|in) (.)', [self.recommend_location("chandigarh","chandigarh")]),
    #     (r'(what is the weather like|tell me about the weather in) (.*) right now', [self.get_weather("chandigarh")]),
    #     (r'(best time to visit|when is the ideal time to go to|when should I go to) (.*)', [
    #         "The best time to visit chandigarh is usually Post-monsoon months, starting from September and lasting till November.",
    #         "I'd recommend going to chandigarh Post-monsoon months, starting from September and lasting till November for the best experience."
    #     ]),
    #     (r'most famous cafe in (.*)', ["Garlic And Greens","Virgin Courtyard","Chilli & Pepper"]),
    #     (r'most famous restaurant in (.*)', ["Old Pal Dhaba","Swagath Restaurant","Ghazal Restaurant"]),
    #     (r'(.*)',['Sorry i am unable to solve your query please send us a detailed query at carvaan@gmail.com']),
    #     (r'quit', ['Goodbye!', 'See you later!', 'Have a great day!']),
    #     ]
    #     self.rules = rules

    # def post(self,request):
    #     request_data = request.GET.get('input', None)
    #     chatbot = Chat(self.rules, reflections)
    #     response = chatbot.respond(request_data)
    #     chatbot_response = ''.join(response)
    #     return Response({'response': chatbot_response})

    # def get_weather(self,city):
    #     try:
    #         # Prepare the Google Weather URL
    #         url = f'https://www.google.com/search?q=weather+in+{city}'

    #         # Send a GET request to Google
    #         response = requests.get(url)

    #         # Parse the HTML content
    #         soup = BeautifulSoup(response.text, 'html.parser')

    #         # Extract the temperature and weather description
    #         temperature = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
    #         description = soup.find('div', {'class': 'BNeawe tAd8D AP7Wnd'}).text

    #         return f"The weather in {city} right now: {temperature}, {description}."
    #     except Exception as e:
    #         return f"Sorry, I couldn't fetch the weather information for {city}. Please try again later."

    # def recommend_location(self,location, target_location):
    #     if location.lower() == 'chandigarh' and target_location.lower() == 'chandigarh':
    #         return f"I recommend {recommendations[0]} in {location}."
    #     else:
    #         return "I'm sorry, I can only recommend places in Chandigarh."


