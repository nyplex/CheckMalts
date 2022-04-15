from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('/admin/', views.admin, name='menu_admin'),
    path('/admin/postRecipe', views.postRecipe, name = "post_friend"),
]
