from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
# from djangouploads.models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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


# def index(request):
#     context = {'title': 'Homeet',}
#     return render(request, 'profil/index.html', context)
#
# def profil(request):
#     context = {'title': 'Homeet - Profile'}
#     return render(request, 'templates/profil.html', context)


# def upload(request):
#     return render(request,'people/upload.html')


# from django.http import HttpResponse
# from django.shortcuts import render
#
# def webpage1(request):
#     return render(request,'index.html')
#
# def webpage2(request):
#     return render(request,'profil.html')


from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'profil.html'
