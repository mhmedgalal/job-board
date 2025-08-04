from django.shortcuts import render

# Create your views here.
def candidate(request):
    return render(request, 'candidate.html')


def employer(request):
    return render(request, 'employer.html')
