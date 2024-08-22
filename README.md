# EV-Charging
EV Charging Booking System
Overview
The EV Charging Booking System is a command-line application designed for booking electric vehicle (EV) charging slots at various charging stations. It allows users to search for available stations based on location, view available time slots, and book a slot after verifying an OTP (One-Time Password).

# Features
List Charging Stations: Display a list of all available charging stations.</br>
Search by Location: Find stations based on location filters.</br>
View Available Slots: Show available time slots for the selected station.</br>
Book a Slot: Book a slot after verifying an OTP.</br>
Slot Status: Slots are marked as booked once reserved, preventing double bookings.</br>

#Requirements
Python 3.x
Installation
Clone the Repository

#shell
bash
Copy code
git clone <repository-url>
cd <repository-directory>
Ensure Python is Installed

Make sure you have Python 3.x installed. You can download it from python.org.</br>

Usage
Run the Script

#shell
python charging.py
Follow the Prompts

Enter a location filter to search for available stations.
Select a station from the list.
Choose an available time slot.
Enter your name and phone number.
You will receive an OTP for verification. Enter the OTP to confirm your booking.

Example
shell{
Welcome to the EV Charging Booking System

Our PIXEL EV Charging Stations are available in these locations:
- Station A located at Kukatpally
- Station B located at L.B Nagar
- Station C located at Srinagar

Enter location filter (e.g., 'Kukatpally'): Srinagar

Charging Stations Found:
1. Station C - Srinagar (Available Slots: 23-08-2024 03:12 AM, 23-08-2024 04:12 AM)

Select station number: 1
Available slots for Station C:
1. 23-08-2024 03:12 AM
2. 23-08-2024 04:12 AM

Select slot number: 1
Your OTP is: 1234
Enter the OTP to confirm booking: 1234
Enter your name: John Doe
Enter your phone number: 9876543210

Booking confirmed for Station C at 23-08-2024 03:12 AM.}
