from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from .forms import EditorForm

# the index function is called when root is visited
def index(request):
    form = EditorForm()
    print(form)
    return render(request, "convertor/index.html", {'form': form})
