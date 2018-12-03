import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Caesar, Atbash, Alphanumeric, Viginere

class CaesarTestCase(TestCase):

    #decoding ciphers

    def can_decode_smaller_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='OLHV')
        caesar_two = Caesar.objects.create(caesar_text ='PBVWHUB VKDFN')
        caesar_three = Caesar.objects.create(caesar_text ='SLWW')
        caesar_four = Caesar.objects.create(caesar_text ='OAUVG')
        caesar_five = Caesar.objects.create(caesar_text ='EWTUG AQW OCTKNAP')
        self.assertEqual(caesar_one.decode(offset), 'LIES')
        self.assertEqual(caesar_two.decode(offset), 'MYSTERY SHACK')
        self.assertEqual(caesar_three.decode(offset), 'PITT')
        self.assertEqual(caesar_four.decode(offset), 'MYSTE')
        self.assertEqual(caesar_five.decode(offset), 'CURSE YOU MARILYN')

    def test_can_decode_theme_song_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='VWDQ LV QRW ZKDW KH VHHPV')
        self.assertEqual(caesar.decode(offset), 'STAN IS NOT WHAT HE SEEMS')

    def test_can_decode_tourist_trapped(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='ZHOFRPH WR JUDYLWB IDOOV.')
        self.assertEqual(caesar.decode(offset), 'WELCOME TO GRAVITY FALLS.')

    def test_can_decode_the_legend_of_gobbleonker(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='QHAW ZHHN: UHWXUQ WR EXWW LVODQG.')
        self.assertEqual(caesar.decode(offset), 'NEXT WEEK: RETURN TO BUTT ISLAND.')

    def test_can_decode_headhunters_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ="KH'V VWLOO LQ WKH YHQWV.")
        self.assertEqual(caesar.decode(offset), "HE'S STILL IN THE VENTS.")

    def test_can_decode_the_hand_that_rocks_the_mabel_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ="FDUOD, ZKB ZRQ'W BRX FDOO PH?")
        self.assertEqual(caesar.decode(offset), "CARLA, WHY WON'T YOU CALL ME?")

    def test_can_decode_the_incoveniencing_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='RQZDUGV DRVKLPD!')
        self.assertEqual(caesar.decode(offset), 'ONWARDS AOSHIMA!')

    def test_can_decode_dipper_vs_manliness_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH.')
        self.assertEqual(caesar.decode(offset), 'MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE.')

    def test_can_decode_carpet_diem_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.')
        self.assertEqual(caesar.decode(offset), 'PUBERTY IS THE GREATEST MYSTERY OF ALL ALSO: GO OUTSIDE AND MAKE FRIENDS.')

    def test_can_decode_gideon_rises_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='ELOO LV ZDWFKLQJ')
        self.assertEqual(caesar.decode(offset), 'BILL IS WATCHING')

    def test_can_decode_shorts_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='IURP WKH ILUVW XQWLO WKH ODVW VHDUFK WKH')
        caesar_two = Caesar.objects.create(caesar_text ='WKHP DOO ZHOFRPH WR JUDYLWB IDOOV')
        caesar_three = Caesar.objects.create(caesar_text ='FRGHV RI FUHGLWV SDVW RQH PHDQV RQH VR VHDUFK')
        self.assertEqual(caesar_one.decode(offset), 'FROM THE FIRST UNTIL THE LAST SEARCH THE')
        self.assertEqual(caesar_two.decode(offset), 'THEM ALL WELCOME TO GRAVITY FALLS')
        self.assertEqual(caesar_three.decode(offset), 'CODES OF CREDITS PAST ONE MEANS ONE SO SEARCH')

    def test_can_decode_scaryoke_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='TEV FP TBKAV PL MBOCBZQ')
        caesar_two = Caesar.objects.create(caesar_text ='ZDWFK RXW')
        caesar_three = Caesar.objects.create(caesar_text ='NLOO PH SOHDVH')
        self.assertEqual(caesar_one.decode(offset), 'WHY IS WENDY SO PERFECT')
        self.assertEqual(caesar_two.decode(offset), 'WATCH OUT')
        self.assertEqual(caesar_three.decode(offset), 'KILL ME PLEASE')

    def test_can_decode_scaryoke_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='ZLGGOH')
        caesar_two = Caesar.objects.create(caesar_text ='VKLIWHU')
        caesar_three = Caesar.objects.create(caesar_text ='ZKDWHYV')
        caesar_four = Caesar.objects.create(caesar_text ='EHDUR')
        self.assertEqual(caesar_one.decode(offset), 'WIDDLE')
        self.assertEqual(caesar_two.decode(offset), 'SHIFTER')
        self.assertEqual(caesar_three.decode(offset), 'WHATEVS')
        self.assertEqual(caesar_four.decode(offset), 'BEARO')


    def test_can_decode_soos_and_the_real_girl_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='VWDQ LV QRW ZKDW KH VHHPV')
        self.assertEqual(caesar.decode(offset), 'STAN IS NOT WHAT HE SEEMS')

    def test_can_decode_not_what_he_seems_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='JXYDPHQW')
        self.assertEqual(caesar.decode(offset), 'GUVAMENT')

    #encoding ciphers

    def test_can_encode_scaryoke_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='WIDDLE')
        caesar_two = Caesar.objects.create(caesar_text ='SHIFTER')
        caesar_three = Caesar.objects.create(caesar_text ='WHATEVS')
        caesar_four = Caesar.objects.create(caesar_text ='BEARO')
        self.assertEqual(caesar_one.encode(offset), 'ZLGGOH')
        self.assertEqual(caesar_two.encode(offset), 'VKLIWHU')
        self.assertEqual(caesar_three.encode(offset), 'ZKDWHYV')
        self.assertEqual(caesar_four.encode(offset), 'EHDUR')

    def test_can_encode_soos_and_the_real_girl_cipher(self):
        offset = 3
        caesar = Caesar.objects.create(caesar_text ='STAN IS NOT WHAT HE SEEMS')
        self.assertEqual(caesar.encode(offset), 'VWDQ LV QRW ZKDW KH VHHPV')

    def test_can_encode_shorts_ciphers(self):
        offset = 3
        caesar_one = Caesar.objects.create(caesar_text ='FROM THE FIRST UNTIL THE LAST SEARCH THE')
        caesar_two = Caesar.objects.create(caesar_text ='THEM ALL WELCOME TO GRAVITY FALLS')
        caesar_three = Caesar.objects.create(caesar_text ='CODES OF CREDITS PAST ONE MEANS ONE SO SEARCH')
        self.assertEqual(caesar_one.encode(offset), 'IURP WKH ILUVW XQWLO WKH ODVW VHDUFK WKH')
        self.assertEqual(caesar_two.encode(offset), 'WKHP DOO ZHOFRPH WR JUDYLWB IDOOV')
        self.assertEqual(caesar_three.encode(offset), 'FRGHV RI FUHGLWV SDVW RQH PHDQV RQH VR VHDUFK')

