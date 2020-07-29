from django.http import HttpResponse
from django.shortcuts import render
from django_ilmoitin.utils import send_notification

from .models import Animal


def index(request):
    animal = Animal(name="Rox the Fox")
    context = {
        "animal": animal,
        "foo": "bar",
    }

    attachment = "test.txt", "foo bar", "text/plain"

    send_notification("foo@bar.com", "event_created", context, "en", [attachment])
    return HttpResponse("Hello, world. You're at the polls index.")
