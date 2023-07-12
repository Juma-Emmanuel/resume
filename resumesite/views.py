from django.shortcuts import render
import pyrebase

config = {
   " apiKey": "AIzaSyCeyATBXwuySMsCGxIk-7rUV-mS3p-qyE4",
    "authDomain": "contactform-fc473.firebaseapp.com",
    "databaseURL": "https://contactform-fc473-default-rtdb.firebaseio.com",
   " projectId": "contactform-fc473",
    "storageBucket": "contactform-fc473.appspot.com",
    "messagingSenderId": "1035070557982",
   " appId": "1s:1035070557982:web:7094306e82429d3961430f"
  }

 firebase = pyrebase.initializeApp(config)

 auth = firebase.auth()
def home(request):
   

    
     return render(request, 'home.html',{})