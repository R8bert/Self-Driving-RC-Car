# 🚗 Self-Driving RC Car with 3D Printing and Modeling

This project is a self-driving RC car I designed and built from scratch using a **Raspberry Pi**, **Arduino**, and a bunch of sensors.  
It combines **3D modeling**, **3D printing**, **embedded programming**, and **computer vision** to create a small-scale autonomous vehicle that can drive and avoid obstacles on its own.

---

## 🧠 Project Overview

The main goal was to build a car that could navigate by itself using camera input and sensors — no manual control needed.  
Along the way, I designed and printed the body, wired up the electronics, and wrote all the software to handle movement, obstacle detection, and remote control through a simple web interface.

I later presented it at a local maker fair, where it got great feedback from visitors and other hobbyists.

---

## ⚙️ What I Built

- **3D Printed Body and Parts**  
  Designed the chassis and components using CAD software and printed them on a desktop 3D printer.

- **Autonomous Driving**  
  Used computer vision and basic machine learning to follow paths and detect obstacles.

- **Sensor Integration**  
  Combined data from ultrasonic sensors, a camera module, and IR sensors to make navigation decisions.

- **Raspberry Pi + Arduino Setup**  
  The Raspberry Pi runs the high-level vision and control code, while the Arduino handles low-level motor and sensor control.

- **Web Control Interface**  
  Built a lightweight web app (Flask) that lets you control the car manually and see live feedback.

- **Real-World Testing**  
  Tested the car indoors and outdoors, tuning the algorithms for different lighting and surface conditions.

---

## 🛠️ Hardware Used

| Component | Description |
|------------|-------------|
| Raspberry Pi 4 | Runs computer vision and main logic |
| Arduino Uno | Handles motor and sensor control |
| Pi Camera | Provides live video feed |
| Ultrasonic Sensors | Detects obstacles and helps with navigation |
| DC Motors + Driver | Powers the wheels |
| 3D Printed Chassis | Custom-designed lightweight frame |
| Battery Pack | Provides portable power |

---

## 💻 Software Stack

| Type | Tools |
|------|-------|
| Programming | Python, C++ |
| Frameworks | OpenCV, TensorFlow, Flask |
| Microcontroller | Arduino IDE |
| 3D Modeling | Fusion 360 / SolidWorks |
| OS | Raspbian |

---

## 🧩 System Overview

Here’s how the system fits together — the Pi and Arduino communicate over serial, with the Pi handling the “brains” and the Arduino handling the “muscles”:

![car sys](https://user-images.githubusercontent.com/61593351/234959681-5ce77418-8f70-4f21-b785-7d2b3a26c022.jpg)
![car sys2](https://user-images.githubusercontent.com/61593351/234959682-025a8b70-5407-4e3d-9fa3-17e317b8f39d.jpg)
![car sys3](https://user-images.githubusercontent.com/61593351/234959686-143efceb-cea2-4997-ac95-3dcaf4f4fe52.jpg)
![car sys4](https://user-images.githubusercontent.com/61593351/234959676-9867c123-73ad-4f39-a5ed-081cd3dfec8d.jpg)

---

## 🧱 Design and Build Photos

### 3D Modeling & Printing
![Image](https://user-images.githubusercontent.com/61593351/234954546-81d05d14-f48e-445b-944e-dd89eae37795.png)
![Image](https://user-images.githubusercontent.com/61593351/234954666-75bada8b-ab2f-4ef3-98a2-f47a665b28fd.png)
![Image](https://user-images.githubusercontent.com/61593351/234954703-5c1405e0-cd41-4b11-9809-0a57ad07e7ec.png)
![Image](https://user-images.githubusercontent.com/61593351/234954767-99e8d6a2-087d-4da6-a888-1c65e8f8b339.png)

### Assembly and Final Build
![image](https://user-images.githubusercontent.com/61593351/234965234-1612fecd-6c52-463c-81a3-a1c519d5ea66.png)
![image](https://user-images.githubusercontent.com/61593351/234964802-b0f567b3-ed56-4c2c-b23f-d97c73a40e41.png)
![image](https://user-images.githubusercontent.com/61593351/234964835-19576ef3-2d48-4e26-b0c3-4a4c687aa222.png)
![image](https://user-images.githubusercontent.com/61593351/234964896-308baf55-2f78-4604-846b-6920a8dfa9ee.png)

---

## 🎯 Results & Learnings

- The car was able to drive autonomously in a test track using vision and sensor data  
- The web interface made it easy to switch between manual and autonomous modes  
- Learned a ton about integrating hardware, software, and mechanical design  
- Got hands-on experience with:
  - Computer Vision (OpenCV)
  - Embedded Systems (Raspberry Pi & Arduino)
  - 3D Design and Printing
  - Python + C++ programming

---

## 🔧 Things to Improve Next

- Add SLAM or more advanced mapping
- Use LiDAR or depth cameras for better obstacle detection
- Improve real-time object detection speed
- Build a nicer web dashboard with live telemetry and camera feed

