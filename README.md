# 🚗 Self-Driving RC Car

Hey everyone! I'm super excited to share a project I've been pouring a ton of time into: a fully self-driving RC car that I designed and built completely from scratch.

This project was a massive learning experience for me, mixing pretty much everything I love: **3D modeling**, **3D printing**, **embedded programming**, and **computer vision**.

---

## 🧠 The Idea

My main goal was to build a small-scale car that could *actually* drive itself. No manual remote control needed. I wanted it to use a camera and a bunch of sensors to navigate a path and, most importantly, not smack into my walls.

Along the way, I ended up designing and 3D-printing the entire body, wiring up all the electronics from scratch, and writing all the code to make it move.

I even got to show it off at a local maker fair recently, which was an awesome experience. It got some great feedback, which made all the late-night troubleshooting worth it!

---

## What Does It Do?

It started as just an idea, but it ended up with a bunch of features I'm really proud of:

* **Custom 3D-Printed Body:** I designed the whole chassis, wheel mounts, and sensor brackets in CAD (I used a mix of Fusion 360 and SolidWorks) and printed everything on my desktop 3D printer.
* **Real Autonomous Driving:** This was the hard part! I'm using OpenCV and a little bit of TensorFlow to process the camera feed. This lets the car follow lines on the floor and spot obstacles in its path.
* **Sensor Fusion:** To make good decisions, the car can't just "see." I also added ultrasonic sensors and IR sensors to help it measure distances and avoid things the camera might miss.
* **A "Split-Brain" System:** I'm using a **Raspberry Pi** as the high-level "brain" to run the computer vision and make the big decisions (like "turn left!"). The Pi then sends simple commands to an **Arduino**, which acts as the "muscle" to handle the low-level, real-time control of the motors and sensors.
* **A Web Control Panel:** For testing (and just for fun), I built a simple web app using Flask. It lets me manually control the car from my phone or laptop and see a live stream from the car's camera.

---

## How It All Fits Together

The "split-brain" approach with the Pi and Arduino is the core of the whole system.

The **Raspberry Pi 4** runs the heavy-duty Python scripts. It captures the video, runs it through OpenCV to find lanes or obstacles, and then decides the best course of action.

Once it makes a decision, it sends a simple command (like `forward`, `stop`, or `turn_left`) over a serial connection to the **Arduino Uno**. The Arduino, running a much simpler C++ script, is dedicated to one job: taking those commands and translating them into the correct electrical signals for the motor driver. It also constantly pings the ultrasonic sensors and can react instantly if something is *right* in front of the car, faster than the Pi could.

Here are a couple of diagrams I drew up to plan it all out:

![System architecture diagram 1](https://user-images.githubusercontent.com/61593351/234959681-5ce77418-8f70-4f21-b785-7d2b3a26c022.jpg)
![System architecture diagram 2](https://user-images.githubusercontent.com/61593351/234959682-025a8b70-5407-4e3d-9fa3-17e317b8f39d.jpg)
![System architecture diagram 3](https://user-images.githubusercontent.com/61593351/234959686-143efceb-cea2-4997-ac95-3dcaf4f4fe52.jpg)
![System architecture diagram 4](https://user-images.githubusercontent.com/61593351/234959676-9867c123-73ad-4f39-a5ed-081cd3dfec8d.jpg)

---

## The "Tech"

For anyone curious, here's a quick breakdown of the main parts and software I used.

### The Hardware Guts
| Component | What I Used It For |
|------------|-------------|
| Raspberry Pi 4 | The "brains" — runs computer vision & main logic |
| Arduino Uno | The "muscles" — handles motors & sensors |
| Pi Camera | The "eyes" — provides the live video feed |
| Ultrasonic Sensors | Detects obstacles (like walls) |
| DC Motors + Driver | Powers the wheels |
| 3D Printed Chassis | My custom-designed frame |
| Battery Pack | To make it all portable! |

### The Software & Tools
| Type | Tools I Used |
|------|-------|
| Programming | Python (for the Pi) and C++ (for the Arduino) |
| Frameworks | OpenCV, TensorFlow, Flask |
| Microcontroller | Arduino IDE |
| 3D Modeling | Fusion 360 / SolidWorks |
| OS | Raspbian (now Raspberry Pi OS) |

---

## The Build Process in Pictures

Of course, no project post is complete without photos! Here’s a look at how it went from a digital model to a real, working car.

### 3D Modeling & Printing
Here are some renders of the chassis and parts right out of the CAD software.

![CAD model 1](https://user-images.githubusercontent.com/61593351/234954546-81d05d14-f48e-445b-944e-dd89eae37795.png)
![CAD model 2](https://user-images.githubusercontent.com/61593351/234954666-75bada8b-ab2f-4ef3-98a2-f47a665b28fd.png)
![CAD model 3](https://user-images.githubusercontent.com/61593351/234954703-5c1405e0-cd41-4b11-9809-0a57ad07e7ec.png)
![CAD model 4](https://user-images.githubusercontent.com/61593351/234954767-99e8d6a2-087d-4da6-a888-1c65e8f8b339.png)

### Assembly and Final Build
And here's the fun part—putting it all together. It took a *lot* of trial and error to get the wiring clean and make sure everything fit inside the printed chassis.

![Assembly photo 1](https://user-images.githubusercontent.com/61593351/234965234-1612fecd-6c52-463c-81a3-a1c519d5ea66.png)
![Assembly photo 2](https://user-images.githubusercontent.com/61593351/234964802-b0f567b3-ed56-4c2c-b23f-d97c73a40e41.png)
![Assembly photo 3](https://user-images.githubusercontent.com/61593351/234964835-19576ef3-2d48-4e26-b0c3-4a4c687aa222.png)
![Assembly photo 4](https://user-images.githubusercontent.com/61593351/234964896-308baf55-2f78-4604-846b-6920a8dfa9ee.png)

---

This was one of the most challenging and rewarding projects I've ever done. Seeing it finally drive across the room all by itself was an incredible feeling.

Thanks for checking it out! Let me know what you think.
