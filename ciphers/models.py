from django.db import models

class Caesar(models.Model):
    caesar_text = models.CharField(max_length=500)
