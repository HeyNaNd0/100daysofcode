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
    1: {"name": "", "breed": "", "pickupTime": "", "dropoffTime": ""},
    2: {"name": "", "breed": "", "pickupTime": "", "dropoffTime": ""},
    3: {"name": "", "breed": "", "pickupTime": "", "dropoffTime": ""},
    4: {"name": "", "breed": "", "pickupTime": "", "dropoffTime": ""}
}

#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
print(f"""Starting Roster:
      {busDict[1]['name']} (Seat 1) - Pickup Time: {busDict[1]['pickupTime']}
      {busDict[2]['name']} (Seat 2) - Pickup Time: {busDict[2]['pickupTime']}
      {busDict[3]['name']} (Seat 3) - Pickup Time: {busDict[3]['pickupTime']}
      {busDict[4]['name']} (Seat 4) - Pickup Time: {busDict[4]['pickupTime']}
""")

# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
MAX_SEATS = 4
newPet = {"name": "Buddy", "breed": "Golden Retriever", "pickupTime": "10:30 AM", "dropoffTime": "11:30 AM"}
if len(busDict) < MAX_SEATS:
    nextSeat = max(busDict.keys()) + 1
    busDict[nextSeat] = newPet
    print(f"""Updated Roster after pickup:
          {busDict[1]['name']} (Seat 1) - Pickup Time: {busDict[1]['pickupTime']}
          {busDict[2]['name']} (Seat 2) - Pickup Time: {busDict[2]['pickupTime']}
          {busDict[3]['name']} (Seat 3) - Pickup Time: {busDict[3]['pickupTime']}
          {busDict[4]['name']} (Seat 4) - Pickup Time: {busDict[4]['pickupTime']}
          {busDict[nextSeat]['name']} (Seat {nextSeat}) - Pickup Time: {busDict[nextSeat]['pickupTime']}
""")
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.
leavingSeat = 2  # Example: Pet in seat 2 is leaving early
if leavingSeat in busDict:
    leavingPet = busDict.pop(leavingSeat)
    print(f"{leavingPet['name']} has headed home early from seat {leavingSeat}.")
    print(f"""Updated Roster after {leavingPet['name']} left:
            {busDict[1]['name']} (Seat 1) - Pickup Time: {busDict[1]['pickupTime']}
            {busDict[3]['name']} (Seat 3) - Pickup Time: {busDict[3]['pickupTime']}
            {busDict[4]['name']} (Seat 4) - Pickup Time: {busDict[4]['pickupTime']}
    """)
# 5. Print a final roster listing the remaining pets and their dropoff times.
print(f"""Final Roster:
      {busDict[1]['name']} (Seat 1) - Dropoff Time: {busDict[1]['dropoffTime']}
      {busDict[3]['name']} (Seat 3) - Dropoff Time: {busDict[3]['dropoffTime']}
      {busDict[4]['name']} (Seat 4) - Dropoff Time: {busDict[4]['dropoffTime']}
""")