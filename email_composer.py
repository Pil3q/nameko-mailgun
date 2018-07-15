def email_composer(data):
    payee = data["payee"]["name"]
    amount = data["payment"]["amount"]
    currency = data["payment"]["currency"]
    client = data["client"]["name"]
    email = data["client"]["email"]

    body = "Dear {payee},\n\nYou have received a payment of {amount} {currency} from {client} ({email}).\n\nYours,\nstudent.com"
    return body.format(payee=payee,amount=amount,currency=currency,client=client,email=email)
