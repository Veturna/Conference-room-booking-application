from django.shortcuts import render
from django.views import View


class AddConferenceRoom(View):
    def get(self, request):
        return render(request, "add_room.html")
    def post(self, request):
        pass
