import pyautogui as pg

class functions():
    def shutdown(self):
        print("shutdown button pressed")

    def restart(self):
        print("restart button pressed")
        pg.press('winleft')

    def invertImg(self):
        print(" Image inverted")
        pg.press('space')