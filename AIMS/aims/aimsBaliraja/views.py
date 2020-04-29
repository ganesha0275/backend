from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
#For sendOTP
import http.client
import math, random
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.conf import settings



def home(request):
    return render(request, 'HomeTwo.htm')
