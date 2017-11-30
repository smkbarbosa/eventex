from django.shortcuts import render

# Create your views here.


def certificate(request):
    return render(request, 'certificate.html')