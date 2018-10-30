from django.db import models

class Caesar(models.Model):
    caesar_text = models.CharField(max_length=500)

    def encode(self, offset):

    def decode(self, offset):


class Atbash(models.Model):
    atbash_test = models.CharField(max_length=500)

class Alphanumeric(models.Model):
    alphanumeric_text = models.CharField(max_length=500)

class Viginere(models.Model):
    viginere_text = models.CharField(max_length=500)
