from django.shortcuts import render, redirect

from Manage_Ambassador.forms import AmbassadorForm
from Manage_Ambassador.models import CreateAmbassador


def ambassador_list(request):
    a_list = CreateAmbassador.objects.order_by('-id')
    return render(request, 'tables_regular.html', {'list': a_list})


def create_ambassador(request):
    form = AmbassadorForm(request.POST)
    if form.is_valid():
        ambassador = CreateAmbassador(ambassador_name=request.POST['ambassador_name'],
                                      phone=request.POST['phone'],
                                      email=request.POST['email'])

        ambassador.save()
        return redirect('ambassador_list')
    return render(request, 'forms_regular.html', {'form': form})


def delete_ambassador(request):
    CreateAmbassador.objects.all().delete()
    return redirect('ambassador_list')


