from time import sleep
from pyautogui import press
import random
import threading


class Flask:
    running = False

    flasks = []

    @classmethod
    def toggle(cls):
        cls.running = not cls.running

    def __init__(self, bind, cd):
        self.bind = bind
        self.cd = cd
        Flask.flasks.append(self)

    def use(self):
        while True:
            if Flask.running:
                press(str(self.bind))
                sleep(random.uniform(self.cd - 0.2, self.cd))
            else:
                sleep(0.1)

    def create_thread(self):
        flasking = threading.Thread(target=self.use)
        flasking.start()
