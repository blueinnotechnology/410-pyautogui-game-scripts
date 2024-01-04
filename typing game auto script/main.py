from PIL import ImageGrab
import pyautogui as gui
import pytesseract

gui.PAUSE = 0.01

change_display_format_box = None

####################################################################################################
#                                Constants for directions                                          #
####################################################################################################
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def find_white(direction: str, start_point: (int, int), screenshot_data) -> int or None:
    '''
    Given a direction, a starting point, and a screenshot, find the first white pixel in that direction.
    If no white pixel is found, return None.
    else return the index of the white pixel of the screenshot in the given direction.
    '''

    start = None
    stop = None
    step = None

    if direction == UP:
        start = start_point[1]
        stop = 0
        step = -1
    elif direction == DOWN:
        start = start_point[1]
        stop = screenshot.height
        step = 1
    elif direction == LEFT:
        start = start_point[0]
        stop = 0
        step = -1
    elif direction == RIGHT:
        start = start_point[0]
        stop = screenshot.width
        step = 1

    if start is None or stop is None or step is None:
        raise Exception(f'Invalid direction: {direction}')

    for i in range(start, stop, step):
        if (direction == LEFT) or (direction == RIGHT):
            pixel = screenshot_data[i, start_point[1]]
        elif (direction == UP) or (direction == DOWN):
            pixel = screenshot_data[start_point[0], i]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        if (direction == UP):
            print(f'i: {i}, r: {r}, g: {g}, b: {b}')

        if r >= 250 and g >= 250 and b >= 250:
            return i

    return None


####################################################################################################
#                                Locate the Instruction text                                       #
####################################################################################################
print('Finding box of "Change Display Format" text')
while change_display_format_box is None:
    try:
        change_display_format_box = gui.locateOnScreen(
            'change_display_format.png')
    except gui.ImageNotFoundException:
        continue
print(f'change_display_format_box: {change_display_format_box}')

####################################################################################################
#                                Take a screenshot                                                 #
####################################################################################################
screenshot = ImageGrab.grab()
screenshot_data = screenshot.load()
screenshot.save('screenshot.png')
print(f'screenshot.size: {screenshot.size}')


####################################################################################################
#                                Spread from Instruction text's sides,                             #
#                                find the position of 1st white pixel                              #
#                                to find the question text area                                    #
####################################################################################################
bottom = change_display_format_box.top
top = find_white(direction=UP,
                 start_point=(change_display_format_box.left,
                              change_display_format_box.top),
                 screenshot_data=screenshot_data)
left = find_white(direction=LEFT,
                  start_point=(change_display_format_box.left,
                               change_display_format_box.top),
                  screenshot_data=screenshot_data)
right = find_white(direction=RIGHT,
                   start_point=(change_display_format_box.left +
                                change_display_format_box.width,
                                change_display_format_box.top),
                   screenshot_data=screenshot_data)
right = find_white(RIGHT, (change_display_format_box.left +
                   change_display_format_box.width, change_display_format_box.top), screenshot_data)
print(f'left: {left}, top: {top}, right: {right}, bottom: {bottom}')


####################################################################################################
#                                Exit if any side not found                                        #
####################################################################################################
if left is None:
    print('Could not find left value')
    exit()
if top is None:
    print('Could not find top value')
    exit()
if right is None:
    print('Could not find right value')
    exit()


####################################################################################################
#                                Screenshot the question text area only                            #
####################################################################################################
FILE_NAME = "game_window.png"
game_window = ImageGrab.grab(bbox=(left, top, right, bottom))
game_window.save(FILE_NAME)
print('Saved game window')


####################################################################################################
#                                Run OCR to get the text                                           #
####################################################################################################
text = pytesseract.image_to_string(FILE_NAME, lang='eng')
text = text.replace('\n', ' ')
print(f'Text: {text}')


####################################################################################################
#                                Click the browser then text field to focus                        #
####################################################################################################
gui.click(x=change_display_format_box.left - 10,
          y=change_display_format_box.top + change_display_format_box.height + 10)
gui.click(x=change_display_format_box.left - 10,
          y=change_display_format_box.top + change_display_format_box.height + 10)


####################################################################################################
#                                Start typing                                                      #
####################################################################################################
# gui.typewrite(text, interval=0.05)
for t in text:
    if t.isupper():
        gui.keyDown('shift')
        gui.press(t)
        gui.keyUp('shift')
    else:
        gui.press(t)
