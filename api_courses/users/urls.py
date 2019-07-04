from django.urls import path
from users.views import UserCreate


app_name = 'users'
urlpatterns = [
    path('createuser/', UserCreate.as_view(), name='createuser'),
]