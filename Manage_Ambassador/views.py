from django.shortcuts import render, redirect

from Manage_Ambassador.forms import AmbassadorForm
from Manage_Ambassador.models import CreateAmbassador


def ambassador_list(request):
    a_list = CreateAmbassador.objects.order_by('-id')
    return render(request, 'tables_regular.html', {'list': a_list})


def create_ambassador(request):
    form = AmbassadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ambassador_list')

    return render(request, 'forms_regular.html', {'form': form})


# def delete(request,id):


def delete_ambassador(request):
    CreateAmbassador.objects.all().delete()
    return redirect('ambassador_list')


def update(request, id):
    product = CreateAmbassador.objects.get(id=id)
    form = AmbassadorForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('ambassador_list')

    return render(request, 'forms_regular.html', {'form': form, 'product': product})


def delete(request,id):
    product = CreateAmbassador.objects.get(id=id)
    product.delete()
    return redirect('ambassador_list')