import csv
import os
from prettytable import PrettyTable
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def file_selector():
    root = Tk()
    root.withdraw()
    file_path = askopenfilename()
    return str(file_path)

def welcome_message():
    print("Auto Texter Script")
    print("Select your .csv file")
    enter = input("Press enter to continue")

# def send_sms(phone_number, message):
#     pb = Pushbullet('o.dQ75BMOxjgber6nLxVC7RwxyRTHMBTbs')

#     device = pb.devices[1]
#     push = pb.push_sms(device, phone_number, message)
#     if push.get('active', True):
#         print('SMS sent successfully.')
#     else:
#         print('Failed to send SMS.')

def send_sms(phone_number, message, s):
    s.send_message(phone_number, message)

def index_table(csvreader):
    first_row = next(csvreader)
    table = PrettyTable()
    table.field_names = ["Index", "Field Name"]
    for index, value in enumerate(first_row):
        table.add_row([index, value], divider=True)
    print(table)
    print("")

def print_table(csv_reader, first_name_i, phone_number_i, date_i):
    table = PrettyTable()

    header = next(csv_reader)
    table.field_names = [header[first_name_i], header[phone_number_i], header[date_i]]

    for row in csv_reader:
        first_name = row[first_name_i]
        phone_number = row[phone_number_i]
        filter = row[date_i]
        if first_name != "":
            table.add_row([first_name, phone_number, filter])
    print(table)
    print("")
    return table

def print_filtered_table(csv_reader, send_list, first_name_i, phone_number_i, date_i):
    table = PrettyTable()

    header = next(csv_reader)
    table.field_names = [header[first_name_i], header[phone_number_i], header[date_i]]

    for row in send_list:
        table.add_row(row) 
    
    print(table)
    print("")

def paragraph():
    print("Please enter your paragraph. Press Enter three times when you're done:\n")
    lines = []
    enter_count = 0

    while enter_count < 3:
        line = input()
        if line:
            lines.append(line)
        else:
            enter_count += 1

    paragraph = "\n".join(lines)
    print("\nYou entered the following paragraph:\n")
    print(paragraph)
    return paragraph

def attendance_text_sender():
    clear_terminal()
    welcome_message()
    csv_file = file_selector()
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        index_table(csv_reader)
        csvfile.seek(0)

        first_name_index = int(input("Enter index of first name coloum: "))
        phone_number_index = int(input("Enter index of the Phone Number coloum: "))
        date_index = int(input("Enter index of the date to filter by: "))

        print_table(csv_reader, first_name_index, phone_number_index, date_index)
        csvfile.seek(0)

        filter_value = input('Enter value to filter by. eg. "Check": ')

        send_list = []
        for row in csv_reader:
            if row[date_index] == filter_value:
                send_list.append([row[first_name_index], row[phone_number_index], row[date_index]])
        csvfile.seek(0)
        
        print_filtered_table(csv_reader, send_list, first_name_index, phone_number_index, date_index)

    while True:
        greeting = input("Enter greeting\neg. Hi, Good morning, Good afternoon, etc.\n")
        message = paragraph()
        clear_terminal()
        print(f"{greeting}\n\n{message}")
        print("")
        yes = input("Send this message? [y|n] ")
        if (yes == 'y'):
            break
        else:
            clear_terminal()


    ip_address = input("Enter ip address of your phone (refer to docs): ")
    session = AirmoreSession(ip_address)
    service = MessagingService(session)
    for person in send_list:
        print(f"*sending message to {person[0]}*")
        message_to_send = f"{greeting} {person[0]} \n\n" + message
        send_sms(person[1], message_to_send, service)
        print("")

if __name__ == "__main__":
    attendance_text_sender()