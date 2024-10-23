from django.urls import path, re_path
from .views import login, signup, test_token

urlpatterns = [
    re_path('login/', login, name='login'),
    re_path('signup/', signup, name='signup'),
    re_path('test_token/', test_token, name='test_token')
]