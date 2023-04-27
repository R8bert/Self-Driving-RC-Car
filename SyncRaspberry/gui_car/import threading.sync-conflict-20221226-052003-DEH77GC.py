import threading
from random import randint
import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import RPi.GPIO as GPIO






class CarGUI:
    GPIO.setmode(GPIO.BCM)

    def CreateBackground(self):
        print("Create background")
        self.image_back = PhotoImage(
        file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/image_1.png"))
        self.back = self.canvas.create_image(
        320.0,
        321.0,
        image=self.image_back
        )
        self.image_car = PhotoImage(
        file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/image_4.png"))
        self.car = self.canvas.create_image(
        320.0,
        401.0,
        image=self.image_car
        )


        #Create the buttons
        self.button_image_1 = PhotoImage(
        file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/button_1.png"))
        self.button_1 = Button(
        image=self.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: threading.Thread(target=self.TurnOnParking, args=()).start(),
        relief="flat"
        )
        print("-----SE PORNESTE ------")
        self.button_1.place(
        x=724.0,
        y=185.0,
        width=100.0,
        height=100.0
        )


        self.button_image_2 = PhotoImage(
        file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/button_2.png"))
        self.button_2 = Button(
        image=self.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
        )
        self.button_2.place(
        x=724.0,
        y=49.0,
        width=100.0,
        height=100.0
        )

    def TurnOnParking(self):
        if self.ParkingStatus == True:
            self.ParkingStatus = False
            # Create the buttons

            self.button_image_1 = PhotoImage(
                file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/button_1_false.png"))
            self.button_1 = Button(
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: threading.Thread(target=self.TurnOnParking, args=()).start(),
                relief="flat"
            )
            print("-----SE PORNESTE ------")
            self.button_1.place(
                x=724.0,
                y=185.0,
                width=100.0,
                height=100.0
            )

        else:
            self.ParkingStatus = True
            threading.Thread(target=self.CalculateDistance, args=()).start()
            # Create the buttons
            self.button_image_1 = PhotoImage(
                file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/button_1_false.png"))
            self.button_1 = Button(
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: threading.Thread(target=self.TurnOnParking, args=()).start(),
                relief="flat"
            )
            print("-----SE PORNESTE ------")
            self.button_1.place(
                x=724.0,
                y=185.0,
                width=100.0,
                height=100.0
            )
        # while self.ParkingStatus == True:
        #     self.ParkingStatus = False
        #     return
        #     # break
        # while self.ParkingStatus == False:
        #     self.ParkingStatus = True
        #     threading.Thread(target=self.CalculateDistance, args=()).start()
        #     return






    def CalculateDistance(self):
        # threading.Thread(target=self.CheckColor, args=()).start() 
        print("Calculate Distance")
        while self.ParkingStatus == True:
            #
            GPIO.output(self.TRIG, False)
            print("Waiting For Sensor To Settle")
            time.sleep(2)

            GPIO.output(self.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIG, False)

            while GPIO.input(self.ECHO) == 0:
                self.pulse_start = time.time()

            while GPIO.input(self.ECHO) == 1:
                self.pulse_end = time.time()

            self.pulse_duration = self.pulse_end - self.pulse_start

            self.distance = self.pulse_duration * 17150

            self.distance = round(self.distance, 2)
            # distancetext = str(distance)
            print("Distance: ", self.distance, "cm")
            # print(distancetext)
            # distancetext = str(distance)
            # root.update()




            #
            print("distance: " + str(self.distance))
            if self.distance > 15:
                self.red = False
                self.yellow = False
                self.green = True
            elif self.distance < 10 and self.distance > 5:
                self.red = False
                self.yellow = True
                self.green = False
            elif self.distance < 5:
                self.red = True
                self.yellow = False
                self.green = False

            print("red: " + str(self.red))
            print("yellow: " + str(self.yellow))
            print("green: " + str(self.green))
            if self.ParkingStatus == False:
                self.image_image_3.destroy()
                break
            time.sleep(1)


    def CheckColor(self):
        while True:
            if self.red == True:
                print("RED TRUE")
                self.image_image_4 = PhotoImage(
                file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/image_5.png"))
                self.image_3 = self.canvas.create_image(
                320.0,
                76.0,   
                image=self.image_image_4
                )
            elif self.yellow == True:
                print("YELLOW TRUE")
                self.image_image_4 = PhotoImage(
                file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/image_2.png"))
                self.image_3 = self.canvas.create_image(
                319.0,
                108.0,
                image=self.image_image_4
                )
            elif self.green == True:
                print("GREEN TRUE")
                self.image_image_4 = PhotoImage(
                file=("/home/pi/Desktop/SyncMSI/gui_car/build/assets/frame0/image_3.png"))
                self.image_3 = self.canvas.create_image(
                319.0,
                141.0,
                image=self.image_image_4
                )
            time.sleep(1)



    def __init__(self):

        print("CarGUI Interface 2.0 - Initialization")
        self.ParkingStatus = False
        self.red = False
        self.yellow = False
        self.green = False
        self.distance = 0
        self.window = Tk()
        self.window.geometry("905x641")
        self.window.configure(bg = "#FFFFFF")
        self.canvas = Canvas(
        self.window,
        bg = "#FFFFFF",
        height = 650,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
        #
        self.TRIG = 23
        self.ECHO = 24
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

        #




        threading.Thread(target=self.CheckColor, args=()).start() 
        threading.Thread(target=self.CreateBackground, args=()).start() 
        # threading.Thread(target=self.CalculateDistance, args=()).start() 
        self.canvas.place(x = 0, y = 0)
        self.window.resizable(False, False)
        self.window.mainloop()
        # self.CreateBackground()



CarGUI()
