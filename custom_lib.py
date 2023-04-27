from django.db import models
from django.contrib.auth.models import User


def authentication_library(request):
    if request.user.is_authenticated:
        return True
    return False 

def login_lib(username,password):
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return user
        return None
    except User.DoesNotExist:
        return None