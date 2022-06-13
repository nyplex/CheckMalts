from django.urls import path
from . import views
from allauth.account import views as allauth_views
from allauth.socialaccount import views as social_views

urlpatterns = [
    path('', views.account, name='account'),
    path('orders', views.my_orders, name='my_orders'),
    
    path('password', views.MyPasswordChangeView.as_view(), name='password'),
    path('logout', allauth_views.logout, name='account_logout'),
    path('login', allauth_views.login, name='account_login'),
    path('signup', allauth_views.signup, name='account_signup'),

    
    path("password/set", views.SetPasswordCustomView.as_view(), name="account_set_password"),
    path("inactive", allauth_views.account_inactive, name="account_inactive"),
    
    # password reset
    path('password/reset', allauth_views.password_reset,
        name='account_reset_password'),
    path('password/reset/done', allauth_views.password_reset_done,
        name='account_reset_password_done'),
    path('password/reset/key/(<uidb36>)-(<key>)',
        allauth_views.password_reset_from_key,
        name='account_reset_password_from_key'),
    path('password/reset/key/done', allauth_views.password_reset_from_key_done,
        name='account_reset_password_from_key_done'),
    
    
    path("email/$", allauth_views.email, name="account_email"),
    path("confirm-email/$", allauth_views.email_verification_sent,
        name="account_email_verification_sent"),
    path("confirm-email/(?P<key>[-:\w]+)/$", allauth_views.confirm_email,
        name="account_confirm_email"),
    
]