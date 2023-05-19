    # for person in send_list:
    #     print(f"*sending message to {person[0]}*")
    #     message_to_send = f"{greeting} {person[0]} \n\n" + message
    #     print(message_to_send)
    #     print("")

import time
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService


phone_number = "0432412105"
message = "Hello world"
ip_address = "10.19.241.17"  # Replace with the IP address of your device
recipient = 'phone_number'  # Replace 'phone_number' with the recipient's phone number

i = 0
while True:
    session = AirmoreSession(ip_address)
    service = MessagingService(session)
    service.send_message(phone_number, message)