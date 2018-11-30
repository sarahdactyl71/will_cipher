from django.db import models
from django.forms import ModelForm
from django import template

register = template.Library()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def rotate(list, offset):
    return list[offset:] + list[:offset]

class Caesar(models.Model):

    caesar_text = models.CharField(max_length=500)

    def __str__(self):
        return self.caesar_text

    @register.filter
    def encode(self, offset):
        return self.new_message(-offset)

    @register.filter
    def decode(self, offset):
        return self.new_message(offset)

    def new_message(self, offset):
        list = []
        new_alphabet = rotate(alphabet, offset)
        for letter in self.caesar_text:
            if letter not in alphabet:
                list.append(letter)
            else:
                letter_index = new_alphabet.index(letter)
                new_letter = alphabet[letter_index]
                list.append(new_letter)
            message = ''.join(list)
        return message

        # import code; code.interact(local=dict(globals(), **locals()))

class CaesarsForm(ModelForm):
    class Meta:
        model = Caesar
        fields = ['caesar_text']

class Atbash(models.Model):
    atbash_text = models.CharField(max_length=500)

class Alphanumeric(models.Model):
    alphanumeric_text = models.CharField(max_length=500)

class Viginere(models.Model):
    viginere_text = models.CharField(max_length=500)
