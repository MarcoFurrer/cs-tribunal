from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user
import requests

# Create your views here.
#@unauthenticated_user
def welcome(request):
    return render(request,"welcome.html")
def instructions(request):
    return render(request,"instructions.html")
def settings(request):
    return render(request,"settings.html")
def contact(request):
    return render(request,"contact.html")
def home(request):
    return render(request,"vote.html")

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=771309151410192384&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"
def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)
def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    user = exchange_code(code)
    authenticate(request, user = user)
    #return JsonResponse({"user": user})
    return redirect('home')
def exchange_code(code:str):
    data = {
        "client_id":"771309151410192384",
        "client_secret":"7mfvS2ub9y4AU14SrB8k_ku8WVyD2BJT",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify" #todo: Welches scope nötig für Gruppen: https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data = data, headers = headers)
    print(response)
    credentials = response.json()
    access_token = credentials["access_token"]

    response = requests.get("https://discord.com/api/v6/users/@me", headers = {
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    return user
