from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Form

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')

'''def fill_form(request):'''