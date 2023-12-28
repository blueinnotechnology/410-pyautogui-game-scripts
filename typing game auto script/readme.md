# TypeRacer Bot

A bot that plays [TypeRacer](https://play.typeracer.com/).

## How to use

1. Go to [TypeRacer](https://play.typeracer.com/) (preferably in split screen).
2. Enter `Practice Mode`.
3. Screenshot the `change display format` button and save it as `change_display_format.png`.

   ![change_display_format](change_display_format.png)
4. Screenshot the `Type This` element and save it as `type_this.png`.

   ![type_this](type_this.png)
5. Run the script (`main.py`).

## Working Principle

1. The script finds the location of the `change display format` button.
2. The script finds the location of the `Type This` element.
3. Base on the locations of these two elements, the script calculates the location of the text box.
4. The script takes a screenshot of the text box and saves it as `game_window.png`
5. The script uses [pytesseract](https://pypi.org/project/pytesseract/) to read the text in the text box.
6. The script uses [pyautogui](https://pypi.org/project/PyAutoGUI/) to type the text in the text box.
