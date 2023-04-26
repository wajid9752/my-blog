from django.urls import path
from .views import *


urlpatterns = [
    path('', home , name="home"),
    path('register/', register , name="register"),
    path('user-login/', user_login , name="user-login"),
    path('log-out/', log_out , name="log-out"),
    path('add-blog/', add_blog , name="add-blog"),
    path('profile/', profile , name="profile"),
    path('update-blog/<str:pk>/',update_blog,name="update-blog"),
    path('delete-blog/<str:pk>/',delete_blog,name="delete-blog")
]
