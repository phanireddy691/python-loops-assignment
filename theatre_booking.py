# Initial State
total_capacity = 350
remaining_seats = 350
total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while remaining_seats > 0:
    # 1. Ask for number of tickets
    num_tickets = int(input("Enter number of tickets (1-15) or 0 to exit: "))
    
    # Check for exit condition
    if num_tickets == 0:
        break
        
    # Validate ticket range and availability
    if num_tickets < 1 or num_tickets > 15 or num_tickets > remaining_seats:
        print("BOOKING REJECTED - Invalid number of tickets or not enough seats.")
        rejected_bookings += 1
        continue  # Skip to the next iteration of the while loop

    # 2. Check ages for the requested tickets
    is_valid_booking = True
    for i in range(num_tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        if age < 12:
            is_valid_booking = False
            # We don't need to ask for more ages if one is invalid
            break 

    # 3. Process Booking Status
    if is_valid_booking:
        remaining_seats -= num_tickets
        tickets_sold += num_tickets
        total_bookings += 1
        print(f"BOOKING CONFIRMED - {num_tickets} tickets")
    else:
        rejected_bookings += 1
        print("BOOKING REJECTED - Age restriction (all must be 12+)")

# 4. Final Report
print("\n--- Final Report ---")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {remaining_seats}")


