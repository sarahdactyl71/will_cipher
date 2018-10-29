from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from .models import Caesar, Atbash, Alphanumeric, Viginere


def index(request):
    caesar = Caesar.objects.all()
    context = {'caesar': caesar}
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
