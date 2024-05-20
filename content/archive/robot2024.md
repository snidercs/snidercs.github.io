---
title: Nelson | 2024
date: 2024-03-11T18:36:45-04:00
draft: false
hideFooter: true
ShowWordCount: true
ShowPostNavLinks: true
ShowReadingTime: true
---

Result: FRC Houston World Rank 58 in Milstein with a record of 4-6-0 (Win-Loss-Tie)

![FRC Robot 2024](/images/featured-bot-00.png)

### Alliance Summary

* Different Autonomous modes to pair with your alliance style
* Ability to hang on the Stage
* Ability to shoot notes into Speaker
* Ability to shoot notes into Amp
* Blocking capabilities
* Ability to score notes in Auto


### Features

* Differential drive.
* Heavy weight blocker.
* Front mount camera.
* Languages: C++ and Lua ([JIT enabled](https://luajit.org)).
* Smart configuration file via Lua.
* Ultra low latency timed robot.
* Fast code deploys.
* High and Low Gear modes for more accurate driving

### Hardware

Weighing in at a whopping one hundred twenty four pounds (124 lbs), and effective use of four CIM motors for tank driving, Snider 9431 is your choice of defense. We can hang too! With the power of two NEO Brushless Motor and a 36:1 planetary kit, 9431 will be hanging on stage for some rocking points!
All of our [motors](#motors) utilize Spark Max's motor controllers, which are controlled by our super quick-to-compile [C++ code](#firmware). With the struggles of a rookie team being, well a rookie team, most of our parts are recycled from bits and pieces being thrown out by our school. For example, the base of our robot is made out of an old display case. That being said, our robot is incredibly durable, clean, and a perfect addition to your alliance. 


### Firmware

The firmware is written in C++ and Lua. Our `frc::TimedRobot` handles robot setup and pre/post processing inside `init/periodic/exit` callbacks.  Our periodic (a.k.a. realtime) code path guarantees not to dynamically allocate and does not use thread locking anywhere. The system runs at approximately 60fps cycles. The lifter, shooter, and drivetrain control logic is handled in Lua as a type of middleware with the same basic realtime guarantees.

Critical aspects of the software, including Lua bindings, are rigorously checked in unit and integration tests. The code is version-controlled using GitHub + CI automation and testing.

### Motors

Motor controllers used in all moving parts.
| Label | Controller | For?                         |
|-------|:----------:|------------------------------|
| M1    | SparkMax   | Drivetrain primary (left)    |
| M2    | SparkMax   | Drivetrain primary (right)   |
| M3    | SparkMax   | Drivetrain secondary (left)  |
| M4    | SparkMax   | Drivetrain secondary (right) |
| M5    | SparkMax   | Lifter arm (left)            |
| M6    | SparkMax   | Lifter arm (right)           |
| M7    | SparkMax   | Shooter main (top)           |
| M8    | SparkMax   | Shooter main (bottom)        |
| M9    | SparkMax   | Shooter support              |

### Gamepad Layout

X Box controller mapping.  Unlisted buttons are unassigned.
|  Button/Stick |             Action          |
|---------------|:---------------------------:|
| Left Axis     | Forward and backward drive  |
| Right Axis    | Left/Right Rotation         |
| Up D-pad      | Shooter 80% power           |
| Right D-pad   | Shooter 60% power           |
| Down D-pad    | Shooter 40% power           |
| Left D-pad    | Shooter 20% power           |
| Left Bumper   | Note intake                 |
| Right Bumper  | Shooter 100% power          |
| Y             | Arm up                      |
| A             | Arm down                    |
| X             | High Gear                   |
| B             | Low Gear (25% power)        |
