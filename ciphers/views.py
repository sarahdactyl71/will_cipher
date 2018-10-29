from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Caesar, Atbash, Alphanumeric, Viginere


def index(request):
    caesar = Caesar.objects.all()
    output = ', '.join([c.caesar_text for c in caesar])
    return HttpResponse(output)

# def show(request, cipher_id):
#     cipher = get_object_or404(Question, pk=cipher_id)
#     return render(request, 'ciphers/show.html', {'cipher': cipher})
#
# def create(request, cipher_id):
#     return HttpResponse()
#
# def destroy(request, cipher_id):
#     return HttpResponse()
