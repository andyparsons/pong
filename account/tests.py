from django.test import TestCase
from django.contrib.auth.models import User
from account.models import UserProfile

class ProfileTests(TestCase):
    def test_user_stuff(self):
        user = User(first_name='Snoot', last_name='Magoot', email='snoot@poot.com')
        user.save()
        profile = user.profile
        profile.company = 'LDV Capital'
        profile.save()
        self.assertEquals(
            user.profile.company,
            'LDV Capital'
    )
