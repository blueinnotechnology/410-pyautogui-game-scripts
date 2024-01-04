# Don't Touch the Red Auto Script

A bot that plays [Don't Touch the Red](https://www.addictinggames.com/clicker/dont-touch-the-red?ref=hackernoon.com#url).

## How to use

1. Go to [Don't Touch the Red](https://www.addictinggames.com/clicker/dont-touch-the-red?ref=hackernoon.com#url) (preferably in split screen).
2. Enter any game mode.
3. Record the coordinates of the region of interest (ROI) by running `get_mouse.py` and set the values of `left`, `right`, `top`, and `bottom` in `main.py`.
   ![ROI](./region_of_interest.png)
4. If entered "Arcade Mode", un-comment the part of the code that surrounded with `#` in `main.py`.
5. Run `main.py`.

## Working Principle

1. The script will take a screenshot of the ROI every cycle in a `while` loop.

2. The script will then divide the ROI into 4 equal parts and check if the color of the pixel in the middle of each part is green.

3. If the color of the pixel in the middle of the part is green, the script will press the corresponding key.

4. For "Arcade Mode", the ROI will gradually move up to the top of the game screen. This is to deal with the increasing falling speed of the blocks.
