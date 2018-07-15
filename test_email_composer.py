import pytest

from email_composer import email_composer

sample_payload = {
            'client': {
                'name': "Jane Doe",
                'email': "jane@whoami.com"
            },
            'payee': {
                'name': "John Doe",
                'email': "john@zombie.com"
            },
            'payment': {
                'amount': "100",
                'currency': "USD"
            }
        }

def test_email_composer():
    assert email_composer(sample_payload) == "Dear John Doe,\n\nYou have received a payment of 100 USD from Jane Doe (jane@whoami.com).\n\nYours,\nstudent.com"
