from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
#from djangouploads.models import Person

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
