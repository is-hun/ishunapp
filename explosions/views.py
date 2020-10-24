from django.shortcuts import render
from django.http import HttpResponse
from explosions.models import Quarry

def index(request):
    all_quarries = Quarry.objects.all()

    allquarries_text = "<b>All quarries:</b> <br><br>"

    for quarry in all_quarries:
        allquarries_text += quarry.name + "<br>"

    return HttpResponse(allquarries_text)
