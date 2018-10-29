from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from .models import Caesar, Atbash, Alphanumeric, Viginere


def index(request):
    caesar = Caesar.objects.all()
    template = loader.get_template('ciphers/index.html')
    context = {
        'caesar': caesar,
    }
    return HttpResponse(template.render(context, request))

# def show(request, cipher_id):
#     cipher = get_object_or404(Question, pk=cipher_id)
#     return render(request, 'ciphers/show.html', {'cipher': cipher})
#
# def create(request, cipher_id):
#     return HttpResponse()
#
# def destroy(request, cipher_id):
#     return HttpResponse()
