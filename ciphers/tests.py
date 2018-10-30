import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Caesar, Atbash, Alphanumeric, Viginere

class CaesarTestCase(TestCase):

    def can_decode_smaller_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text = 'OLHV')
        caesar_two = Caesar.objects.create(caesar_text = 'PBVWHUB VKDFN')
        caesar_three = Caesar.objects.create(caesar_text = 'SLWW')
        caesar_four = Caesar.objects.create(caesar_text = 'OAUVG')
        caesar_five = Caesar.objects.create(caesar_text = 'EWTUG AQW OCTKNAP')
        self.assertEqual(caesar_one.decode(offset), 'LIES')
        self.assertEqual(caesar_two.decode(offset), 'MYSTERY SHACK')
        self.assertEqual(caesar_three.decode(offset), 'PITT')
        self.assertEqual(caesar_four.decode(offset), 'MYSTE')
        self.assertEqual(caesar_five.decode(offset), 'CURSE YOU MARILYN')

    def test_can_decode_theme_song_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'VWDQ LV QRW ZKDW KH VHHPV')
        self.assertEqual(caesar.decode(offset), 'STAN IS NOT WHAT HE SEEMS')

    def test_can_decode_tourist_trapped(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'ZHOFRPH WR JUDYLWB IDOOV.')
        self.assertEqual(caesar.decode(offset), 'WELCOME TO GRAVITY FALLS.')

    def test_can_decode_the_legend_of_gobbleonker(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'QHAW ZHHN: UHWXUQ WR EXWW LVODQG.')
        self.assertEqual(caesar.decode(offset), 'NEXT WEEK: RETURN TO BUTT ISLAND.')

    def test_can_decode_headhunters_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = "KH'V VWLOO LQ WKH YHQWV.")
        self.assertEqual(caesar.decode(offset), "	HE'S STILL IN THE VENTS.")

    def test_can_decode_the_hand_that_rocks_the_mabel_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = "FDUOD, ZKB ZRQ'W BRX FDOO PH?")
        self.assertEqual(caesar.decode(offset), "	CARLA, WHY WON'T YOU CALL ME?")

    def test_can_decode_the_incoveniencing_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'RQZDUGV DRVKLPD!')
        self.assertEqual(caesar.decode(offset), 'ONWARDS AOSHIMA!')

    def test_can_decode_dipper_vs_manliness_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH.')
        self.assertEqual(caesar.decode(offset), 'MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE.')

    def test_can_decode_carpet_diem_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.')
        self.assertEqual(caesar.decode(offset), 'PUBERTY IS THE GREATEST MYSTERY OF ALL ALSO: GO OUTSIDE AND MAKE FRIENDS.')

    def test_can_decode_gideon_rises_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'ELOO LV ZDWFKLQJ')
        self.assertEqual(caesar.decode(offset), 'BILL IS WATCHING')

    def test_can_decode_shorts_ciphers(self):
        offset = 3
        caesar_one = Caesar.object.create(caesar_text = 'IURP WKH ILUVW XQWLO WKH ODVW VHDUFK WKH')
        caesar_two = Caesar.object.create(caesar_text = 'WKHP DOO ZHOFRPH WR JUDYLWB IDOOV')
        caesar_three = Caesar.object.create(caesar_text = 'FRGHV RI FUHGLWV SDVW RQH PHDQV RQH VR VHDUFK')
        self.assertEqual(caesar_one.decode(offset), 'FROM THE FIRST UNTIL THE LAST SEARCH THE')
        self.assertEqual(caesar_two.decode(offset), 'THEM ALL WELCOME TO GRAVITY FALLS')
        self.assertEqual(caesar_three.decode(offset), 'CODES OF CREDITS PAST ONE MEANS ONE SO SEARCH')

    def test_can_decode_scaryoke_cipehrs(self):
        offset = 3
        caesar_one = Caesar.object.create(caesar_text = 'TEV FP TBKAV PL MBOCBZQ')
        caesar_two = Caesar.object.create(caesar_text = 'ZDWFK RXW')
        caesar_three = Caesar.object.create(caesar_text = 'NLOO PH SOHDVH')
        self.assertEqual(caesar_one.decode(offset), 'WHY IS WENDY SO PERFECT')
        self.assertEqual(caesar_two.decode(offset), 'WATCH OUT')
        self.assertEqual(caesar_three.decode(offset), 'KILL ME PLEASE')

    def test_can_decode_scaryoke_cipehrs(self):
        offset = 3
        caesar_one = Caesar.object.create(caesar_text = 'ZLGGOH')
        caesar_two = Caesar.object.create(caesar_text = 'VKLIWHU')
        caesar_three = Caesar.object.create(caesar_text = 'ZKDWHYV')
        caesar_four = Caesar.object.create(caesar_text = 'EHDUR)
        self.assertEqual(caesar_one.decode(offset), 'WIDDLE')
        self.assertEqual(caesar_two.decode(offset), 'SHIFTER')
        self.assertEqual(caesar_three.decode(offset), 'WHATEVS')
        self.assertEqual(caesar_four.decode(offset), 'BEARO')

    def test_can_decode_soos_and_the_real_girl_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'VWDQ LV QRW ZKDW KH VHHPV')
        self.assertEqual(caesar.decode(offset), 'STAN IS NOT WHAT HE SEEMS')

    def test_can_decode_not_what_he_seems_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text = 'JXYDPHQW')
        self.assertEqual(caesar.decode(offset), 'GUVAMENT')