#TESTING FOR THE ATBASH CIPHER

class AtbashTestCase(TestCase):

    def test_decodes_double_dipper(self):
        atbash = Atbash.objects.create(atbash_text = 'KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"')
        self.assertEqual(atbash.decode(), 'PAPER JAM DIPPER SAYS: "AUUGHWXQHGADSADUH!"')

    def test_can_decode_irrational_treasure(self):
        atbash = Atbash.objects.create(atbash_text = 'V. KOFIRYFH GIVNYOVB.')
        self.assertEqual(atbash.decode(), 'E. PLURIBUS TREMBLEY.')

    def test_can_decode_the_time_travelers_pig(self):
        atbash = Atbash.objects.create(atbash_text = 'MLG S.T. DVOOH ZKKILEVW.')
        self.assertEqual(atbash.decode(), 'NOT H.G. WELLS APPROVED.')

    def test_can_decode_fight_fighters(self):
        atbash = Atbash.objects.create(atbash_text = 'HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.')
        self.assertEqual(atbash.decode(), 'SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE.')

    def test_can_decode_little_dipper(self):
        atbash = Atbash.objects.create(atbash_text = 'GSV RMERHRYOV DRAZIW RH DZGXSRMT.')
        self.assertEqual(atbash.decode(), 'THE INVISIBLE WIZARD IS WATCHING.')

    def test_can_decode_summerween(self):
        atbash = Atbash.objects.create(atbash_text = 'YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB.')
        self.assertEqual(atbash.decode(), 'BROUGHT TO YOU BY HOMEWORK: THE CANDY.')

    def test_can_decode_boss_mabel(self):
        atbash = Atbash.objects.create(atbash_text = 'SVZEB RH GSV SVZW GSZG DVZIH GSV UVA.')
        self.assertEqual(atbash.decode(), 'HEAVY IS THE HEAD THAT WEARS THE FEZ.')

    def test_can_decode_sock_opera(self):
        atbash_one = Atbash.objects.create(atbash_text = 'KFIV VMVITB, MLG HPRM ZMW YLMV')
        atbash_two = Atbash.objects.create(atbash_text = 'IRHRMT ORPV GSV HSVKZIW GLMV')
        self.assertEqual(atbash_one.decode(), 'PURE ENERGY, NOT SKIN AND BONE')
        self.assertEqual(atbash_two.decode(), 'RISING LIKE THE SHEPARD TONE')

    def test_can_decode_society_of_the_blind_eye(self):
        atbash = Atbash.objects.create(atbash_text = 'YROO XRKSVI! GIRZMTOV!')
        self.assertEqual(atbash.decode(), 'BILL CIPHER! TRIANGLE!')

    def test_can_decode_a_tale_of_two_stans(self):
        atbash = Atbash.objects.create(atbash_text = 'YROO XRKSVI GIRZMTOV')
        self.assertEqual(atbash.decode(), 'BILL CIPHER TRIANGLE')

    def test_can_encode_double_dipper(self):
        atbash = Atbash.objects.create(atbash_text = 'PAPER JAM DIPPER SAYS: "AUUGHWXQHGADSADUH!"')
        self.assertEqual(atbash.encode(), 'KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"')

    def test_can_encode_irrational_treasure(self):
        atbash = Atbash.objects.create(atbash_text = 'E. PLURIBUS TREMBLEY.')
        self.assertEqual(atbash.encode(), 'V. KOFIRYFH GIVNYOVB.')

    def test_can_encode_the_time_travelers_pig(self):
        atbash = Atbash.objects.create(atbash_text = 'NOT H.G. WELLS APPROVED.')
        self.assertEqual(atbash.encode(), 'MLG S.T. DVOOH ZKKILEVW.')

    def test_can_encode_fight_fighters(self):
        atbash = Atbash.objects.create(atbash_text = 'SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE.')
        self.assertEqual(atbash.encode(), 'HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.')

