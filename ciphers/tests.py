import datetime

from django.test import TestCase
from django.utils import timezone
from unittest import skip

from .models import Caesar, Atbash, Alphanumeric, Vigenere

class CaesarTestCase(TestCase):

    #decoding Caesar ciphers

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

    #encoding Caesar ciphers

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

        #Encoding atbash ciphers

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

    #decoding alphanumeric cipher

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
        alpha = Alphanumeric.objects.create(alphanumeric_text = '8-1-16-16-25 14-15-23, 1-18-9-5-12?')
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

    #encoding alphanumeric cipher

    def test_can_encode_bottomless_pit(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = "NEXT UP: FOOTBOT TWO: GRUNKLE'S GREVENGE.")
        self.assertEqual(alpha.encode(), "14-5-24-20 21-16: 6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19 7-18-5-22-5-14-7-5.")

    def test_can_encode_the_deep_end(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = 'VIVAN LOS PATOS DE LA PISCINA.')
        self.assertEqual(alpha.encode(), '22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.')

    def test_can_encode_carpet_diem(self):
        alpha = Alphanumeric.objects.create(alphanumeric_text = 'BUT WHO STOLE THE CAPERS?')
        self.assertEqual(alpha.encode(), '2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19?')

# TESTING FOR VIGENERE CIPHER

