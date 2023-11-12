from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Person

# Create your views here.
# def home(request):
#     return HttpResponse("ok")
#
# def person(request, person_id):
#     person = Person.objects.get(pk=person_id)
#     if person is not None:
#         return render(request,'people/person.html', {'person': person})
#     else:
#         raise Http404('Person does not exist')
def index(request):
    context = {'title': 'Homeet',}
    return render(request, 'profil/index.html', context)

def profil(request):
    context = {'title': 'Homeet - Profile'}
    return render(request, 'profil/profil.html', context)

def contactUs(request):
    if request.method == "POST":
        name = request.POST['name']
        # gender = request.POST['gender'] #here are names in ['...']
        # date_of_birth = request.POST['date_of_birth']
        # tg = request.POST['tg']
        # nom_tel = request.POST['nom_tel']
        # osebe = request.POST['osebe']

        if len(name) < 2:
            return redirect('home')
        else:
            save_data = Person(name=name)
            save_data.save()

            return redirect('profil')
    return render(request, "profil/index.html")

