from django.http import HttpResponse
from django.shortcuts import render

# Create Your Views 
def home(self):
    return HttpResponse("<h1> Hello My Name Is Tanmay And My PRN Is 1841011 </h1> <br>  <li><a href='login/'>Login Page</li>")

def login(self):
    return HttpResponse("<h1> Welcome To The Login Page </h1>  <br> <li><a href='/home'>Home</li>") 