class VigenereTestCase(TestCase):

    #ENCODING TESTS

    def test_can_encode_simple_case(self):
        keyword = 'GRAVITY'
        vigenere = Vigenere.objects.create(vigenere_text = 'MABELEATSSPRINKLES')
        self.assertEqual(vigenere.encode(keyword), 'SRBZTXYZJSKZBLQCEN')

    def test_can_encode_scaryoke_cipher(self):
        keyword = 'WIDDLE'
        vigenere = Vigenere.objects.create(vigenere_text = 'WELCOME BACK')
        self.assertEqual(vigenere.encode(keyword), 'SMOFZQA JDFV')

    def test_can_encode_into_the_bunker(self):
        keyword = 'SHIFTER'
        vigenere = Vigenere.objects.create(vigenere_text = 'WHAT KIND OF DISASTER INDEED')
        self.assertEqual(vigenere.encode(keyword), 'OOIY DMEV VN IBWRKAMW BRUWLL')

    def test_can_encode_the_golf_war(self):
        keyword = 'WHATEVS'
        vigenere = Vigenere.objects.create(vigenere_text = 'REMEMBER BIG HENRY')
        self.assertEqual(vigenere.encode(keyword), 'NLMXQWWN IIZ LZFNF')

    def test_can_encode_sock_opera(self):
        keyword = 'CIPHER'
        vigenere = Vigenere.objects.create(vigenere_text = 'WE’VE ALL HAD SOME FUN TONIGHT, BUT LET’S NOT FORGET WHO THE REAL "PUPPET MASTERS" ARE: REPTOIDS WHO HAVE INFILTRATED OUR GOVERNMENT')
        self.assertEqual(vigenere.encode(keyword), 'YM’KL ECN PPK WFOM UBR KQVXNLK, DCI SIK’U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH" HVV: TMEASZFA LOS YCDT PRWKTIYEKGL DBV XQDTYRDGVI')

    def test_can_encode_soos_and_the_real_girl(self):
        keyword = 'BEARO'
        vigenere = Vigenere.objects.create(vigenere_text = 'ANTHYDING CAN HADPLEN')
        self.assertEqual(vigenere.encode(keyword), 'BRTYMEMNX QBR HRRQPEE')

    def test_can_encode_little_gift_shop_of_horrors(self):
        keyword = 'NONCANON'
        vigenere = Vigenere.objects.create(vigenere_text = 'CHECK OUT DR. WADDLES’ LATEST BOOK: "A BRIEF HISTORY OF OINK OINK OINK OINK OINK"')
        self.assertEqual(vigenere.encode(keyword), 'PVREK BIG QF. JCDQZRF’ ZNVEFH OBCX: "C BEWRS VVUTBFL BT BKNX CVAY BKNX CVAY BKNX"')

    def test_can_encode_society_of_the_blind_eye(self):
        keyword = 'ERASE'
        vigenere = Vigenere.objects.create(vigenere_text = 'IGNORANCE IS BLISS. BUT BLISS IS BORING.')
        self.assertEqual(vigenere.encode(keyword), 'MXNGVEECW MW SLAWW. SUL FPZSK MW SOJMRX.')

    def test_can_encode_blendins_game(self):
        keyword = 'CAPACITOR'
        vigenere = Vigenere.objects.create(vigenere_text = "DON'T DO THE TIME CRIME IF YOU CAN'T DO THE TIME TIME.")
        self.assertEqual(vigenere.encode(keyword), "FOC'T FW MVV VIBE EZBAV KF NOW KTB'K FO IHG BBAV VIBE.")

    def test_can_encode_the_love_god(self):
        keyword = 'GOATANDAPIG'
        vigenere = Vigenere.objects.create(vigenere_text = 'I EAT KIDS.')
        self.assertEqual(vigenere.encode(keyword), 'O SAM KVGS.')

    def test_can_encode_northwest_mansion_mystery(self):
        keyword = 'CURSED'
        vigenere = Vigenere.objects.create(vigenere_text = 'NEXT UP ON UTBAHC: DID ALIENS WRITE THE CONSTITUTION? CRAWDADS IN TIARAS! AND FLORIDA: THE SHOW.')
        self.assertEqual(vigenere.encode(keyword), 'PYOL YS QH LLFDJW: UAH DNCVFW ZTCKW XKG WFFWWKNLLMRP? WISAGCXJ AR WKUISW! DPX WDSUKXR: LLH UBFO.')

    def test_can_encode_not_what_he_seems(self):
        keyword = 'STNLYMBL'
        vigenere = Vigenere.objects.create(vigenere_text = 'THE ORIGINAL MYSTERY TWINS')
        self.assertEqual(vigenere.encode(keyword), 'LAR ZPUHTFTY XWEUPJR GHGZT')

    def test_can_encode_a_tale_of_two_stans(self):
        keyword = 'SIXER'
        vigenere = Vigenere.objects.create(vigenere_text = 'BACKUPSMORE UNIVERSITY: YOU TRIED')
        self.assertEqual(vigenere.encode(keyword), 'TIZOLHAJSIW CKMMWZPMKQ: GLY KJQBH')

    def test_can_encode_dungeons_dungeons_and_more_dungeons(self):
        keyword = 'RADMASTER'
        vigenere = Vigenere.objects.create(vigenere_text = 'EXCELSI-WHATEVER!')
        self.assertEqual(vigenere.encode(keyword), 'VXFQLKB-AYRTHHEJ!')

    def test_can_encode_stanchurian_candidate(self):
        keyword = 'WORKINIT'
        vigenere = Vigenere.objects.create(vigenere_text = "GIIIIIIIIIIIIIIIIIIIIIITTTTT 'EM!")
        self.assertEqual(vigenere.encode(keyword), "CWZSQVQBEWZSQVQBEWZSQVQMPHKD 'MZ!")

    def test_can_encode_the_last_mabelcorn(self):
        keyword = 'SCHMENDRICK'
        vigenere = Vigenere.objects.create(vigenere_text = 'A SIMPLE MAN WITH EAGER EARS MAY TRUST THE WHISPERS THAT HE HEARS')
        self.assertEqual(vigenere.encode(keyword), 'S UPYTYH DIP GAVO QETHI MCBK OHK XEXJB VRW YOUWCHIA VRSV OQ LRDIA')

    def test_can_encode_roadside_attraction(self):
        keyword = 'DOPPER'
        vigenere = Vigenere.objects.create(vigenere_text = 'SOOS, LIKE A NOBLE GOLDEN RETRIEVER, EVENTUALLY FOUND HIS WAY HOMEWARD, AND BEFRIENDED A TALKING BULLDOG AND SASSY CAT ALONG THE WAY')
        self.assertEqual(vigenere.encode(keyword), 'VCDH, PZNS P CSSOS VDPUHB GTXILSKTV, VYSCIYROZN USLQR WXW NDM WDQVZOGS, EEG PTUVZHBSTH R WOAZMEJ PJAPURU PCH JDGHN GRW OADRX WVT LEP')

    def test_can_encode_dipper_and_mabel_vs_the_future(self):
        keyword = 'BLUEBOOK'
        vigenere =  Vigenere.objects.create(vigenere_text = 'DID YOU MISS ME?')
        self.assertEqual(vigenere.encode(keyword), 'ETX CPI ASTD GI?')

    def test_can_encode_weridmaggedon_part_one(self):
        keyword= 'CILLBIPHER'
        vigenere = Vigenere.objects.create(vigenere_text = "IT WILL TAKE 1,000 YEARS FOR TIME BABY'S MOLECULES TO RECONSTITUTE, AND WHEN HE'S BACK, HE'S GOING TO BE VERY CRANKY.")
        self.assertEqual(vigenere.encode(keyword), "KB HTMT IHOV 1,000 AMLCT NDY XZOM MLCG'H TSCGKFWFA IV VVEWYDUQIBXV, CVO HIMC OI'J DINV, IM'H NSZPO EZ CM KLVP EZLYLG.")

    def test_can_encode_weirdmaggedon_two_escape_from_reality(self):
        keyword = 'DIPPYFRESH'
        vigenere = Vigenere.objects.create(vigenere_text = "CRAZ AND XYLER WENT ON TO RUN THE LEGAL DEPARTMENT AT A MAJOR CHILDREN'S TELEVISION NETWORK")
        self.assertEqual(vigenere.encode(keyword), "FZPO YSU BQSHZ LTLY FR LV UCC IFJ CIYHO LTEYWKQWUW II P KFASJ JKQASPJE'W LLOMKXQNFR FLWEDGI")

    def test_can_encode_weridmaggedon_part_three_take_back_the_falls(self):
        keyword = 'SHACKTRON'
        vigenere = Vigenere.objects.create(vigenere_text = 'SOOS LATER FORCED MCGUCKET TO WATCH ALL 900 HOURS OF NEON CRISIS MECHABOT BOY: REVELATIONS')
        self.assertEqual(vigenere.encode(keyword), 'KVOU VTKSE XVREOW DQTMJKGD MF KNLJH CVE 900 YCHJZ OH XXFB PJPSKC FVQUSIOV LHP: FRNLLCDBFBF')

    @skip(reason="not sure if I am going to program this kind of implementation with the keyword")
    def test_can_encode_weridmaggedon_part_four_somewhere_in_the_woods(self):
        keyword_one = 'HIDDEN DEEP WITHIN THE WOODS A BURIED TREASURE WAITS'
        keyword_two = 'AXOLOTL'
        vigenere_one = Vigenere.objects.create(vigenere_text = 'SECRETS LOST AND STATUES FOUND BEYOND THE RUSTY GATES')
        vigenere_two = Vigenere.objects.create(vigenere_text = 'GOODBYE GRAVITY FALLS')
        self.assertEqual(vigenere_one.encode(keyword_one), 'ZMFUIGV PSHP IGK AGTAYAG TRMNE VVGSQW KLE JOJXU GIMWZ')
        self.assertEqual(vigenere_two.encode(keyword_two), 'GLCOPRP GOOGWMJ FXZWG')

    #BEGIN DECODING TESTS

    def test_can_decode_scaryoke_ciphers(self):
        keyword = 'WIDDLE'
        vigenere = Vigenere.objects.create(vigenere_text = 'SMOFZQA JDFV')
        self.assertEqual(vigenere.decode(keyword), 'WELCOME BACK')

    def test_can_decode_into_the_bunker(self):
        keyword = 'SHIFTER'
        vigenere = Vigenere.objects.create(vigenere_text = 'OOIY DMEV VN IBWRKAMW BRUWLL')
        self.assertEqual(vigenere.decode(keyword), 'WHAT KIND OF DISASTER INDEED')

    def test_can_decode_the_golf_war(self):
        keyword = 'WHATEVS'
        vigenere = Vigenere.objects.create(vigenere_text = 'NLMXQWWN IIZ LZFNF')
        self.assertEqual(vigenere.decode(keyword), 'REMEMBER BIG HENRY')

    def test_can_decode_sock_opera(self):
        keyword = 'CIPHER'
        vigenere = Vigenere.objects.create(vigenere_text = 'YM’KL ECN PPK WFOM UBR KQVXNLK, DCI SIK’U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH" HVV: TMEASZFA LOS YCDT PRWKTIYEKGL DBV XQDTYRDGVI')
        self.assertEqual(vigenere.decode(keyword), 'WE’VE ALL HAD SOME FUN TONIGHT, BUT LET’S NOT FORGET WHO THE REAL "PUPPET MASTERS" ARE: REPTOIDS WHO HAVE INFILTRATED OUR GOVERNMENT')

    def test_can_decode_soos_and_the_real_girl(self):
        keyword = 'BEARO'
        vigenere = Vigenere.objects.create(vigenere_text = 'BRTYMEMNX QBR HRRQPEE')
        self.assertEqual(vigenere.decode(keyword), 'ANTHYDING CAN HADPLEN')

    def test_can_decode_little_gift_shop_of_horrors(self):
        keyword = 'NONCANON'
        vigenere = Vigenere.objects.create(vigenere_text = 'PVREK BIG QF. JCDQZRF’ ZNVEFH OBCX: "C BEWRS VVUTBFL BT BKNX CVAY BKNX CVAY BKNX"')
        self.assertEqual(vigenere.decode(keyword), 'CHECK OUT DR. WADDLES’ LATEST BOOK: "A BRIEF HISTORY OF OINK OINK OINK OINK OINK"')

    def test_can_decode_society_of_the_blind_eye(self):
        keyword = 'ERASE'
        vigenere = Vigenere.objects.create(vigenere_text = 'MXNGVEECW MW SLAWW. SUL FPZSK MW SOJMRX.')
        self.assertEqual(vigenere.decode(keyword), 'IGNORANCE IS BLISS. BUT BLISS IS BORING.')

    def test_can_decode_blendins_game(self):
        keyword = 'CAPACITOR'
        vigenere = Vigenere.objects.create(vigenere_text = "FOC'T FW MVV VIBE EZBAV KF NOW KTB'K FO IHG BBAV VIBE.")
        self.assertEqual(vigenere.decode(keyword), "DON'T DO THE TIME CRIME IF YOU CAN'T DO THE TIME TIME.")

    def test_can_decode_the_love_god(self):
        keyword = 'GOATANDAPIG'
        vigenere = Vigenere.objects.create(vigenere_text = 'O SAM KVGS.')
        self.assertEqual(vigenere.decode(keyword), 'I EAT KIDS.')

    def test_can_decode_northwest_mansion_mystery(self):
        keyword = 'CURSED'
        vigenere = Vigenere.objects.create(vigenere_text = 'PYOL YS QH LLFDJW: UAH DNCVFW ZTCKW XKG WFFWWKNLLMRP? WISAGCXJ AR WKUISW! DPX WDSUKXR: LLH UBFO.')
        self.assertEqual(vigenere.decode(keyword), 'NEXT UP ON UTBAHC: DID ALIENS WRITE THE CONSTITUTION? CRAWDADS IN TIARAS! AND FLORIDA: THE SHOW.')

    def test_can_decode_not_what_he_seems(self):
        keyword = 'STNLYMBL'
        vigenere = Vigenere.objects.create(vigenere_text = 'LAR ZPUHTFTY XWEUPJR GHGZT')
        self.assertEqual(vigenere.decode(keyword), 'THE ORIGINAL MYSTERY TWINS')

    def test_can_decode_a_tale_of_two_stans(self):
        keyword = 'SIXER'
        vigenere = Vigenere.objects.create(vigenere_text = 'TIZOLHAJSIW CKMMWZPMKQ: GLY KJQBH')
        self.assertEqual(vigenere.decode(keyword), 'BACKUPSMORE UNIVERSITY: YOU TRIED')

    def test_can_decode_dungeons_dungeons_and_more_dungeons(self):
        keyword = 'RADMASTER'
        vigenere = Vigenere.objects.create(vigenere_text = 'VXFQLKB-AYRTHHEJ!')
        self.assertEqual(vigenere.decode(keyword), 'EXCELSI-WHATEVER!')

    def test_can_decode_stanchurian_candidate(self):
        keyword = 'WORKINIT'
        vigenere = Vigenere.objects.create(vigenere_text = "CWZSQVQBEWZSQVQBEWZSQVQMPHKD 'MZ!")
        self.assertEqual(vigenere.decode(keyword), "GIIIIIIIIIIIIIIIIIIIIIITTTTT 'EM!")

    def test_can_decode_the_last_mabelcorn(self):
        keyword = 'SCHMENDRICK'
        vigenere = Vigenere.objects.create(vigenere_text = 'S UPYTYH DIP GAVO QETHI MCBK OHK XEXJB VRW YOUWCHIA VRSV OQ LRDIA')
        self.assertEqual(vigenere.decode(keyword), 'A SIMPLE MAN WITH EAGER EARS MAY TRUST THE WHISPERS THAT HE HEARS')

    def test_can_decode_roadside_attraction(self):
        keyword = 'DOPPER'
        vigenere = Vigenere.objects.create(vigenere_text = 'VCDH, PZNS P CSSOS VDPUHB GTXILSKTV, VYSCIYROZN USLQR WXW NDM WDQVZOGS, EEG PTUVZHBSTH R WOAZMEJ PJAPURU PCH JDGHN GRW OADRX WVT LEP')
        self.assertEqual(vigenere.decode(keyword), 'SOOS, LIKE A NOBLE GOLDEN RETRIEVER, EVENTUALLY FOUND HIS WAY HOMEWARD, AND BEFRIENDED A TALKING BULLDOG AND SASSY CAT ALONG THE WAY')

    def test_can_decode_dipper_and_mabel_vs_the_future(self):
        keyword = 'BLUEBOOK'
        vigenere =  Vigenere.objects.create(vigenere_text = 'ETX CPI ASTD GI?')
        self.assertEqual(vigenere.decode(keyword), 'DID YOU MISS ME?')

    def test_can_decode_weridmaggedon_part_one(self):
        keyword= 'CILLBIPHER'
        vigenere = Vigenere.objects.create(vigenere_text = "KB HTMT IHOV 1,000 AMLCT NDY XZOM MLCG'H TSCGKFWFA IV VVEWYDUQIBXV, CVO HIMC OI'J DINV, IM'H NSZPO EZ CM KLVP EZLYLG.")
        self.assertEqual(vigenere.decode(keyword), "IT WILL TAKE 1,000 YEARS FOR TIME BABY'S MOLECULES TO RECONSTITUTE, AND WHEN HE'S BACK, HE'S GOING TO BE VERY CRANKY.")

    def test_can_decode_weirdmaggedon_two_escape_from_reality(self):
        keyword = 'DIPPYFRESH'
        vigenere = Vigenere.objects.create(vigenere_text = "FZPO YSU BQSHZ LTLY FR LV UCC IFJ CIYHO LTEYWKQWUW II P KFASJ JKQASPJE'W LLOMKXQNFR FLWEDGI")
        self.assertEqual(vigenere.decode(keyword), "CRAZ AND XYLER WENT ON TO RUN THE LEGAL DEPARTMENT AT A MAJOR CHILDREN'S TELEVISION NETWORK")

    def test_can_decode_weridmaggedon_part_three_take_back_the_falls(self):
        keyword = 'SHACKTRON'
        vigenere = Vigenere.objects.create(vigenere_text = 'KVOU VTKSE XVREOW DQTMJKGD MF KNLJH CVE 900 YCHJZ OH XXFB PJPSKC FVQUSIOV LHP: FRNLLCDBFBF')
        self.assertEqual(vigenere.decode(keyword), 'SOOS LATER FORCED MCGUCKET TO WATCH ALL 900 HOURS OF NEON CRISIS MECHABOT BOY: REVELATIONS')

    @skip(reason="not sure if I am going to program this kind of implementation with the keyword")
    def test_can_decode_weridmaggedon_part_four_somewhere_in_the_woods(self):
        keyword_one = 'HIDDEN DEEP WITHIN THE WOODS A BURIED TREASURE WAITS'
        keyword_two = 'AXOLOTL'
        vigenere_one = Vigenere.objects.create(vigenere_text = 'ZMFUIGV PSHP IGK AGTAYAG TRMNE VVGSQW KLE JOJXU GIMWZ')
        vigenere_two = Vigenere.objects.create(vigenere_text = 'GLCOPRP GOOGWMJ FXZWG')
        self.assertEqual(vigenere_one.decode(keyword_one), 'SECRETS LOST AND STATUES FOUND BEYOND THE RUSTY GATES')
        self.assertEqual(vigenere_two.decode(keyword_two), 'GOODBYE GRAVITY FALLS')

#TESTING FOR COMBINED CIPHERS
