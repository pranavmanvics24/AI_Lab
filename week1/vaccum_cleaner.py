import random

# Define the environment (1D array of rooms)
NUM_ROOMS = 10
# Initialize rooms randomly: 'dirty', 'clean', or 'obstacle'
rooms = [random.choice(['dirty', 'clean', 'obstacle']) for _ in range(NUM_ROOMS)]

# Ensure at least one dirty room and one obstacle for a good test case (optional)
if 'dirty' not in rooms:
    rooms[random.randint(0, NUM_ROOMS - 1)] = 'dirty'
if 'obstacle' not in rooms:
    rooms[random.randint(0, NUM_ROOMS - 1)] = 'obstacle'

# Define the vacuum cleaner's initial state
vacuum_position = random.randint(0, NUM_ROOMS - 1) # Start at a random room

# Ensure vacuum doesn't start on an obstacle
while rooms[vacuum_position] == 'obstacle':
    vacuum_position = random.randint(0, NUM_ROOMS - 1)

print(f"Initial rooms: {rooms}")
print(f"Vacuum cleaner starts at room index: {vacuum_position}")

def clean_rooms(rooms, initial_position):
    cleaned_rooms = list(rooms) # Create a copy to modify
    
    print("\n--- Cleaning Process ---")
    
    # Strategy: Clean to the right, then clean to the left, stopping at obstacles
    
    # Pass 1: Clean to the right from the initial position
    for i in range(initial_position, NUM_ROOMS):
        if cleaned_rooms[i] == 'obstacle':
            print(f"Vacuum at room {i}: Encountered an obstacle. Stopping rightward movement.")
            break
        elif cleaned_rooms[i] == 'dirty':
            print(f"Vacuum at room {i}: Cleaning dirty room.")
            cleaned_rooms[i] = 'clean'
        else:
            print(f"Vacuum at room {i}: Room is already clean.")

    # Pass 2: Clean to the left from the initial position (excluding the initial position if already cleaned)
    for i in range(initial_position - 1, -1, -1):
        if cleaned_rooms[i] == 'obstacle':
            print(f"Vacuum at room {i}: Encountered an obstacle. Stopping leftward movement.")
            break
        elif cleaned_rooms[i] == 'dirty':
            print(f"Vacuum at room {i}: Cleaning dirty room.")
            cleaned_rooms[i] = 'clean'
        else:
            print(f"Vacuum at room {i}: Room is already clean.")

    print("--- Cleaning Complete ---")
    return cleaned_rooms

# Run the cleaning simulation
final_rooms = clean_rooms(rooms, vacuum_position)
print(f"\nInitial state of rooms: {rooms}")
print(f"Final state of rooms:   {final_rooms}")

if all(room == 'clean' for room in final_rooms):
    print("All rooms are now clean!")
else:
    print("Some rooms might still be dirty")
