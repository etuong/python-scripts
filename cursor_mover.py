# At work, our communication (e.g Microsoft Teams) status does not stay green if we idle.
# This script automatically moves the cursor so it appears like we are working

import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)
