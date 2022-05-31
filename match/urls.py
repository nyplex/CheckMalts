from django.urls import path
from . import views


urlpatterns = [
    path('', views.match, name='match'),
    path('result/<result>', views.match_result, name='match_result')
]