from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Form
from django.urls import reverse

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')

def fill_form(request):
    a = Form(
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        idea = request.POST['idea'],
        #file = request.FILES['file'],
        )
    a.save()
    return render(request, 'common/index.html')