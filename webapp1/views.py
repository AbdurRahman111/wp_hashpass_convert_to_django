from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import get_hasher
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    all_wp_usr = User.objects.filter(password__startswith='$P$B')
    hasher = get_hasher('phpass')

    for user in all_wp_usr:
        print(user.password)
        user.password = hasher.from_orig(user.password)
        user.save()
        print(user.pk)
        print(user.password)

    return HttpResponse('convert done')