import csv
import os 
import re
from rich import print as r_print
from rich.console import Console
from ascii_magic import AsciiArt 
from datetime import datetime
from tabulate import tabulate  
from rich.table import Table 
from pytz import timezone
import time

#collection of all individual functions
def main():
    available_slots = {
        "Tuesday": ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", 
                    "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"], 
        "Wednesday": ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", 
                    "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"], 
        "Thursday": ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", 
                    "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"], 
        "Friday": ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", 
                    "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"], 
        "Saturday": ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", 
                    "15:00-16:00", "16:00-17:00", "17:00-18:00"], 
    }  
    
    welcome_message()

    schedule() 

    # create a list to add info
    user_list = []
    n_people = n_customers()
    get_user_info(user_list, n_people)

    appointments("appointments.csv")

    #current date/time and info message:
    now()
    time.sleep(7)

    # add user info to CSV
    write_user_info(user_list, "users.csv")
    user_choice_number = show_slots_return_choice(available_slots, "appointments.csv", n_people)

    write_appointments(user_list, user_choice_number, n_people, "appointments.csv")  

    print("😀Great. We got your appointment. Arrive 5 minutes early, please. See you.👋") 

#wellcome message
def welcome_message():
    console = Console() 
    console.rule("[bold white]💺 Barber Matteo💈")  
    console.print("Welcome to **Matteo's Barbershop! 💈✨**", justify="center")  
    console.print("Our booking system makes scheduling an appointment quick and hassle-free ⏳✅", justify="center")  
    console.print("saving you time that would otherwise be spent waiting in line ⌛.", justify="center")  
    console.print("Just follow the on-screen instructions,", justify="center")  
    console.print("and we'll guide you through smoothly. Let's start now....👉📅**!", justify="center")  
    console.rule("[bold white]💺 Barber Matteo💈")  

#working hours
def schedule(): 
    console = Console()
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("[underline]Day:🗓️[/underline]", width=20, justify="center")
    table.add_column("[underline]Working Hours:🕰️[/underline]", width=20, justify="center")
    table.add_row("Monday & Sunday", "[italic]Closed[/italic]")
    table.add_row("Tuesday - Friday", "[italic]8:30 - 19:00[/italic]")
    table.add_row("Saturday", "[italic]8:30 - 18:00[/italic]") 
    table.add_row("***break☕***", "[italic]12:30 - 15:00[/italic]")
    console.print(table)

#choose the number of customers
def n_customers(): 
    while True:
        n_people = input("For how many customers do you want to book an appointment✍️  ?: ")
        if n_people.isdigit():
            n_people = int(n_people) 
            if n_people > 0 and n_people < 3:
                return n_people
            else:
                print("❌You can take an appointment for a max. of 2 people at a time...")
        else:
            print("❌Please enter an integer (1 or 2)...") 

#input info of n_customers
def get_user_info(some_list, n_people):
    for i in range(n_people):
        first_name, last_name, phone = None, None, None

        while not first_name:  
            first_name = input(f"Customer #{i+1} first name: ").strip().title()
            if not re.match("^[a-zA-Z]+$", first_name):
                print("❌First name inputted incorrectly. Please check your name...")
                first_name = None  
        
        while not last_name:  
            last_name = input(f"Customer #{i+1} last name: ").strip().title()
            if not re.match("^[a-zA-Z]+$", last_name):
                print("❌Last name inputted incorrectly. Please check your last name...")
                last_name = None 
        
        while not phone:  
            phone = input(f"Customer #{i+1} phone number after +39-📞: ")
            if not re.match(r"^\d{10}$", phone):
                print("❌Please include only numbers and no need to include +39...")
                phone = None 
        
        phone = "+39" + phone
        some_list.append([first_name, last_name, phone])  
    return some_list

#add info of n customers to users.csv
def write_user_info(users_list, file):
    file_exists = os.path.isfile(file)
    write_headers = not (file_exists and os.path.getsize(file) > 0)

    with open(file, "a", newline="") as write_file:
        writer = csv.writer(write_file)
        if write_headers:
            writer.writerow(["first_name", "last_name", "phone_number"])
        for info in users_list:
            writer.writerow(info)

