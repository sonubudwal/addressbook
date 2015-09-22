from django.test import TestCase
from contacts.models import Contact

# Create your tests here.
class ContactTests(TestCase):
    """  Contact model tests. """

    def test_str(self):
        contact = Contact(first_name = 'Fateh', last_name = 'Budwal')

        self.assertEquals(
            str(contact),
            'Fateh Budwal',
        )