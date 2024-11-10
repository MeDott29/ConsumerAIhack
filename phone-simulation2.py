import os
import time
from datetime import datetime
import random
import itertools

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    """Get current time in 12-hour format."""
    return datetime.now().strftime("%I:%M %p")

def draw_phone(is_picked_up=False, screen_content=None, power_button_highlight=False):
    """Draw ASCII art of phone in different states."""
    if is_picked_up:
        angle = "  "  # Tilted phone
    else:
        angle = "--"  # Flat phone
    
    if screen_content is None:
        screen = "             "
    else:
        screen = screen_content

    # Power button highlight
    power_btn = "►" if power_button_highlight else "│"
    
    phone = f"""
    {angle}-------------
    {power_btn}{screen}|
    |{screen}|
    |{screen}|
    |{screen}|
    |{screen}|
    |      O      |
    ---------------
    """
    return phone

def get_video_frame(frame_num):
    """Generate educational video frames."""
    videos = [
        # DNA double helix animation
        [
            "   🧬 DNA    ",
            "    ╱╲      ",
            "   ╱──╲     ",
            "  ╱    ╲    ",
            " ╱──────╲   "
        ],
        # Math equation animation
        [
            "   2+2=4    ",
            "   3×3=9    ",
            "   5÷5=1    ",
            "   7-4=3    ",
            "   x²=25    "
        ],
        # Planet orbit animation
        [
            "    ☀️      ",
            "   🌍 →     ",
            "    ↑ ↓     ",
            "   ← 🌑     ",
            "           "
        ]
    ]
    
    current_video = videos[frame_num % len(videos)]
    return current_video

def simulate_accelerometer():
    """Simulate accelerometer readings during pickup."""
    return random.uniform(0.8, 1.2)

def power_button_animation():
    """Animate the power button press."""
    for _ in range(2):
        clear_screen()
        print("\nPress the power button (highlighted)...")
        print(draw_phone(is_picked_up=True, power_button_highlight=True))
        time.sleep(0.3)
        clear_screen()
        print("\nPress the power button (highlighted)...")
        print(draw_phone(is_picked_up=True, power_button_highlight=False))
        time.sleep(0.3)

def run_simulation():
    """Run the phone pickup simulation."""
    try:
        while True:
            # Phone lying flat
            clear_screen()
            print("\nPhone is lying flat on the table. Press Enter to pick it up (Ctrl+C to exit)...")
            print(draw_phone(is_picked_up=False))
            input()

            # Simulate picking up motion
            for _ in range(3):
                clear_screen()
                accel = simulate_accelerometer()
                print(f"\nPicking up phone... (Accelerometer: {accel:.2f}g)")
                print(draw_phone(is_picked_up=True))
                time.sleep(0.2)

            # Prompt for power button press
            power_button_animation()
            print("Press Enter to simulate pressing the power button...")
            input()

            # Phone is picked up and shows time briefly
            clear_screen()
            time_screen = [
                f"             ",
                f"             ",
                f"  {get_current_time()}    ",
                f"             ",
                f" Swipe up to ",
            ]
            print("\nPhone is picked up and screen is on!")
            print(draw_phone(is_picked_up=True, screen_content=time_screen))
            time.sleep(1)

            # Educational video plays for 15 seconds
            print("\nPlaying educational video...")
            start_time = time.time()
            frame = 0
            while time.time() - start_time < 15:
                clear_screen()
                remaining_time = 15 - int(time.time() - start_time)
                print(f"\nEducational Video Playing... ({remaining_time}s remaining)")
                video_frame = get_video_frame(frame)
                print(draw_phone(is_picked_up=True, screen_content=video_frame))
                frame += 1
                time.sleep(0.8)

            # Video ends, screen timeout countdown
            for i in range(5, 0, -1):
                clear_screen()
                end_screen = [
                    "             ",
                    "  Video End  ",
                    f" Timeout: {i}s ",
                    "             ",
                    "             ",
                ]
                print(f"\nScreen will turn off in {i} seconds...")
                print(draw_phone(is_picked_up=True, screen_content=end_screen))
                time.sleep(1)

            # Screen turns off but phone still tilted
            clear_screen()
            print("\nScreen timed out. Press Enter to put the phone down...")
            print(draw_phone(is_picked_up=True))
            input()

    except KeyboardInterrupt:
        clear_screen()
        print("\nSimulation ended. Goodbye!")

if __name__ == "__main__":
    print("Phone Pick-up Simulation with Educational Video")
    print("=============================================")
    print("\nInstructions:")
    print("1. Press Enter to pick up the phone")
    print("2. Press Enter again to press the power button when prompted")
    print("3. Watch the educational video")
    print("4. Press Enter to put the phone down when finished")
    print("5. Press Ctrl+C to exit the simulation")
    print("\nStarting simulation...")
    time.sleep(3)
    run_simulation()