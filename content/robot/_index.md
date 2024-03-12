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
* Differential drive
* Front mount camera
* More....

### Firmware Features
* Languages: C++ and Lua.
* Smart confguration file via Lua.
* Ultra low latency TimedRobot base.
* Fast code deploys when only Lua code changes.
* Unit Testing of primary bot functions.
* Unit Testing of Lua/C++ bindings.

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
