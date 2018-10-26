from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ciphers index.")

def show(request, cipher_id):
    cipher = get_object_or404(Question, pk=cipher_id)
    return render(request, 'ciphers/show.html', {'cipher': cipher})
#
# def create(request, cipher_id):
#     return HttpResponse()
#
# def destroy(request, cipher_id):
#     return HttpResponse()
