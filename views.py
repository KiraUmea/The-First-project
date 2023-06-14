from django.http import HttpResponse
from django.db import models
# Create your views here.


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    return HttpResponse("Hey! It's your main view!!")


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def blogs(request):
    return HttpResponse("blogs")


def about(request):
    return HttpResponse("about")


def slash(request):
    return HttpResponse("/")


def slug(request):
    return HttpResponse("slug")


def slug_comment(request):
    return HttpResponse("slug/comment")


def create(request):
    return HttpResponse("create")


def slug_update(request):
    return HttpResponse("slug_update")


def slug_delete(request):
    return HttpResponse("slug_delete")


def profile_username(request):
    return HttpResponse("profile_username>")


def change_password(request):
    return HttpResponse("change_password")


def register(request):
    return HttpResponse("register")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")
