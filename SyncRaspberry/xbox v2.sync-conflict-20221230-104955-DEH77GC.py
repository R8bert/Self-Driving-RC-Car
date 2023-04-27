import threading
from random import randint
import time
from tkinter import *
from pathlib import Path
import RPi.GPIO as GPIO
from evdev import *
import pigpio
import serial

pi = pigpio.pi()
ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
ser.flush()
gamepad = InputDevice('/dev/input/event0')
print(gamepad)
buttons = {
    308: "Y",
    305: "B",
    304: "A",
    307: "X",
    311: "RB",
    310: "LB",
    172: "Xbox",
    158: "View",
    315: "Menu",
    318: "Joy1",
    318: "Joy2"
}

lt = 10
rt = 9

joy1_y = 1
joy1_x = 0
joy1_position = [0, 0]

joy2_y = 5
joy2_x = 2
joy2_position = [0, 0]

directionnal_button_x = 16
directionnal_button_y = 17

holded_button = 0
ltrig = False
rtrig = False



class XboxContol:

    def buttonCheck(self):
        print("buttonCheck")
        for event in gamepad.read_loop():
            # BUTTON
            if event.type == ecodes.EV_KEY:
                val = int(event.value)

                if val == 1:
                    print(buttons[int(event.code)] + " pressed")
                elif val == 0:
                    print(buttons[int(event.code)] + " released")
                else:
                    print("else")
                    print(buttons[int(event.code)] + " value: " + str(event.value))

            # JOYSTICK
            elif event.type == ecodes.EV_ABS:
                # JOY 1
                if event.code == joy1_x:
                    joy1_position[0] = int(event.value)
                #             print("JOY 1: X " + str(joy1_position[0]) + " Y " + str(joy1_position[1]))
                    self.initLeftMushroomL = joy1_position[0]
                    if self.initLeftMushroomL < 4000:
                        pi.set_servo_pulsewidth(17, 1200)
                    else:
                        pi.set_servo_pulsewidth(17, 900)




                elif event.code == joy1_y:
                    joy1_position[1] = int(event.value)
                #             print("JOY 1: X " + str(joy1_position[0]) + " Y " + str(joy1_position[1]))

                    self.initLeftMushroomR = joy1_position[1]
                    if self.initLeftMushroomR > 2000:
                        pi.set_servo_pulsewidth(17, 600)
                    else:
                        pi.set_servo_pulsewidth(17, 900)
                # JOY 2
                elif event.code == joy2_x:
                    joy2_position[0] = int(event.value)
                    print("JOY 2: X " + str(joy2_position[0]) + " Y " + str(joy2_position[1]))



                if event.code == joy2_y:
                    joy2_position[1] = int(event.value)
                #             print("JOY 2: X " + str(joy2_position[0]) + " Y " + str(joy2_position[1]))

                # DIRECTIONAL BUTTON AXIS Y
                elif event.code == directionnal_button_y:
                    pos = int(str(event.value).replace("L", ""))
                    if pos > 0:
                        print("Down pressed")
                        holded_button = "Down"

                        self.CamLeft = True
                        if self.CamLeft == True:
                            threading.Thread(target=self.CamLeftTrue, args=()).start()

                    elif pos < 0:
                        print("Up pressed")
                        holded_button = "Up"
                        self.CamRight = True
                        if self.CamRight == True:
                            threading.Thread(target=self.CamRightTrue, args=()).start()
                    elif pos == 0:
                        print(holded_button + " released")
                        self.CamLeft = False
                        self.CamRight = False

                # DIRECTIONAL BUTTON AXIS X
                elif event.code == directionnal_button_x:
                    pos = int(str(event.value).replace("L", ""))
                    if pos > 0:
                        print("Right pressed")
                        holded_button = "Right"
                        print('Right')
                        pi.set_servo_pulsewidth(17, 1200)
                    elif pos < 0:
                        print("Left pressed")
                        holded_button = "Left"
                        print('Left')
                        pi.set_servo_pulsewidth(17, 600)
                    elif pos == 0:
                        print(holded_button + " released")
                        print('No key pressed');
                        pi.set_servo_pulsewidth(17, 900);

                elif event.code == lt:
                    ltrig = True
                    print("LT pressed at " + str(event.value))
                    ltrigvalue = event.value
                    if ltrigvalue == 1023 and ltrig == True:
                        print("Car goes forward")
                        ser.write(b"f\n")
                    else:
                        ser.write(b"s\n")
                        ltrig = False
                        ltrigvalue = 0

                elif event.code == rt:
                    rtrig = True
                    print("RT pressed at " + str(event.value))
                    rtrigvalue = event.value
                    if rtrigvalue == 1023 and rtrig == True:
                        print("Car goes backwords")
                        ser.write(b"b\n")
                    else:
                        ser.write(b"s\n")
                        rtrig = False
                        rtrigvalue = 0



    def CamLeftTrue(self):
        while self.CamLeft == True:
            actial = pi.get_servo_pulsewidth(25)
            if actial >= self.servoMin:
                pi.set_servo_pulsewidth(25, actial + 1)
                time.sleep(0.0001)
                if actial == self.servoMaxL or actial == self.servoMaxR:
                    break
#             else:
#                 break

    def CamRightTrue(self):
        while self.CamRight == True:
            actial = pi.get_servo_pulsewidth(25)
            if actial >= self.servoMin:
                pi.set_servo_pulsewidth(25, actial - 1)
                time.sleep(0.0001)
#                 print(actial)
                if actial == self.servoMaxL or actial == self.servoMaxR:
                    break
#             else:
#                 break



    def __init__(self):
        print("XboxContol init")
        # self.gamepad = InputDevice('/dev/input/event0')
        threading.Thread(target=self.buttonCheck, args=()).start()
        self.servoMid = 1300
        self.servoMin = 600
        self.servoMax = 1600
        self.servoMaxL = 2250
        self.servoMaxR = 605


        self.initLeftMushroomL = 0
        self.initLeftMushroomR = 0
        
        pi.set_servo_pulsewidth(25, self.servoMid);
        self.CamLeft = False
        self.CamRight = False




XboxContol()
