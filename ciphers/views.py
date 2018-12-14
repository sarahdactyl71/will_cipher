from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .models import Caesar, Atbash, Alphanumeric, Vigenere, CaesarsForm


def index(request):
    caesars = Caesar.objects.all()
    atbashs = Atbash.objects.all()
    alphanumerics = Alphanumeric.objects.all()
    context = {'caesars': caesars, 'atbashs': atbashs, 'alphanumerics': alphanumerics}
    return render(request, 'ciphers/index.html', context)

def caesar_show(request, caesar_id):
    caesar = get_object_or_404(Caesar, pk=caesar_id)
    return render(request, 'ciphers/caesar_show.html', {'caesar': caesar})

def atbash_show(request, atbash_id):
    atbash = get_object_or_404(Atbash, pk=atbash_id)
    return render(request, 'ciphers/atbash_show.html', {'atbash': atbash})

def alphanumeric_show(request, alphanumeric_id):
    atbash = get_object_or_404(Alphanumeric, pk=alphanumeric_id)
    return render(request, 'ciphers/alphanumeric_show.html', {'alphanumeric': alphanumeric})

def create(request, template_name='ciphers/caesar_form.html'):
    form = CaesarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ciphers:index')
    return render(request, template_name, {'form': form})

def update(request, caesar_id, template_name='ciphers/caesar_form.html'):
    caesar = get_object_or_404(Caesar, pk=caesar_id)
    form = CaesarsForm(request.POST or None, instance=caesar)
    if form.is_valid():
        form.save()
        return redirect('ciphers:index')
    return render(request, template_name, {'form': form})

def delete(request, caesar_id, template_name='ciphers/caesar_delete.html'):
    caesar = get_object_or_404(Caesar, pk=caesar_id)
    if request.method=='POST':
        caesar.delete()
        return redirect('ciphers:index')
    return render(request, template_name, {'caesar': caesar})
