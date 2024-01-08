from picozero import Pot # Pot is short for Potentiometer
from time import sleep

dial = Pot(0) # Connected to pin A0 (GP_26)

while True:
    print(dial.value)
    sleep(0.1) # slow down the output