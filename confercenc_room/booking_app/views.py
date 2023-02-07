from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .models import Room

class AddConferenceRoom(View):
    def get(self, request):
        return render(request, "add_room.html")
    def post(self, request):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity")
        projector = request.POST.get("projector")

        if projector == None:
            projector = False
        else:
            projector = True

        if str(name) is "" or int(capacity) <= 0:
            ctx = {"result" : "Data are incorrect"}
            return render(request, "add_room.html", ctx)
        else:
            try:
                room = Room.objects.create(name=name, capacity=capacity, projector=projector)
                return HttpResponseRedirect("/")
            except Exception as e:
                ctx = {"result" : "Room already exist"}
                return render(request, "add_room.html", ctx), e


class RoomsList(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, "room_list.html", {"rooms": rooms})



