import pyautogui
from PIL import ImageGrab, ImageChops
import cv2 as cv
import numpy as np

pyautogui.PAUSE = 0

upper_area = {
    "left": 1330,
    "top": 315,
    "width": 80,
    "height": 40
}

lower_area = {
    "left": 1350,
    "top": 330,
    "width": 80,
    "height": 30
}


def find_similarity(base_img, img):
    # Calculate the difference between the two images
    diff = ImageChops.difference(base_img, img)

    # Get the bounding box of the non-zero regions in the difference image
    bbox = diff.getbbox()

    # If the bounding box is None, the images are identical
    if bbox is None:
        similarity = 100.0
    else:
        # Calculate the percentage similarity
        total_pixels = diff.size[0] * diff.size[1]
        changed_pixels = (diff.size[0] - bbox[0]) * (diff.size[1] - bbox[1])
        similarity = (total_pixels - changed_pixels) / total_pixels * 100

    return similarity


def screenshot():
    screen_img = ImageGrab.grab().convert('L')
    screen_img_data = screen_img.load()
    for x in range(lower_area["left"], lower_area["left"] + lower_area["width"]):
        for y in range(lower_area["top"], lower_area["top"] + lower_area["height"]):
            screen_img_data[x, y] = 0
    cv.imshow('lower', np.array(screen_img))
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()


if __name__ == "__main__":

    lower_bounding_box = (lower_area["left"],
                          lower_area["top"],
                          lower_area["left"] + lower_area["width"],
                          lower_area["top"] + lower_area["height"])

    upper_bounding_box = (upper_area["left"],
                          upper_area["top"],
                          upper_area["left"] + upper_area["width"],
                          upper_area["top"] + upper_area["height"])

    empty_lower_img = ImageGrab.grab(bbox=lower_bounding_box).convert('L')
    empty_lower_img_np = np.array(empty_lower_img)

    empty_upper_img = ImageGrab.grab(bbox=upper_bounding_box).convert('L')
    empty_upper_img_np = np.array(empty_upper_img)

    while True:

        screenshot()

        # capture image in black & white format
        lower_image = ImageGrab.grab(bbox=lower_bounding_box).convert('L')

        # Calculate the difference between the two images
        lower_similarity = find_similarity(empty_lower_img, lower_image)
        if (lower_similarity < 50):
            pyautogui.keyUp('down')
            pyautogui.press('space')
        else:
            upper_image = ImageGrab.grab(bbox=upper_bounding_box).convert('L')
            upper_similarity = find_similarity(empty_upper_img, upper_image)
            if (upper_similarity < 85):
                pyautogui.hold('down')
