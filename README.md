# 🚗 CAN & IOT IMPLEMENTATION FOR VEHICAL SAFETY.

### Real-Time Vehicle Monitoring using **STM32F407**, **CAN Bus**, **ESP32**, **MQTT**, **Flask**, and **MySQL**

The project demonstrates a complete Embedded IoT solution for monitoring critical vehicle parameters using Controller Area Network (CAN) communication and cloud-based monitoring.

---

![STM32](https://img.shields.io/badge/STM32-F407-blue)
![ARM Cortex-M4](https://img.shields.io/badge/ARM-Cortex--M4-green)
![CAN Bus](https://img.shields.io/badge/CAN-Bus-success)
![ESP32](https://img.shields.io/badge/ESP32-WiFi-orange)
![MQTT](https://img.shields.io/badge/MQTT-IoT-purple)
![Flask](https://img.shields.io/badge/Flask-Python-lightgrey)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---
# 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Workflow](#-project-workflow)
- [Hardware Components](#-hardware-components)
- [Software & Technologies](#-software--technologies)
- [Repository Structure](#-repository-structure)
- [Installation Guide](#-installation-guide)
- [Results](#-results)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---
# 📖 About the Project

The **CAN-Based Vehicle Safety System** is an Embedded IoT application designed to enhance vehicle safety by continuously monitoring critical parameters in real time.

The system acquires sensor data such as **temperature, gas leakage, obstacle distance, and rain detection** using an STM32F407 microcontroller. The collected data is transmitted over the **Controller Area Network (CAN)** to another STM32 node for further processing.

The receiving STM32 communicates with an ESP32 using UART. The ESP32 publishes the received sensor values to an MQTT broker over Wi-Fi. A Flask-based server subscribes to the MQTT topic, stores the incoming data in a MySQL database, and displays the latest vehicle status on a responsive web dashboard.

This project demonstrates the integration of **Embedded Systems**, **CAN Communication**, **IoT**, and **Cloud-Based Monitoring** into a single real-time vehicle safety solution.

---
# 🎯 Project Objectives

- Monitor critical vehicle parameters in real time.
- Demonstrate reliable communication using CAN Bus.
- Integrate Embedded Systems with IoT technologies.
- Provide remote vehicle monitoring through a web dashboard.
- Store sensor data in a MySQL database for future analysis.
- Design a scalable system that can be extended with additional sensors and cloud services.

---
# ✨ Key Features

## 🚗 Vehicle Monitoring

- 🌡 Real-time Temperature Monitoring
- 🔥 Gas Leakage Detection
- 📏 Obstacle Distance Monitoring
- 🌧 Rain Detection

## ⚡ Communication

- CAN Bus Communication
- UART Communication
- Reliable Differential Signaling

## ☁ IoT Integration

- ESP32 Wi-Fi Connectivity
- MQTT Publish/Subscribe
- Flask Web Server
- MySQL Database

## 📊 Dashboard

- Live Vehicle Status
- Sensor Monitoring
- Safety Alert Indicator
- Automatic Data Refresh

## 🛡 Advantages

- Modular Design
- Reliable Communication
- Low Latency
- Easy to Expand
- Automotive-Oriented Architecture

---
# 🏗 System Architecture

The project consists of two STM32F407 microcontrollers connected through a CAN Bus network.

The transmitting node collects data from multiple sensors and sends it over the CAN network. The receiving node forwards the received information to an ESP32 through UART communication. The ESP32 publishes the data to an MQTT broker using Wi-Fi.

The Flask server subscribes to the MQTT topic, stores the received sensor data in a MySQL database, and displays it on a responsive web dashboard for real-time monitoring.

---
# 🔄 Project Workflow

The project follows a complete Embedded-to-IoT communication pipeline.

```text
Vehicle Sensors
      │
      ▼
STM32F407 (Transmitter)
      │
ADC / GPIO Processing
      │
Application Layer
      │
CAN Controller
      │
CAN Transceiver
      │
CAN_H / CAN_L
═══════════════════════
CAN Bus Network
═══════════════════════
      │
CAN Transceiver
      │
CAN Controller
      │
STM32F407 (Receiver)
      │
UART Communication
      │
ESP32
      │
Wi-Fi
      │
MQTT Broker
      │
Flask Server
      │
MySQL Database
      │
Vehicle Safety Dashboard
```

### Working Principle

1. Sensors continuously monitor vehicle parameters.
2. STM32 acquires sensor data through ADC and GPIO.
3. The application layer processes the sensor values.
4. The CAN controller creates CAN frames.
5. The CAN transceiver sends the data over the CAN Bus.
6. The receiving STM32 extracts the received CAN data.
7. The receiver forwards the information to ESP32 through UART.
8. ESP32 publishes the data to the MQTT broker.
9. Flask receives the MQTT message, stores it in MySQL, and updates the dashboard.

---
# 🛠 Hardware Components

The following hardware components are used in the implementation of the Vehicle Safety Monitoring System.

| Component | Specification | Purpose |
|-----------|--------------|---------|
| STM32F407VG | ARM Cortex-M4 MCU | Sensor interfacing, CAN communication, and data processing |
| ESP32 DevKit | Wi-Fi Microcontroller | IoT communication using MQTT |
| MCP2551 / TJA1050 | CAN Transceiver | CAN Bus communication |
| LM35 | Temperature Sensor | Measures vehicle temperature |
| MQ-2 | Gas Sensor | Detects combustible gases |
| HC-SR04 | Ultrasonic Sensor | Measures obstacle distance |
| Rain Sensor Module | Digital Sensor | Detects rainfall |
| Breadboard & Jumper Wires | Prototype Hardware | Circuit connections |
| USB Cable | Communication | Programming STM32 and ESP32 |

---
# 💻 Software & Technologies

| Technology | Purpose |
|------------|---------|
| STM32CubeIDE | Embedded Firmware Development |
| STM32CubeMX | Peripheral Configuration |
| Arduino IDE | ESP32 Programming |
| Embedded C | STM32 Firmware Development |
| Python | Backend Development |
| Flask | Web Server |
| MQTT (Mosquitto) | Message Broker |
| MySQL | Database |
| HTML | Dashboard Structure |
| CSS | Dashboard Styling |
| Git & GitHub | Version Control |

---
# 📂 Repository Structure

```text
CAN-Based-Vehicle-Safety-System/
│
├── STM32/
│   ├── Transmitter/
│   └── Receiver/
│
├── ESP32/
│   └── esp32_code.ino
│
├── Flask_Server/
│   ├── server.py
│   ├── database.py
│   ├── config.py
│   ├── templates/
│   └── static/
│
├── images/
│   ├── dashboard.png
│   ├── database.png
│   └── hardware_setup.jpg
│
├── README.md
└── LICENSE
```

---
# ⚙ Installation Guide

## Clone the Repository

```bash
git clone https://github.com/CAN-Implementation-for-Vehicle-Safety/CAN-Based-Vehicle-Safety-System-with-IoT-Monitoring-Using-STM32.git
cd CAN-Based-Vehicle-Safety-System-with-IoT-Monitoring-Using-STM32```

## Install Required Python Packages

```bash
pip install flask
pip install paho-mqtt
pip install mysql-connector-python
```

## Configure MySQL

- Create the required database.
- Import the SQL schema if available.

## Start MQTT Broker

```bash
mosquitto
```

## Flash STM32 Firmware

- Open STM32CubeIDE.
- Build and flash both STM32 projects.

## Upload ESP32 Firmware

- Open Arduino IDE.
- Select the ESP32 board.
- Upload the sketch.

## Run Flask Server

```bash
python server.py
```

## Open Dashboard

```text
http://localhost:5000
```

---
# 📈 Results

The implemented system successfully demonstrates real-time vehicle monitoring through Embedded Systems and IoT integration.

### Achievements

- Successfully established CAN communication between two STM32F407 nodes.
- Real-time sensor data transmission over CAN Bus.
- Reliable UART communication between STM32 and ESP32.
- Successful MQTT-based cloud communication.
- Automatic storage of sensor readings in MySQL.
- Live monitoring through a Flask-based web dashboard.

---
# 🚀 Future Enhancements

The current implementation can be extended with additional features such as:

- GPS-Based Vehicle Tracking
- Mobile Application Integration
- Cloud Deployment (AWS / Azure)
- AI-Based Predictive Maintenance
- Driver Fatigue Detection
- SMS and Email Alerts
- CAN FD Support
- Real-Time Notifications

---
# 📜 License

This project was developed as part of the **CDAC DESD** curriculum for educational and research purposes.

You are free to use, modify, and extend this project for learning purposes with proper attribution.

---
