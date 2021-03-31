import pyautogui as pg

class functions():

    brightness='0%'
    contrast = '0%'

    def shutdown(self):
        print("shutdown button pressed")

    def restart(self):
        print("restart button pressed")
        pg.press('winleft')

    def invertImg(self):
        print(" Image inverted")
        pg.press('space')

    def brightness_percentage(self):

        return '100%'
        