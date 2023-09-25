from django.shortcuts import render

# Create your views here.

def showmain(request):
    return render(request, "teamInfo/main.html")

def showach(request):
    return render(request, "teamInfo/achievements.html")

def showeduc(request):
    return render(request, "teamInfo/education.html")

def showhobby(request):
    return render(request, "teamInfo/hobby.html")

def showleisure(request):
    return render(request, "teamInfo/leisure.html")