#today's date/time
def now():  
    time_zone_it = timezone("Europe/Rome")
    today = datetime.now(time_zone_it).strftime("%Y-%m-%d, %H:%M, %A")
    r_print(f"🗓️ 🕰️ Date/time as of now in Rome/Italy🍕: ***[italic][green][bald]{today}[/italic][/green][/bald]***") 
    r_print(f"You can see available date/times starting from next week, Tuesday: 1....2...3...👇")

#show available slots and get/return user choice
def show_slots_return_choice(dict_of_lists, csv_file, n):
    #number each slot in available slots [[]] 
    counter = 1 
    numbered_slots = []
    for day, slots in dict_of_lists.items(): 
        for spcific_time in slots:
            numbered_slots.append([counter, day, spcific_time]) 
            counter = counter + 1
    
    #make a list of indexes of available slots
    available_slots_indexes = []
    for list in numbered_slots: 
        available_slots_indexes.append(list[0]) 

    #read appointments.csv and return a list of indexes of booked slots
    with open(csv_file, "r") as read_file:
        reader = csv.DictReader(read_file) 

        booked_slots_indexes = []
        for dictionary in reader: 
            booked_slots_indexes.append(int(dictionary["slot_index"])) 
    
    #only leave free slots
    free_slots = [slot for slot in numbered_slots if slot[0] not in booked_slots_indexes]


    #print only the available slots:
    headers = ["#","day", "time slot"]
    table = tabulate(free_slots, headers=headers, tablefmt="fancy_grid")
    print(table)


    #ask for slot from user
    while True:
        if n == 1: 
            user_choice = input("Choose a time slot by it's number: ")
            if user_choice.isdigit():
                user_choice = int(user_choice)
                break
            else:
                print("Please enter a number, 1 or 2...") 
                continue 

        elif n == 2:
            user_choice_1 = input("Please select a time slot by its number for person #1: ")
            user_choice_2 = input("Please select a time slot by its number for person #2: ")
            if user_choice_1.isdigit() and user_choice_2.isdigit():
                user_choice_1, user_choice_2 = int(user_choice_1), int(user_choice_2) 
                user_choices_tuple = (user_choice_1, user_choice_2)
                break
            else: 
                print("Please enter a number, 1 or 2...") 
                continue             

    #extract the chosen slot
    if 'user_choice' in locals():  # Checks if user_choice exists
        for slot in numbered_slots:
            if slot[0] == user_choice:
                index_day_time = [slot[0], slot[1], slot[2]]
                return index_day_time
 
    elif 'user_choices_tuple' in locals():  # Checks if user_choices_tuple exists
        slot_1 = slot_2 = None
        for slot in numbered_slots:
            if slot[0] == user_choices_tuple[0]: 
                slot_1 = [slot[0], slot[1], slot[2]]
            elif slot[0] == user_choices_tuple[1]:
                slot_2 = [slot[0], slot[1], slot[2]]
                return [slot_1, slot_2]

#create appointments.csv and write headers
def appointments(file):
    if not os.path.isfile(file):
        with open(file, "a", newline="") as csv_file:
            csv.writer(csv_file).writerow(["slot_index", "day", "time", "last_name", "first_name", "phone_number"])

#write all the info to appointments
def write_appointments(user_list, selected_slots, n, file):
    #open appointments.csv 
    with open(file, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
    
    # if only 1 person: 
        if n == 1:
            day_index, day, time = selected_slots[0], selected_slots[1], selected_slots[2]
            first_name, last_name, phone_number = user_list[0][0], user_list[0][1], user_list[0][2]
            writer.writerow([day_index, day, time, last_name, first_name, phone_number])
        
        elif n == 2:
            for i in range(2):
                    day_index, day, time = selected_slots[i][0], selected_slots[i][1], selected_slots[i][2]
                    first_name, last_name, phone_number = user_list[i][0], user_list[i][1], user_list[i][2]
                    writer.writerow([day_index, day, time, last_name, first_name, phone_number])

if __name__ == "__main__":
    main() 