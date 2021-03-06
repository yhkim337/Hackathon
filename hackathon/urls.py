"""soldierletter URL Configuration

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
from django.urls import path
from django.conf.urls import include
import soldierLetter.views
import accounts.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', soldierLetter.views.index, name='index'),
    path('intro/', include('soldierLetter.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/subscribe/', accounts.views.subscribe, name='subscribe'),
    path('accounts/edit/', accounts.views.edit, name='edit'),
    path('accounts/signup/check/', accounts.views.check, name='check'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)