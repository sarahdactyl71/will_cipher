from django.db import models

class Caesar(models.Model):
    caesar_text = models.CharField(max_length=500)

class Atbash(models.Model):
    atbash_test = model.CharField(max_length=500)

class Alphanumeric(models.Model):
    alphanumeric_text = model.CharField(max_length=500)

class Viginere(model.Model):
    viginere_text = model.CharField(max_length=500)
    
