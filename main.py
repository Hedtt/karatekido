from PIL import ImageGrab, Image
import cv2
import numpy as np
import pyautogui
import time


def capture_screen(area):
    return np.array(ImageGrab.grab(bbox=area))[0][0]


if __name__ == '__main__':
    # region variables
    r_position = [1027, 712]
    l_position = [890, 712]
    width = 1
    heigth = 1
    l_area = (l_position[0], l_position[1], l_position[0] + width, l_position[1] + heigth)
    r_area = (r_position[0], r_position[1], r_position[0] + width, r_position[1] + heigth)
    press_left = True
    press_right = not press_left
    l_pixel = capture_screen(l_area)
    r_pixel = capture_screen(r_area)
    # endregion

    while True:
        new_l_pixel = capture_screen(l_area)
        new_r_pixel = capture_screen(r_area)

        if (new_l_pixel == [24, 26, 27]).all() or (new_r_pixel == [24, 26, 27]).all():
            time.sleep(0.2)
            # print('waiting for start')
            continue

        # print(new_l_pixel, press_left, new_r_pixel, press_right)

        if (new_l_pixel != np.array([255, 142, 92])).all() and press_left:
            press_left = False
            press_right = True
            # print('change')

        elif (new_r_pixel != np.array([107, 112, 78])).all() and press_right:
            press_right = False
            press_left = True
            # print('change')
        # else:
        #     print('error', new_l_pixel, new_r_pixel)
        #     # quit()

        if press_left:
            pyautogui.press('left')
            # print(l_pixel, new_l_pixel, 'l')
            # print('pressed left')
        else:
            pyautogui.press('right')
            # print(r_pixel, new_r_pixel, 'r')
            # print('pressed right')

        # print(l_pixel, new_l_pixel, r_pixel, new_l_pixel)
        l_pixel = new_l_pixel
        r_pixel = new_r_pixel
        time.sleep(0.05)
