from django.shortcuts import render
from firebase_admin import firestore
import pyrebase
config={
     "apiKey": "AIzaSyCeyATBXwuySMsCGxIk-7rUV-mS3p-qyE4",
    "authDomain": "contactform-fc473.firebaseapp.com",
    "databaseURL": "https://contactform-fc473-default-rtdb.firebaseio.com",
    "projectId": "contactform-fc473",
    "storageBucket": "contactform-fc473.appspot.com",
    "messagingSenderId": "1035070557982",
    "appId": "1:1035070557982:web:7094306e82429d3961430f"
}
firebase=pyrebase.initialize_app(config)
# Create your views here.
def home(request):
     name = request.POST.get("name")
     email = request.POST.get("email")
     message = request.POST.get("message")

     firebase.database().child("contactForm").push({
    "name": name,
    "email": email,
    "message": message,
     })
     return render(request, 'home.html',{})