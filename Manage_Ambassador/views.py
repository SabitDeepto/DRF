from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from Manage_Ambassador.forms import AmbassadorForm


# Create your views here.
from Manage_Ambassador.models import CreateAmbassador


def create_ambassador(request):
    form = AmbassadorForm
    context = {'name': 'Ambassador', 'form': form}
    return render(request, 'forms_regular.html', context)


@require_POST
def ambassador_list(request):
    form = AmbassadorForm(request.POST)
    if form.is_valid():
        ambassador = CreateAmbassador(ambassador_name=request.POST['ambassador_name'],
                                      email=request.POST['email'],
                                      phone=request.POST['phone'])
        ambassador.save()
    return redirect('create_ambassador')


def amb_list(request):
    list = CreateAmbassador.objects.all()
    return render(request, 'tables_regular.html', {'list': list})