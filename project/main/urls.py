from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import adminhome, userhome, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', userhome, name='userhome'),
    path('adminhome/', adminhome, name='adminhome'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
