import pyautogui
import time
import keyboard # Import the keyboard module

# Delay before starting (in seconds)
initial_delay = 5
# Number of clicks
clicks = 10000
# Delay between clicks (in seconds)
click_delay = 0.01 # Adjust this value as needed

# Countdown before starting
print(f"Auto Clicker will start in {initial_delay} seconds...")
time.sleep(initial_delay)

# Get current mouse position
initial_position = pyautogui.position()

# Click loop
for _ in range(clicks):
# Check if the 'q' key is pressed to cancel
if keyboard.is_pressed('q'):
print("Auto Clicker cancelled.")
break

pyautogui.click(initial_position)
time.sleep(click_delay)

print(f"Auto Clicker completed {clicks} clicks.")


Make note of the line that says "if keyboard.is_pressed('q'):" if you want to stop the auto-clicker, press the Q key on your keyboard.