#Testing for A1Z26(Alphanumeric) Cipher

class AlphanumericTestCase(TestCase):

    def test_can_decode_bottomless_pit(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = "14-5-24-20 21-16: 6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19 7-18-5-22-5-14-7-5.")
        self.assertEqual(alpha.decode(), "NEXT UP: FOOTBOT TWO: GRUNKLE'S GREVENGE.")

    def test_can_decode_the_deep_end(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = '22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.')
        self.assertEqual(alpha.decode(), 'VIVAN LOS PATOS DE LA PISCINA.')

    def test_can_decode_carpet_diem(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = '2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19?')
        self.assertEqual(alpha.decode(), 'BUT WHO STOLE THE CAPERS?')

    def test_can_decode_boyz_crazy(self):
        alpha = Alphanumeric.object.create(alphanumeric_text = '8-1-16-16-25 14-15-23, 1-18-9-5-12?')
        self.assertEqual(alpha.decode(), 'HAPPY NOW, ARIEL?')

    def test_land_before_swine(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = '9-20 23-15-18-11-19 6-15-18 16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19!')
        self.assertEqual(alpha.decode(), 'IT WORKS FOR PIIIIIIIIIIIIIIIIIGS!')

    def test_can_decode_dreamscapers(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = '20-15 2-5 3-15-14-20-9-14-21-5-4...')
        self.assertEqual(alpha.decode(), 'TO BE CONTINUED...')

    def test_can_decode_gideon_rises(self):
        alpha_one = Alphanumeric.objects.create(alphanumeric_text = '18-5-22-5-18-19-5 20-8-5 3-9-16-8-5-18-19')
        self.assertEqual(alpha_one.decode(), 'REVERSE THE CIPHERS')
