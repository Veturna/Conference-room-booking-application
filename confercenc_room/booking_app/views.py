from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Room, Booking
import datetime

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
                Room.objects.create(name=name, capacity=capacity, projector=projector)
                return HttpResponseRedirect("/")
            except Exception as e:
                ctx = {"result" : "Room already exist"}
                return render(request, "add_room.html", ctx), e


class RoomsList(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, "room_list.html", {"rooms": rooms})


class DeleteRoom(View):
    def get(self, request, id):
            to_delete = Room.objects.get(id=id)
            to_delete.delete()
            return HttpResponseRedirect("room-list")


class ModifyRoom(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, "modify_room.html", {"room":room})
    def post(self, request, id):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity")
        projector = request.POST.get("projector")

        if projector == None:
            projector = False
        else:
            projector = True

        if str(name) is "" or int(capacity) <= 0:
            ctx = {"result" : "Data are incorrect"}
            return render(request, "modify_room.html", ctx)
        else:
            try:
                room = Room.objects.get(id=id)
                room.name = name
                room.capacity = capacity
                room.projector = projector
                room.save()
                return HttpResponseRedirect("/")
            except Exception as e:
                ctx = {"result" : "Room already exist"}
                return render(request, "add_room.html", ctx), e

class ReservationView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, "reservation_view.html", {"room":room})
    def post(self, request, id):
        room = Room.objects.get(id=id)
        comment = request.POST.get("comment")
        date = request.POST.get("date")

        if Booking.objects.filter(room_id=room, date=date):
            return render(request, "reservation_view.html", {"result":"The room is already booking"})
        elif date < str(datetime.date.today()):
            return render(request, "reservation_view.html", {"result":"The date need to be at least today"})
        else:
            Booking.objects.create(room_id=room, date=date, comment=comment)
            return HttpResponseRedirect("/")


class RoomDetails(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, "reservation_view.html", {"room": room})






