from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from .models import Caesar, Atbash, Alphanumeric, Viginere


def index(request):
    caesars = Caesar.objects.all()
    context = {'caesars': caesars}
    return render(request, 'ciphers/index.html', context)

def show(request, caesar_id):
    caesar = get_object_or_404(Caesar, pk=caesar_id)
    return render(request, 'ciphers/show.html', {'caesar': caesar})
#
# def create(request, cipher_id):
#     return HttpResponse()
#
# def destroy(request, cipher_id):
#     return HttpResponse()
