from django.test import TestCase
from help.models import Ask

class AskTests(TestCase):
    def test_str(self):
        ask = Ask(body='I need help badly, dude!', is_closed=False)
        self.assertEquals(
            str(ask),
            'I need hel'
    )
