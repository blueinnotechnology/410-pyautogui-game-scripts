import math
import pyautogui as gui
from pynput.mouse import Listener
from PIL import ImageGrab

gui.PAUSE = 0.05

FILE_NAME = "coordinates.txt"
keys = ['H', 'J', 'K', 'L']


# Coordinates of the corners of the region of interest
# Run `get_mouse.py` to get the coordinates
left = 1425
right = 1919
top = 631
bottom = 796

width = right - left
height = bottom - top
divider = len(keys) + 1
center_y = math.floor(height / 2)


####################################################################################################
#                                For Arcade Mode                                                   #
#
# Used to calculate speed
frame_id = 0
#
# Make sure the region of interest doesn't go beyond the top edge.
min_y = 200
####################################################################################################


while True:
    ####################################################################################################
    # Enable this for Arcade mode                                                                      #
    # Need to re-run the script for each game
    #
    if top != min_y:
        frame_id += 1
        speed = math.floor(math.log(frame_id)**2.4)
        top -= speed
        bottom -= speed
        top = max(top, min_y)
        bottom = max(bottom, min_y + height)

        if top == min_y:
            gui.PAUSE = 0.04
    ####################################################################################################

    # Only capture the region of interest to improve performance
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot_pixels = screenshot.load()

    for i in range(len(keys)):
        percent = (i + 1) / divider
        x = math.floor(width * percent)

        pixel = screenshot_pixels[x, center_y]

        if pixel[1] > 200:
            gui.press(keys[i])
