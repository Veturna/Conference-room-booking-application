"""confercenc_room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from booking_app.views import AddConferenceRoom, RoomsList, DeleteRoom, ModifyRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddConferenceRoom.as_view(), name="add-room"),
    path('', RoomsList.as_view(), name="room-list"),
    re_path(r'^room/delete/(?P<id>\d+)/$', DeleteRoom.as_view(), name="delete-room"),
    re_path(r'^room/modify/(?P<id>\d+)/$', ModifyRoom.as_view(), name="modify-room")

]
