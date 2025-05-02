# "Barber Matteo"

#### Demo Video: https://youtu.be/aH80gKGzpyo 
#### Overview: barbershop appointment booking system

**Barber Matteo** is a simple system which helps customers to easily schedule and book an appointment in a barbershop. It provides user-friendly experience, allowing users to input their information first and then select the time slot they want by the number of that time slot. Program then handles these appointments, creates two CSV files, user.csv and appointments.csv where all info will be stored. 

### Gaol of the project: 
to simplify the appointment booking process and reduce wait times, benefiting both customers and the barbershop.

### Key Features:
- **Intuitive Interface:** System has easy-to-use and friendly interface that guides the users in every step. 
- **Flexible Scheduling:** Customers can book a time slot(s) for a maximum of 2 people at a time. All available days alongside with their time slots are shown. For the next user the chosen sloe before will not be displayed, ensuring no double bookings. 
- **Data Management:** Program then handles these appointments, creates two CSV files, user.csv and appointments.csv where all info will be stored. 
- **Working Hours:** At the beginning, it shows the working hours for the barbershop, including break times, and day offs. 

### File Overview:
- `main.py`: The main script that handles the booking flow, user inputs, and storing data. It also checks availability and writes appointment details to `appointments.csv`.
- `appointments.csv`: This file stores the appointments, including slot index, day, time, and customer details. The system ensures no overbooking by checking current bookings.
- `users.csv`: Stores customer information (name and phone number) for each booking. This file is updated whenever a new appointment is made.
- `test_project.py`: imports three functoins from `project.py` and tests them using `pytest`.

### Core Functions:
- **`main()`**: The central function that drives the entire booking process. It collects user details, checks available slots, and writes the appointment data to the CSV files.
- **`welcome_message()`**: Displays a greeting to customers, introducing them to the booking system.
- **`schedule()`**: Shows the barbershop's operating hours, including opening times and break periods.
- **`n_customers()`**: Prompts the user to choose how many people will be booking (1 or 2).
- **`get_user_info()`**: Gathers customer names and phone numbers.
- **`write_user_info()`**: Saves customer information into the `users.csv` file.
- **`now()`**: Prints the current date and time for the user in Rome.
- **`show_slots_return_choice()`**: Displays available time slots and asks the user to select a slot for booking.
- **`appointments()`**: Creates and writes to `appointments.csv` if the file doesn't exist.
- **`write_appointments()`**: Writes the booking details to `appointments.csv`.

### Design Decisions:
- **Using CSV Files for Data Storage:** I used CSV files because they are easy to use. Also, I want to further work on this project and create a Telegram Bot from it. 
- **Slot Indexing:** Each available slot is given an index number, allowing for easy identification and tracking of appointments.
- **Support for Multiple Bookings:** The system supports both single and double bookings in one session, providing flexibility for customers.

### test_project.py
It imports three functions from the main project function and checks them using `pytest`'s `monkeypatch` fixture. 

### Requirements:
- `rich` library
- `tabulate` library
- `pytz` library
- `ascii-magic` library

### How to Use:
1. Clone this repository.
2. Install required libraries using `pip install rich tabulate pytz ascii-magic`.
3. Run the script with `python main.py`.
4. Follow the instructions on-screen to book an appointment.
