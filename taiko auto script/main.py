import pyautogui as gui
import time
from PIL import ImageGrab
import numpy as np

gui.PAUSE = 0


current_time = time.time()


def print_elapsed_time():
    global current_time
    elapsed_time = time.time() - current_time
    current_time = time.time()
    print(f"Elapsed time: {elapsed_time}")


LEFT = 1485
TOP = 400
if __name__ == "__main__":
    while True:

        # print_elapsed_time()

        # Capture the screen
        screenshot = ImageGrab.grab(bbox=(LEFT, TOP, LEFT + 1, TOP + 1))

        # screenshot = np.array(screenshot)
        screenshot = screenshot.load()

        # Get the RGB value at the drum location
        pixel_rgb = screenshot[0, 0]

        r = pixel_rgb[0]
        g = pixel_rgb[1]
        b = pixel_rgb[2]

        if r > 100:
            # print("Red")  # or yellow
            gui.press("f")
        elif b > 100:
            # print("Blue")
            gui.press("d")
