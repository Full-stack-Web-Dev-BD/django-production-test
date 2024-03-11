from django.shortcuts import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("Hellow world !")