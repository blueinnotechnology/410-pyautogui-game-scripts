from pynput.mouse import Listener
import pyautogui
from PIL import ImageGrab
import time


# Initialize pyautogui
pyautogui.PAUSE = 0

# Initialize holes (with default values for manual, empty for automatic)
holes = [
    # (1215, 258),
    # (1430, 265),
    # (1310, 318),
    # (1560, 310),
    # (1170, 380),
    # (1430, 400),
    # (1640, 400),
    # (1150, 510),
    # (1380, 540),
    # (1620, 540)
]

# Function to be called by the listener
# Stop the listener when clicked 10 times
def on_clicked(x, y, button, pressed):
    if (len(holes) >= 10):
        with open("holes.txt", "w") as f:
            for (x, y) in holes:
                f.write(f"{int(x)}, {int(y)}\n")
        
        return False # Stop the listener
    
    if pressed:
        holes.append((x, y))
        return True # Continue the listener


# Ask the user if wants to recalibrate
calibrate = input("Recalibrate? (y/n)")
if calibrate == "y":
    print("Click on the 10 holes.")
    with Listener(on_click=on_clicked) as listener:
        listener.join()

# Read the holes positions from the file
with open("holes.txt", "r") as f:
    for line in f.readlines():
        x, y = line.split(", ")
        holes.append((int(x), int(y)))
    
# Record the start time
start_time = time.time()

# Loop until 65 seconds
while (time.time() - start_time) < 65:
    
    screenshot = ImageGrab.grab()
    screenshot_data = screenshot.load()

    for (x, y) in holes:

        # Get the pixel color at the hole
        pixel = screenshot_data[x, y]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        is_black = r < 50 and g < 50 and b < 50
        if not is_black:
            pyautogui.click(x, y)
