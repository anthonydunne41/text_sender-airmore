import time
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService


# i = 0
# while True:
#     session = AirmoreSession(ip_address)
#     service = MessagingService(session)
#     service.send_message(phone_number, message)


    # print("Please enter your paragraph. Press Enter three times when you're done:\n")
    # lines = []
    # enter_count = 0

    # while enter_count < 3:
    #     line = input()
    #     if line:
    #         lines.append(line)
    #     else:
    #         enter_count += 1

    # paragraph = "\n".join(lines)
    # print("\nYou entered the following paragraph:\n")
    # print(paragraph)

# def send_sms(phone_number, message):
#     pb = Pushbullet('o.dQ75BMOxjgber6nLxVC7RwxyRTHMBTbs')

#     device = pb.devices[1]
#     push = pb.push_sms(device, phone_number, message)
#     if push.get('active', True):
#         print('SMS sent successfully.')
#     else:
#         print('Failed to send SMS.')