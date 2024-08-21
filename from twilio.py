from twilio.rest import Client

# Your Account SID and Auth Token from Twilio

account_sid = 'your_account_sid'

auth_token = 'your_auth_token'

# Create a client to interact with Twilio's API

client = Client(account_sid, auth_token)

# Define your Twilio phone number, recipient phone number, and the message

twilio_phone_number = '+1234567890'  # Your Twilio phone number

recipient_phone_number = '+0987654321'  # Recipient's phone number

message_body = 'Hello, this is a test message from Python!'

# Send the SMS

message = client.messages.create(

    body=message_body,

    from_=twilio_phone_number,

    to=recipient_phone_number

)

# Print the SID of the message to confirm it was sent

print(f"Message sent with SID: {message.sid}")