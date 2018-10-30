import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Caesar, Atbash, Alphanumeric, Viginere

class CaesarTestCase(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        offset = 3
        secret = 'VWDQ LV QRW ZKDW KH VHHPV'
        self.assertIs(future_question.was_published_recently(), False)
