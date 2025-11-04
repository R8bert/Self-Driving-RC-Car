# Project: 3D-Printed Autonomous RC Vehicle

This project details the design, fabrication, and implementation of a small-scale, self-driving RC car. The vehicle integrates **3D modeling**, **3D printing**, **embedded programming**, and **computer vision** to achieve autonomous navigation and obstacle avoidance.

---

## 1. Project Objective

The primary objective was to engineer a fully autonomous vehicle capable of self-navigation using real-time camera input and sensor data.

The project scope encompassed the complete ground-up design of the chassis, integration of all electronics, and development of the software stack. This includes algorithms for movement, obstacle detection, and a remote teleoperation interface. The completed vehicle was successfully demonstrated at a local maker fair.

---

## 2. Key Features and Subsystems

* **Custom 3D-Printed Chassis:** All structural components were designed in CAD software (Fusion 360/SolidWorks) and fabricated using a desktop 3D printer.
* **Autonomous Navigation:** Utilizes computer vision (OpenCV) and machine learning (TensorFlow) for path following and obstacle detection.
* **Multi-Sensor Fusion:** Integrates data from ultrasonic sensors, a camera module, and IR sensors to make informed real-time navigation decisions.
* **Hierarchical Control System:** A Raspberry Pi manages high-level vision processing and control logic, while an Arduino handles low-level, real-time motor and sensor I/O.
* **Web-Based Teleoperation:** A lightweight Flask web application provides an interface for manual control and live video feedback.
* **Algorithm Validation:** The system was tested and tuned under various indoor and outdoor conditions to optimize performance.

---

## 3. Hardware Components

| Component | Description |
|---|---|
| Raspberry Pi 4 | Primary compute module; runs vision processing and main logic |
| Arduino Uno | Real-time controller for motors and sensors |
| Pi Camera | Provides live video feed for computer vision |
| Ultrasonic Sensors | Detects obstacles for navigation and collision avoidance |
| DC Motors + Driver | Provides vehicle propulsion |
| 3D Printed Chassis | Custom-designed, lightweight vehicle frame |
| Battery Pack | Provides portable power to all systems |

---

## 4. Software and Technology Stack

| Type | Tools |
|---|---|
| Programming | Python, C++ |
| Frameworks | OpenCV, TensorFlow, Flask |
| Microcontroller | Arduino IDE |
| 3D Modeling | Fusion 360 / SolidWorks |
| OS | Raspbian |

---

## 5. System Architecture

The system employs a hierarchical control architecture. The Raspberry Pi serves as the high-level "brain," handling computationally intensive tasks like image processing and decision-making.

It communicates commands via serial to the Arduino, which functions as a low-level, real-time controller. The Arduino directly interfaces with the motor drivers and sensors, ensuring rapid response to immediate obstacles and precise movement control.

![System architecture diagram 1](https://user-images.githubusercontent.com/61593351/234959681-5ce77418-8f70-4f21-b785-7d2b3a26c022.jpg)
![System architecture diagram 2](https://user-images.githubusercontent.com/61593351/234959682-025a8b70-5407-4e3d-9fa3-17e317b8f39d.jpg)
![System architecture diagram 3](https://user-images.githubusercontent.com/61593351/234959686-143efceb-cea2-4997-ac95-3dcaf4f4fe52.jpg)
![System architecture diagram 4](https://user-images.githubusercontent.com/61593351/234959676-9867c123-73ad-4f39-a5ed-081cd3dfec8d.jpg)

---

## 6. Design and Fabrication Process

### 3D Modeling & Printing
![CAD model 1](https://user-images.githubusercontent.com/61593351/234954546-81d05d14-f48e-445b-944e-dd89eae37795.png)
![CAD model 2](https://user-images.githubusercontent.com/61593351/234954666-75bada8b-ab2f-4ef3-98a2-f47a665b28fd.png)
![CAD model 3](https://user-images.githubusercontent.com/61593351/234954703-5c1405e0-cd41-4b11-9809-0a57ad07e7ec.png)
![CAD model 4](https://user-images.githubusercontent.com/61593351/234954767-99e8d6a2-087d-4da6-a888-1c65e8f8b339.png)

### Assembly and Final Build
![Assembly photo 1](https://user-images.githubusercontent.com/61593351/234965234-1612fecd-6c52-463c-81a3-a1c519d5ea66.png)
![Assembly photo 2](https://user-images.githubusercontent.com/61593351/234964802-b0f567b3-ed56-4c2c-b23f-d97c73a40e41.png)
![Assembly photo 3](https://user-images.githubusercontent.com/61593351/234964835-19576ef3-2d48-4e26-b0c3-4a4c687aa222.png)
![Assembly photo 4](https://user-images.githubusercontent.com/61593351/234964896-308baf55-2f78-4604-846b-6920a8dfa9ee.png)
