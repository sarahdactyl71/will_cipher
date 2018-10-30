import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Caesar, Atbash, Alphanumeric, Viginere

class CaesarTestCase(TestCase):

    def test_can_decode_theme_song_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'VWDQ LV QRW ZKDW KH VHHPV')
        self.assertEqual(caesar.decode(), 'STAN IS NOT WHAT HE SEEMS')

    def test_can_decode_tourist_trapped(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'ZHOFRPH WR JUDYLWB IDOOV.')
        self.assertEqual(caesar.decode(), 'WELCOME TO GRAVITY FALLS.')

    def test_can_decode_the_legend_of_gobbleonker(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'QHAW ZHHN: UHWXUQ WR EXWW LVODQG.')
        self.assertEqual(caesar.decode(), 'NEXT WEEK: RETURN TO BUTT ISLAND.')
