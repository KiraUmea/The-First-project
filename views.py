from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'index.html')


def blogs(request):
    return HttpResponse('Blogs')


def about(request):
    return HttpResponse('about')


def slash(request):
    return HttpResponse('/')


def slug(request):
    return HttpResponse('slug')


def slug_comment(request):
    return HttpResponse('Here will be some comments')


def create(request):
    return HttpResponse('Create new post')


def slug_update(request):
    return HttpResponse('Update a post')


def slug_delete(request):
    return HttpResponse('Delete a post')


def profile_username(request):
    return HttpResponse('Profile of user')


def change_password(request):
    return HttpResponse('change_password')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return HttpResponse('Log in')


def logout(request):
    return HttpResponse('Log out')


def main(request):
    return render(request, 'main.html')


def create_blog(request):
    return render(request, 'create_blog.html')
