from django.urls import path
from . import views

urlpatterns = [
    path('', views.expert_profile_list, name='expert_list'),  
    path('<int:pk>/', views.expert_profile_detail, name='expert_detail'),
]
