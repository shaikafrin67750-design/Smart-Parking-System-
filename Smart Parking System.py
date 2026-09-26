# Smart Parking System using Python

parking_slots = {
1: None,
2: None,
3: None,
4: None,
5: None
}

def show_slots():
print("\n===== PARKING SLOT STATUS =====")

```
for slot, vehicle in parking_slots.items():
    if vehicle is None:
        print(f"Slot {slot}: EMPTY")
    else:
        print(f"Slot {slot}: {vehicle}")
```

def park_vehicle():
print("\n===== PARK VEHICLE =====")

```
vehicle_number = input("Enter vehicle number: ").upper()

if not vehicle_number:
    print("Vehicle number cannot be empty.")
    return

# Check whether vehicle is already parked
for vehicle in parking_slots.values():
    if vehicle == vehicle_number:
        print("Vehicle is already parked.")
        return

# Find an empty slot
for slot in parking_slots:
    if parking_slots[slot] is None:
        parking_slots[slot] = vehicle_number
        print(f"Vehicle {vehicle_number} parked in Slot {slot}.")
        return

print("Parking Full!")
```

def remove_vehicle():
print("\n===== REMOVE VEHICLE =====")

```
vehicle_number = input("Enter vehicle number: ").upper()

for slot, vehicle in parking_slots.items():
    if vehicle == vehicle_number:
        parking_slots[slot] = None
        print(f"Vehicle {vehicle_number} removed from Slot {slot}.")
        return

print("Vehicle not found.")
```

while True:
print("\n===== SMART PARKING SYSTEM =====")
print("1. Show Parking Slots")
print("2. Park Vehicle")
print("3. Remove Vehicle")
print("4. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    show_slots()

elif choice == "2":
    park_ve_
```
