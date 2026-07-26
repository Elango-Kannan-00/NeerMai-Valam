# NeerMai Valam 

![NeerMai Valam Logo](images/logo.png)

## IoT Enabled Equitable Water Distribution and Monitoring System for Sustainable Rural Water Management

# Project Overview

- **NeerMai Valam** is an IoT-based smart water distribution and monitoring system designed to bring fairness, automation, and transparency to household water supply, particularly in rural and semi-urban areas. The project addresses the widespread problem of unequal and unmonitored water distribution by automatically allocating water to households based on the government-recommended standard of **55 Litres Per Capita per Day (LPCD)**.

- The system uses a **Raspberry Pi** as the main controller, an **ultrasonic sensor** to monitor tank water levels, a **flow meter** to measure real-time water usage, and a **solenoid valve** (driven via a relay) to automatically control water release. An **LCD display** provides live status updates to the household.

- By combining low-cost hardware with simple, effective allocation logic, NeerMai Valam eliminates manual valve operation, reduces water wastage and overflow, discourages water theft, and introduces basic usage analytics — creating a scalable foundation for smart, sustainable rural water management.

# Problem Statement

Water distribution in many rural and semi-urban communities still relies heavily on manual processes, leading to several recurring issues:

- **Unequal water distribution** across households
- **Manual valve operation**, dependent on human availability and honesty
- **Water wastage** due to overflow and lack of shutoff mechanisms
- **Overflow of storage tanks** from unmonitored filling
- **Water theft** through unauthorized tapping
- **Lack of real-time monitoring** of tank levels and usage
- **Heavy human dependency** for day-to-day distribution
- **No usage analytics** to track consumption patterns or detect anomalies

These issues collectively result in inefficient, unfair, and unsustainable water management systems.

# Proposed Solution

NeerMai Valam automates the entire water distribution pipeline — from measuring available water to delivering the exact allocated quantity per household — removing the need for manual intervention.

```
Water Tank
     ↓
Ultrasonic Sensor
     ↓
Raspberry Pi
     ↓
Water Allocation Logic
     ↓
Solenoid Valve
     ↓
Flow Meter
     ↓
LCD Display
```

The Raspberry Pi continuously reads the tank's water level, calculates the amount of water each household is entitled to based on the 55 LPCD standard, and controls the solenoid valve accordingly — while the flow meter ensures the exact quantity is delivered.

# Key Features

- Automatic water distribution
- 55 LPCD (Litres Per Capita per Day) allocation
- Real-time tank level monitoring
- Real-time flow measurement
- Automatic valve control
- Overflow prevention
- Water usage monitoring
- Leakage detection support
- IoT-enabled architecture
- Low-cost prototype

# System Architecture

```
              Water Tank
                   │
          Ultrasonic Sensor
                   │
             Raspberry Pi
         ┌─────────┴─────────┐
         │                   │
      LCD Display      Solenoid Valve
                               │
                         Flow Meter
                               │
                          Household
```

# Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi 3B+ | Main Controller |
| HC-SR04 (Ultrasonic Sensor) | Water Level Measurement |
| Flow Meter | Water Usage Measurement |
| 12V Solenoid Valve | Water Control |
| LCD Display (I2C) | Status Display |
| Relay Module | Controls Valve |
| Power Supply | Powers Components |

# Software Stack

**Programming**
- Python

**IoT / Platform**
- Raspberry Pi OS
- GPIO
- I2C

**Libraries**
- `RPi.GPIO`
- `RPLCD`
- `time`

# Working Principle

```
Step 1 — Water fills the storage tank.
↓
Step 2 — The ultrasonic sensor measures the tank's water level.
↓
Step 3 — The Raspberry Pi calculates the available water.
↓
Step 4 — Water allocation is calculated using the 55 LPCD standard.
↓
Step 5 — The solenoid valve opens.
↓
Step 6 — The flow meter measures the water being supplied.
↓
Step 7 — The valve closes once the target quantity is delivered.
↓
Step 8 — The LCD displays the current status.
```

# LPCD Calculation

**LPCD** = Litres Per Capita per Day
**Government Standard** = 55 LPCD

**Example:**

```
Family Members = 4

Daily Water Allocation = 55 × 4 => 220 Litres
```

The system automatically calculates each household's daily water allocation based on the number of registered household members, ensuring fair and standardized distribution without manual calculation.

# Future Enhancements

- Mobile application for household users
- Cloud-based dashboard for monitoring
- SMS alerts for low tank levels or leaks
- AI-based water demand prediction
- ML-based leak detection
- Solar-powered deployment for off-grid areas
- Government monitoring dashboard
- Household usage history and trends
- Mobile push notifications

# Challenges Faced

- Calibrating the flow meter readings, ultrasonic sensor for accurate readings
- GPIO interfacing issues during initial setup
- Achieving stable and consistent flow meter readings
- Fine-tuning valve open/close timing
- Power supply inconsistencies
- General hardware troubleshooting
- Waterproofing the prototype for real-world conditions

# My Contribution

As part of this project, I contributed to the following:

- Assisted in hardware integration
- Connected the Raspberry Pi with sensors and actuators
- Interfaced the ultrasonic sensor
- Integrated the flow meter
- Connected the LCD display via I2C
- Integrated the solenoid valve using a relay/driver
- Performed hardware testing
- Troubleshot wiring issues
- Verified sensor readings
- Assisted in prototype validation

# Team Members

| Name | Role |
|---|---|
| Dhanushiya Srinivasan | Project Lead & Venture developement |
| Aiswarya Saravanan | Software development & Venture development |
| **Elango Kannan** | Hardware Integration & Prototype Development |
| Harini Madheswaran | Hardware Integration & Prototype Development |

# Project Outcomes

- Successfully developed a working prototype
- Automated household water distribution
- Demonstrated fair allocation using the 55 LPCD standard
- Reduced manual intervention in water supply
- Improved transparency in water usage
- Suitable as a foundation for rural smart water management initiatives
- Received Rs. 15,000 fund for prototype development
- Secured Top 500 in Niral Thiruvizha 3.o
