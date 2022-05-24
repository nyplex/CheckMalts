"""CheckMalts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as allauth_views
from profiles.views import MyPasswordChangeView, LoginCustomView

from importlib import import_module
from allauth.socialaccount import providers
from allauth.socialaccount import views as social_views
from allauth import app_settings



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('profile/', include('profiles.urls')),
    path('', include('home.urls')),
    path('menu', include('menu.urls')),
    path('order', include('order.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    
    # path("signup/$", allauth_views.signup, name="account_signup"),
    # path("login", allauth_views.login, name="account_login"),
    # path("logout/$", allauth_views.logout, name="account_logout"),

    # path("password/change/$", MyPasswordChangeView.as_view(),
    #     name="account_change_password"),
    
    # path("password/set/$", allauth_views.password_set, name="account_set_password"),

    # path("inactive/$", allauth_views.account_inactive, name="account_inactive"),

    # E-mail
    # path("email/$", allauth_views.email, name="account_email"),
    # path("confirm-email/$", allauth_views.email_verification_sent,
    #     name="account_email_verification_sent"),
    # path("confirm-email/(?P<key>[-:\w]+)/$", allauth_views.confirm_email,
    #     name="account_confirm_email"),

    # # password reset
    # path("password/reset/$", allauth_views.password_reset,
    #     name="account_reset_password"),
    # path("password/reset/done/$", allauth_views.password_reset_done,
    #     name="account_reset_password_done"),
    # path("password/reset/key/(<uidb36>)-(<key>)/$",
    #     allauth_views.password_reset_from_key,
    #     name="account_reset_password_from_key"),
    # path("password/reset/key/done/$", allauth_views.password_reset_from_key_done,
    #     name="account_reset_password_from_key_done"),
    
    
    # path(
    # "login/cancelled/",
    # social_views.login_cancelled,
    # name="socialaccount_login_cancelled",
    # ),
    # path("login/error/", social_views.login_error, name="socialaccount_login_error"),
    # path("signup/", social_views.signup, name="socialaccount_signup"),
    # path("connections/", social_views.connections, name="socialaccount_connections"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "CheckMalts.views.page_not_found_view"


if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns