from django.db import models
from django.forms import ModelForm
import re

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
backwards_alphabet = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

def rotate(list, offset):
    return list[offset:] + list[:offset]

class Caesar(models.Model):

    caesar_text = models.CharField(max_length=500)

    def __str__(self):
        return self.caesar_text

    def encode(self, offset):
        return self.new_message(-offset)

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


class CaesarsForm(ModelForm):
    class Meta:
        model = Caesar
        fields = ['caesar_text']

class Atbash(models.Model):

    atbash_text = models.CharField(max_length=500)

    def __str__(self):
        return self.atbash_text

    def decode(self):
        list = []
        for character in self.atbash_text:
            if character not in alphabet:
                list.append(character)
            else:
                character_index = backwards_alphabet.index(character)
                new_character = alphabet[character_index]
                list.append(new_character)
            message = ''.join(list)
        return message

    def encode(self):
        list = []
        for character in self.atbash_text:
            if character not in alphabet:
                list.append(character)
            else:
                character_index = alphabet.index(character)
                new_character = backwards_alphabet[character_index]
                list.append(new_character)
            message = ''.join(list)
        return message

class Alphanumeric(models.Model):

    alphanumeric_text = models.CharField(max_length=500)

    def __str__(self):
        return self.alphanumeric_text

    def decode(self):
        list = []
        character_split = re.split('(\W)', self.alphanumeric_text)
        import code; code.interact(local=dict(globals(), **locals()))
        for character in character_split:
            if character not in alphabet:
                list.append(character)
            else:
                print(character)



class Viginere(models.Model):

    viginere_text = models.CharField(max_length=500)

    def __str__(self):
        return self.viginere_text
