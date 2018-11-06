from django.db import models

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def rotate(list, offset):
    return list[offset:] + list[:offset]

class Caesar(models.Model):

    caesar_text = models.CharField(max_length=500)

    # def encode(self, offset):

    def decode(self, offset):
        list = []
        new_alphabet = rotate(alphabet, offset)
        for letter in self.caesar_text:
            import code; code.interact(local=dict(globals(), **locals()))
            new_letter = new_alphabet[alphabet[letter]]
            list.append(new_letter)
        return list


class Atbash(models.Model):
    atbash_text = models.CharField(max_length=500)

class Alphanumeric(models.Model):
    alphanumeric_text = models.CharField(max_length=500)

class Viginere(models.Model):
    viginere_text = models.CharField(max_length=500)
