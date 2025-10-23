# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time

busDict = {
    1: {"name": "Max", "breed": "Labrador", "pickupTime": "9:00 AM", "dropoffTime": "5:00 PM"},
    2: {"name": "Bella", "breed": "Poodle", "pickupTime": "9:15 AM", "dropoffTime": "4:30 PM"},
    3: {"name": "Charlie", "breed": "Beagle", "pickupTime": "9:30 AM", "dropoffTime": "5:15 PM"},
    4: {"name": "Luna", "breed": "Husky", "pickupTime": "9:45 AM", "dropoffTime": "5:30 PM"}
}

#
# 2. Print a starting roster showing each pet's seat, name, and pickup time.
print("Starting Roster:")
for seat, pet in busDict.items():
    print(f"  {pet['name']} (Seat {seat}) - Pickup Time: {pet['pickupTime']}")
print()

# 3. Add one new pet if there's room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
MAX_SEATS = 6
newPet = {"name": "Buddy", "breed": "Golden Retriever", "pickupTime": "10:30 AM", "dropoffTime": "11:30 AM"}
if len(busDict) < MAX_SEATS:
    nextSeat = max(busDict.keys()) + 1
    busDict[nextSeat] = newPet
    print("Updated Roster after pickup:")
    for seat, pet in busDict.items():
        print(f"  {pet['name']} (Seat {seat}) - Pickup Time: {pet['pickupTime']}")
    print()
else:
    print(f"Bus is full! Cannot add {newPet['name']}.")
    print()
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they've headed home.
leavingSeat = 2  # Example: Pet in seat 2 is leaving early
if leavingSeat in busDict:
    leavingPet = busDict.pop(leavingSeat)
    print(f"{leavingPet['name']} has headed home early from seat {leavingSeat}.")
    print(f"Updated Roster after {leavingPet['name']} left:")
    for seat, pet in busDict.items():
        print(f"  {pet['name']} (Seat {seat}) - Pickup Time: {pet['pickupTime']}")
    print()
else:
    print(f"No pet found in seat {leavingSeat}.")
    print()
# 5. Print a final roster listing the remaining pets and their dropoff times.
print("Final Roster:")
for seat, pet in busDict.items():
    print(f"  {pet['name']} (Seat {seat}) - Dropoff Time: {pet['dropoffTime']}")