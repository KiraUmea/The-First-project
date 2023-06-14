from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    return HttpResponse("Our blogs")

def about(request):
    return HttpResponse("About")

def slug(request):
    return HttpResponse("<slug>")

def slug_comment(request):
    return HttpResponse("<slug>/comment/")

def create(request):
    return HttpResponse("create")

def slug_update(request):
    return HttpResponse("<slug>/update/")

def slug_delete(request):
    return HttpResponse("<slug>/delete/")

def profile_username(request):
    return HttpResponse("profile/<username>/")

def change_password(request):
    return HttpResponse("change_password")

def register(request):
    return HttpResponse("register")

def login(request):
    return HttpResponse("login")

def logout(request):
    return HttpResponse("logout")
