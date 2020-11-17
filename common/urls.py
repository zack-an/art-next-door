from django.urls import path
from .views import IndexView, fill_form
from . import views

app_name = 'common'
urlpatterns = [
    path('common/', IndexView.as_view(), name = 'IndexView'),
    path('common/fill_form', views.fill_form, name = 'fill_form'),
]