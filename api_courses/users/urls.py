from django.urls import path
from users.views import UserCreateView, UserLogInView, UserLogOutView


app_name = 'users'
urlpatterns = [
    path('createuser/', UserCreateView.as_view(), name='createuser'),
    path('login/', UserLogInView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]
