from django.shortcuts import redirect
from . import views

def homepage (request):
  return redirect('/movies/')
