from PIL import Image, ImageGrab
import os
import time
import mouse
import keyboard as kb
import win32con
import win32api


def screenGrab():
    box = (1920,0,2920,1080)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snaffffffffffffp__' + str(int(time.time())) +
            '.png',
            'PNG')


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1117, 782)
    time.sleep(.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1117, 782)
    print("Click.")


def main():

    # while True:
    # #     time.sleep(5)
    # #     screenGrab()
    # screenGrab()
    while True:
        if kb.is_pressed('s'):
            while True:
                if kb.is_pressed('e'):
                    print("STOP----------------------------")
                    break
                print("Click.")
                # time.sleep(0.0001)
                mouse.double_click(button='left')






if __name__ == '__main__':
    main()