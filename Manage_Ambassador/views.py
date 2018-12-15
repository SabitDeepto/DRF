from django.shortcuts import render


# Create your views here.
def create_ambassador(request):
    return render(request, 'forms_regular.html', {'name': 'ambassador'})



