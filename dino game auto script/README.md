# Auto Script (Chrome Dino Game)

This project is a simple script/prototype that plays the Chrome Dino Game. It uses the Python Imaging Library (PIL) to capture the screen and uses the pyautogui library to press the space bar.

## Mac

Requirements:

- Need to allow VS Code for screen record (Require Admin's permission, some students will need to ask parents).

- Need to allow VS Code for accessibility control of auto mouse click & key press (Require Admin's permission).

## How to Run

1. Preferably, split the screen with VS Code and [Chrome Dino Game](https://chromedino.com/).
2. Start the game.
3. Return to VS Code and run the script (The game should pause when focus is lost).
4. Return and click the game.

## How it Works

1. The script mainly focuses on the area in front of the dino.
2. The area is divided into two parts, the upper and lower part.
3. The upper part is used to detect birds and the lower part is used to detect cactuses.
4. Update the script to change the area of detection.

    ```python
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
    ```

5. Enable the `screenshot()` function to see/adjust the area of detection.

    ```python
    if __name__ == "__main__":
        ...

        while True:

            # screenshot() # ⬅️ enable this function

            # capture image in black & white format
            lower_image = ImageGrab.grab(bbox=lower_bounding_box).convert('L')
            ...
    ```
