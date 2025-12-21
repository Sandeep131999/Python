from twilio.rest import Client

# Twilio credentials
account_sid = "AC45e87b4a4e2c4981cef936cb61b0f720"
auth_token = "88fb1eac2e458b98af33e9d2c646bdc4"
client = Client(account_sid, auth_token)
def send_message(msg):
    message = client.messages.create(
        body=msg,
        # Your Twilio phone number
        from_="+12295973568",
        # Recipient's phone number
        to="+919206754274"
    )
    return message.sid