from django.shortcuts import render

def list(request):
    return render(request, "list.html")

def add(request):
    return render(request, "add.html")