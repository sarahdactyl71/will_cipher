from django.db import models
from django.forms import ModelForm
import re

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
backwards_alphabet = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
special_chars = ['.',':',' ',"'",'!','?','',',']

def alphabet_grid():
    offset = 0
    grid = []
    while offset < 26:
        row = rotate(alphabet, offset)
        grid.append(row)
        offset += 1
    return grid

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
        while '-' in character_split: character_split.remove('-')
        for character in character_split:
            if character in special_chars:
                list.append(character)
            else:
                character = int(character)
                letter = alphabet[character - 1]
                list.append(letter)
            message = ''.join(list)
        return message

    def encode(self):
        list = []
        for character in self.alphanumeric_text:
            if character not in alphabet:
                if list[-1] not in alphabet and list[-1] != '-':
                    list.append(character)
                else:
                    list.pop()
                    list.append(character)
            else:
                number = str(alphabet.index(character) + 1)
                list.append(number)
                list.append('-')
            message = ''.join(list)
        return message


class Vigenere(models.Model):

    vigenere_text = models.CharField(max_length=500)

    def __str__(self):
        return self.vigenere_text

    def keyword_length(self, keyword):
        list = []
        for character in self.vigenere_text:
            if character in alphabet:
                list.append(character)
            keyword_length = len(list)
        return keyword_length

    def repeat_keyword(self, keyword):
        length = self.keyword_length(keyword)
        while len(keyword) < length:
            keyword += keyword
        keyword = keyword[:length]
        return keyword

    def encode(self, keyword):
        list = []
        new_keyword = self.repeat_keyword(keyword)
        for character in self.vigenere_text:
            if character in special_chars:
                list.append(character)
            else:
                column_index = self.vigenere_text.index(character)
                character_index = alphabet.index(character)
                row = alphabet_grid()[character_index]
                column = row[column_index]
                list.append(column)
            message = ''.join(list)
        return message

    # def encode(self, keyword):
    #     new_keyword = self.repeat_keyword(keyword)
    #     for character in self.vigenere_text:
    #         list = []
    #         if character in special_chars:
    #             list.append(character)
    #         else:
    #             for keyword_letter in new_keyword:
    #                 column_index = alphabet.index(keyword_letter)
    #                 character_index = alphabet.index(character)
    #                 row = alphabet_grid()[character_index]
    #                 column = row[column_index]
    #                 list.append(column)
    #             message = ''.join(list)
    #         return message
    #         import code; code.interact(local=dict(globals(), **locals()))
