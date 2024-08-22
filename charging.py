from datetime import datetime, timedelta
import random

class Station:
    def __init__(self, id, name, address, slots):
        self.id = id
        self.name = name
        self.address = address
        self.slots = slots  
        self.booked_slots = {} 

    def is_slot_available(self, slot):
        return slot in self.slots and slot not in self.booked_slots

    def book_slot(self, slot, otp, user_info):
        if self.is_slot_available(slot):
            self.booked_slots[slot] = {'otp': otp, 'status': 'occupied', 'user_info': user_info}
            return True
        elif slot in self.booked_slots and self.booked_slots[slot]['otp'] == otp:
            self.booked_slots[slot]['status'] = 'occupied'
            self.booked_slots[slot]['user_info'] = user_info
            return True
        return False

    def __str__(self):
        available_slots = [slot for slot in self.slots if slot not in self.booked_slots]
        booked_slots = [f"{slot} (Booked by {self.booked_slots[slot]['user_info']['name']})"
                        for slot in self.booked_slots if self.booked_slots[slot]['status'] == 'occupied']
        all_slots = available_slots + booked_slots
        return f"{self.name} - {self.address} (Available Slots: {', '.join(all_slots)})"

class EVSystem:
    def __init__(self):
        # Simulated in-memory stations with slots in 'dd-mm-yyyy hh:mm AM/PM' format
        now = datetime.now()
        self.stations = [
            Station("1", "Station A", "Kukatpally", [
                (now + timedelta(hours=1)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=2)).strftime("%d-%m-%Y %I:%M %p")
            ]),
            Station("2", "Station B", "L.B Nagar", [
                (now + timedelta(hours=3)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=4)).strftime("%d-%m-%Y %I:%M %p")
            ]),
            Station("3", "Station C", "Srinagar", [
                (now + timedelta(hours=5)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=6)).strftime("%d-%m-%Y %I:%M %p")
            ]),
            Station("4", "Station D", "MVP Colony", [
                (now + timedelta(hours=7)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=8)).strftime("%d-%m-%Y %I:%M %p")
            ]),
            Station("5", "Station E", "RushiKonda", [
                (now + timedelta(hours=9)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=10)).strftime("%d-%m-%Y %I:%M %p")
            ]),
            Station("6", "Station F", "Secunderabad", [
                (now + timedelta(hours=11)).strftime("%d-%m-%Y %I:%M %p"),
                (now + timedelta(hours=12)).strftime("%d-%m-%Y %I:%M %p")
            ]),
        ]

    def find_stations(self, loc):
        return [s for s in self.stations if loc.lower() in s.address.lower()]

    def generate_otp(self):
        return random.randint(1000, 9999)

    def verify_otp(self, otp):
        return otp.isdigit() and 1000 <= int(otp) <= 9999

    def book_slot(self, id, slot, otp, user_info):
        for s in self.stations:
            if s.id == id:
                if s.book_slot(slot, otp, user_info):
                    return f"Booking confirmed for {s.name} at {slot}."
                elif slot in s.booked_slots:
                    return f"OTP verified, but slot was already booked by {s.booked_slots[slot]['user_info']['name']}."
                return "Invalid OTP or slot is unavailable."
        return "Station not found."

def main():
    ev_sys = EVSystem()

    print("Welcome to the EV Charging Booking System")
    print("\nOur PIXEL EV Charging Stations are available in these locations:")
    for s in ev_sys.stations:
        print(f"- {s.name} located at {s.address}")
    
    loc_filter = input("\nEnter location filter (e.g., 'Kukatpally'): ")

    found_stations = ev_sys.find_stations(loc_filter)

    if not found_stations:
        print("No stations found.")
        return

    print("\nCharging Stations Found:")
    for i, s in enumerate(found_stations):
        print(f"{i+1}. {s}")

    try:
        while True:
            choice = int(input("\nSelect station number: ")) - 1
            if choice < 0 or choice >= len(found_stations):
                print("Invalid number.")
                continue

            selected_station = found_stations[choice]
            print(f"Available slots for {selected_station.name}:")
            available_slots = [slot for slot in selected_station.slots if selected_station.is_slot_available(slot)]
            
            if not available_slots:
                print("No available slots.")
                return

            for idx, slot in enumerate(available_slots):
                print(f"{idx+1}. {slot}")

            slot_index = int(input("Select slot number: ")) - 1
            if slot_index < 0 or slot_index >= len(available_slots):
                print("Invalid slot number.")
                continue

            slot = available_slots[slot_index]

            otp = ev_sys.generate_otp()
            print(f"Your OTP is: {otp}")

            user_otp = input("Enter the OTP to confirm booking: ")
            
            user_name = input("Enter your name: ")
            user_phone = input("Enter your phone number: ")

            user_info = {
                'name': user_name,
                'phone': user_phone
            }

            confirmation = ev_sys.book_slot(selected_station.id, slot, user_otp, user_info)
            print(confirmation)

            if "Booking confirmed" in confirmation:
                break  

    except ValueError:
        print("Invalid input. Enter a number.")

if __name__ == "__main__":
    main()
