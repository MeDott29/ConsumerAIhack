import os
import time
from datetime import datetime
import random

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    """Get current time in 12-hour format."""
    return datetime.now().strftime("%I:%M %p")

def draw_phone(is_picked_up=False, screen_on=False):
    """Draw ASCII art of phone in different states."""
    if is_picked_up:
        angle = "  "  # Tilted phone
    else:
        angle = "--"  # Flat phone
    
    time_display = get_current_time() if screen_on else "       "
    
    phone = f"""
    {angle}-------------
    |             |
    |    {time_display}    |
    |             |
    |             |
    |             |
    |      O      |
    ---------------
    """
    return phone

def simulate_accelerometer():
    """Simulate accelerometer readings during pickup."""
    return random.uniform(0.8, 1.2)

def run_simulation():
    """Run the phone pickup simulation."""
    try:
        while True:
            # Phone lying flat
            clear_screen()
            print("\nPhone is lying flat on the table. Press Enter to pick it up (Ctrl+C to exit)...")
            print(draw_phone(is_picked_up=False, screen_on=False))
            input()

            # Simulate picking up motion
            for _ in range(3):
                clear_screen()
                accel = simulate_accelerometer()
                print(f"\nPicking up phone... (Accelerometer: {accel:.2f}g)")
                print(draw_phone(is_picked_up=True, screen_on=False))
                time.sleep(0.2)

            # Phone is picked up and screen turns on
            clear_screen()
            print("\nPhone is picked up and screen is on!")
            print(draw_phone(is_picked_up=True, screen_on=True))
            time.sleep(2)

            # Auto screen timeout after 5 seconds
            for i in range(5, 0, -1):
                clear_screen()
                print(f"\nScreen will turn off in {i} seconds...")
                print(draw_phone(is_picked_up=True, screen_on=True))
                time.sleep(1)

            # Screen turns off but phone still tilted
            clear_screen()
            print("\nScreen timed out. Press Enter to put the phone down...")
            print(draw_phone(is_picked_up=True, screen_on=False))
            input()

    except KeyboardInterrupt:
        clear_screen()
        print("\nSimulation ended. Goodbye!")

if __name__ == "__main__":
    print("Phone Pick-up Simulation")
    print("========================")
    run_simulation()