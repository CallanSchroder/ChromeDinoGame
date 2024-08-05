from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np


class coordinates():
    replaybutton = (1920, 424)
    dinasaur = (1636, 449)


def restartGame():
    pyautogui.click(coordinates.replaybutton)


def press_space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    time.sleep(0.10)
    pyautogui.keyUp('space')


def imageGrab():
    box = (coordinates.dinasaur[0] + 100, coordinates.dinasaur[1] - 40,
           coordinates.dinasaur[0] + 120, coordinates.dinasaur[1])
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


restartGame()
while True:
    if (imageGrab() != 1047):
        press_space()
        time.sleep(0.1)