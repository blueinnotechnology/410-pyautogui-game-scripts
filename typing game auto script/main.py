from PIL import ImageGrab
import pyautogui as gui
import pytesseract

gui.PAUSE = 0.01

change_display_format_box = None
type_this_box = None

while change_display_format_box is None:
    try:
        change_display_format_box = gui.locateOnScreen('change_display_format.png')
    except gui.ImageNotFoundException:
        continue

while type_this_box is None:
    try:
        type_this_box = gui.locateOnScreen('type_this.png')
    except gui.ImageNotFoundException:
        continue

print(f'change_display_format_box: {change_display_format_box}')

LEFT = int(type_this_box.left + type_this_box.width * 0.75)
RIGHT = change_display_format_box.left + change_display_format_box.width
TOP = type_this_box.top + type_this_box.height + 10
BOTTOM = change_display_format_box.top

FILE_NAME = "game_window.png"
game_window = ImageGrab.grab(bbox=(LEFT, TOP, RIGHT, BOTTOM))
game_window.save(FILE_NAME)
print('Saved game window')

text = pytesseract.image_to_string(FILE_NAME, lang='eng')
text = text.replace('\n', ' ')
print(f'Text: {text}')

gui.click(x=change_display_format_box.left - 10, y=change_display_format_box.top + change_display_format_box.height + 10)
gui.click(x=change_display_format_box.left - 10, y=change_display_format_box.top + change_display_format_box.height + 10)

# print('Starting in 2 seconds...')
# time.sleep(2)

# gui.typewrite(text, interval=0.05)
for t in text:
    if t.isupper():
        gui.keyDown('shift')
        gui.press(t)
        gui.keyUp('shift')
    else:
        gui.press(t)

