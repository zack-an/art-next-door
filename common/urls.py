from django.urls import path
from .views import IndexView

urlpatterns = [
    path('common/', IndexView.as_view()),
]