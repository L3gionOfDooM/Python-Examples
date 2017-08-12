#######################Python Clock#######################

#Import Modules
import os
import time
from datetime import datetime as dt

#Loop for getting time updates.
def timeUpdate():
    time.sleep(1)
    os.system('cls')
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    timeUpdate()

#Call for Loop
timeUpdate()
