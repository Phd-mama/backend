from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.expert_profile_list, name='expert_list'),  
    path('<int:pk>/', views.expert_profile_detail, name='expert_detail'),
]
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
