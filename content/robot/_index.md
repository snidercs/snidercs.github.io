---
linkTitle: Robot
title:  Robot - FRC 2024
date:   2024-03-11T18:36:45-04:00
draft:  false
tags: ['robot']
menu:
  main:
    identifier: robot
    weight: 3
hideFooter: True
---

### Robot Features
* Differential drive.
* Front mount camera.
* Languages: C++ and Lua.
* Smart confguration file via Lua.
* Ultra low latency TimedRobot base.
* Fast code deploys when only Lua code changes.
* Unit Testing of primary bot functions.
* Unit Testing of Lua/C++ bindings.

### Firmware

The firmware is written in C++ and leverages well-documented header files (.hpp) to promote code readability and efficiency. The program manages various robot components, including the mechanical arm, shooter, and drive train, through dedicated motor control functionalities. Utilizing the WPLib's XboxController class, seamless integration with a Logitech gamepad (model details omitted) is achieved. 

To ensure maintainability, all variables are meticulously organized throughout the codebase. This meticulous structure facilitates effortless reconfiguration for port changes, motor swaps, and robot repairs, minimizing downtime. Additionally, a backup MiniSD card preloaded with the roboRIO OS and our firmware provides a quick recovery solution in unforeseen circumstances. Furthermore, our code is version-controlled using GitHub, enabling remote collaboration and assistance from offsite programmers when necessary.

This revised version incorporates the following changes:

* **Formal Language:** Replaces informal phrases like "well-documented code" with "well-documented header files (.hpp)" for a more technical tone. 
* **Specificity:** Omits specifics of the Logitech controller model for a broader appeal.
* **Emphasis on Maintainability:**  Highlights the well-organized code structure and its benefit for future modifications.
* **Professional Terminology:** Uses terms like "functionalities" and "version-controlled" for a professional feel.
* **Conciseness:** Condenses sentences while preserving key information.


### Gamepad Layout
X Box controller mapping.  Controls not listed are not in use.
|  Button/Stick |             Action          |
|---------------|:---------------------------:|
| Left Axis     | Forward and backward motion |
| Right Axis    | Rotation                    |
| Left Bumper   | Note intake                 |
| Right Bumper  | Note shooting               |
| Right Trigger | Brake                       |
| X             | Arm up                      |
| A             | Arm down                    |

### Motor Controllers
Motor controllers used in all moving parts.
| Label | Controller | For?                         |
|-------|:----------:|------------------------------|
| M1    | SparkMax   | Drivetrain primary (left)    |
| M2    | SparkMax   | Drivetrain primary (right)   |
| M3    | SparkMax   | Drivetrain secondary (left)  |
| M4    | SparkMax   | Drivetrain secondary (right) |
| M5    | SparkMax   | Lifter arm (left)            |
| M5    | SparkMax   | Lifter arm (right)           |
| M5    | SparkMax   | Shooter main (top)           |
| M5    | SparkMax   | Shooter main (bottom)        |
| M5    | SparkMax   | Shooter support              |
