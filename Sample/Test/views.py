from django.http import HttpResponse
from django.shortcuts import render

# Create Your Views 
def home(self):
    return HttpResponse("Hello My Name Is Tanmay And My PRN Is 1841011")

def login(self):
    return HttpResponse("Welcome To The Login Page")
    