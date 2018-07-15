from faker import Factory
from email_composer import email_composer
from env import api_key
from nameko.events import EventDispatcher, event_handler
from nameko.timer import timer
import requests

fake = Factory.create()

class PaymentService(object):
    name = "payments"

    dispatch = EventDispatcher()

    @timer(interval=10)
    def emit_event(self):

        payload = {
            'client': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payee': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payment': {
                'amount': fake.random_int(),
                'currency': fake.random_element(
                    ("USD", "GBP", "EUR")
                )
            }
        }
        self.dispatch("payment_received", payload)

class MailingService(object):
    name = "emails"

    @event_handler("payments", "payment_received")
    def send_email(self, payload):

        body = email_composer(payload)
        email = payload["payee"]["email"]
        amount = payload["payment"]["amount"]
        currency = payload["payment"]["currency"]

        return requests.post(
        "https://api.mailgun.net/v3/sandboxe5cbc07f22d64cb28db5d17075ae7971.mailgun.org/messages",
        auth=("api", api_key),
        data={"from": "Student.com <mailgun@sandboxe5cbc07f22d64cb28db5d17075ae7971.mailgun.org>",
              "to": "{email}".format(email=email),
              "subject": "You just received {amount} {currency}!".format(amount=amount,currency=currency),
              "text": body
              })
