from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {"variable": ": this is sent"}
    return render(request, "index.htm", context)
    # return HttpResponse("This is homepage")


def about(request):
    return HttpResponse("This is About Page")


def services(request):
    return HttpResponse("This is services Page")


def contact(request):
    return HttpResponse("This is contact Page")