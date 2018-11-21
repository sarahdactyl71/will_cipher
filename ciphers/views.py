from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Caesar, Atbash, Alphanumeric, Viginere, CaesarsForm

# from django.conf import settings
# from .utils import parse_json_for_data, get_user_creds


def index(request):
    caesars = Caesar.objects.all()
    context = {'caesars': caesars}
    return render(request, 'ciphers/index.html', context)

def show(request, caesar_id):
    caesar = get_object_or_404(Caesar, pk=caesar_id)
    return render(request, 'ciphers/show.html', {'caesar': caesar})

def create(request, template_name='contact_api/caesar_form.html'):
    form = CaesarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ciphers:index')
    return render(request, template_name, {'form': form})

# def destroy(request, cipher_id):
#     return HttpResponse()
