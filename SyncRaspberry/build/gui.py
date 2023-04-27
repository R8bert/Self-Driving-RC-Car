import threading
from tkinter import *
import time
from random import randint
import RPi.GPIO as GPIO
import time
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Desktop/SyncMSI/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

distanceI = "Dist"



# Initialize a new window
root=Tk()
root.geometry('500x400')
# A function that interrupts for five seconds
def five_seconds():
    # time.sleep(5)
    while True:
        
        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150
        
        distance = round(distance, 2)
        
        print("Distance: ",distance,"cm")
        distanceI = str(distance)

    label.config(text=distance)
# A function that generates a random number
def random_numbers():
    rand_label.config(text=f'The random number is: {randint(1,100)}')


canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 720,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=629.0,
    y=206.0,
    width=125.0,
    height=125.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=629.0,
    y=52.0,
    width=125.0,
    height=125.0
)

canvas.create_rectangle(
    13.0,
    52.0,
    275.0,
    146.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    45.0,
    75.0,
    anchor="nw",
    text= str(distanceI),
    fill="#000000",
    font=("Inter", 40 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    691.0,
    268.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    400.0,
    268.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    692.0,
    114.0,
    image=image_image_3
)









label=Label(root,text='Hello there!')
label.pack(pady=20)
# A button that calls a function
button1=Button(root,text='5 seconds',command=threading.Thread(target=five_seconds).start())
button1.pack(pady=20)

button2=Button(root,text='pick a random number',command=random_numbers)
button2.pack(pady=20)
rand_label=Label(root,text='')
rand_label.pack(pady=20)
root.mainloop()