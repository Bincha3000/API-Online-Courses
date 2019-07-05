from django.urls import path
from users.views import UserCreateView, UserLogInView


app_name = 'users'
urlpatterns = [
    path('createuser/', UserCreateView.as_view(), name='createuser'),
    path('login/', UserLogInView().as_view(), name='login'),
]