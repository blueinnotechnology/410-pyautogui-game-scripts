import os
import json
import numpy as np
from mss import mss
import pyautogui
from skimage.metrics import structural_similarity as ssim


pyautogui.PAUSE = 0


def remap_zone():
    try:
        box = pyautogui.locateOnScreen('zone.png')
        print('zone.png found: ', box)
        
        # Store zone in json file
        with open('zone.json', 'w') as f:
            pixel_ratio = pyautogui.screenshot().size[0] / pyautogui.size().width
            zone = {
                'top': int(box.top / pixel_ratio),
                'left': int(box.left / pixel_ratio),
                'width': int(box.width / pixel_ratio),
                'height': int(box.height / pixel_ratio),
            }
            json.dump(zone, f)

    except pyautogui.ImageNotFoundException:
        print('zone.png not found or not found in the screen')
        print('Exiting...')
        exit()
    

def check_similarity(target_img, base_img):
    s = ssim(target_img, base_img, multichannel=True, channel_axis=2)
    return (s + 1) / 2


def main():
    # Check if zone.json exists
    file_exists = os.path.exists('zone.json')
    if not file_exists:
        remap_zone()
    elif input('Remap Zone? (Y/N)') == 'Y':
        remap_zone()
    
    # Read zone from json file
    with open('zone.json', 'r') as f:
        zone = json.load(f)
        
    
    # Define keys
    keys = ['s', 'd', 'f', 'space', 'j', 'k', 'l']
    screen_captor = mss()
    initial_zone_img = screen_captor.grab(zone)
    initial_img_np = np.array(initial_zone_img)
    initial_img_np_list = np.array_split(initial_img_np, len(keys), axis=1)
    
    
    # Initialize pressed keys
    pressed_keys = {}
    for k in keys:
        pressed_keys.update({k: False})

    
    print('You may now start the game')
    
    
    # Start watching the screen
    while True:
        img = screen_captor.grab(zone)
        img_np = np.array(img)
        game_img_np_list = np.array_split(img_np, len(keys), axis=1)
        
        for i in range(len(keys)):
            similarity = check_similarity(initial_img_np_list[i], game_img_np_list[i])
            # print(keys[i], similarity)
            if similarity < 0.8:
                pyautogui.keyDown(keys[i])
                pressed_keys.update({keys[i]: True})
            elif pressed_keys[keys[i]]:
                pyautogui.keyUp(keys[i])
                pressed_keys.update({keys[i]: False})


main()