from django.shortcuts import render, HttpResponse, redirect
from .models import Notes
from .forms import NoteFrom


def index(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        try:
            note = Notes(title = title, description = description)
            note.save()
        except Exception as e:
            return HttpResponse("Some Error occord", e)
    formNote = NoteFrom()
    notes = Notes.objects.all()

    return render(request, "todoApp/index.html", {"notes": notes, "form": formNote})




def deleteNote(request, id):
    if request.method == "POST":
        note = Notes.objects.get(pk=id)
        note.delete()
        return redirect('/')
    return HttpResponse("Deletion Failed")