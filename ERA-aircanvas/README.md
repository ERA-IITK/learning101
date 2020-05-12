# Air Canvas

Just imagine how it would have been that whatever we draw with our fingers in the air gets actually drawn on some surface and you could have been able to see that drawing with your eyes rather than pressurising your brain to imagine and make a picture in itself. Well, you would be able to see it as long as you want. Just imagine that you would be able to draw anything without using pens, pencils, brushes, etc and save it to your smart phone or PC for future use. Just imagine that you wave your finger in the air and a message is sent to your peers without typing that message manually. This project is a way to convert all your imaginations into reality where anything can be drawn on the screen by just waving your fingers in the air.

## Getting Started

The project presents a software application which, on launching, displays a drawing platform a window showing the frames captured by the camera (attached to the PC) in succession. When you draw anything using your forefinger in the air  before the camera, that drawing will be drawn on the drawing platform beside. You can also change the color and thickness of the curves drawn on the screen by suitable keys and track-bars. 

### Prerequisites

Language used is python-3.x and the environment is ubuntu-18.04-LTS
Packages used is opencv-python and pygame


### Installing

The language used is python-3.x which can be downloaded by the following snippet on Linux and can be edited on any local editor.

```
$sudo apt-get update
$sudo apt-get install python3.6
```
To check whether the python is installed or not, you can check its version by: 

```
$python --version
```
To install the pip3 use the following snippet:

```
$sudo apt-get -y install python3-pip
```
In this project we have used two packges of python namely openCV and pygame. To download them use the following snippet:

```
$pip3 install opencv-python
$pip3 install pygame
```
To check for the installation of the packages, open the python terminal by typing ```python3``` and type the following:

```
import cv2
import pygame
```
If everything works fine then you can proceed with our code.

### Setup

### Concepts

#### Finger Tip Detection

#### Pygame Drawing

Pygame is an amazing library that allows us to build small gui wherein we can draw anything, insert images, vedios, icons and so on. It constantly loops over the gui's screen and thus through simple logical code, we can easily make our drawings move in some particular pattern. It defines a term 'event' which basically refers to any activity done by the mouse or keypad. Thus we can easily incorporate various basic features like mouse clicks, key press, etc. We can draw numerous shapes using very easy functions provided in this module. Having done the fingertip detection, now we know two coordinates, the current and the previous one, and these are enough to draw a line between them using the pygame.draw.line() function using the values of the selected color and thickness. This process iterates over frames and we see a continuous line drawn on the pygame screen.

### Additional Features

Besides simply drawing, we have also incorporated various other features like 
* Color changing using various keys on the keyboard
* Changing the thickness of the line drawn using the trackbar window
* Icon of a small pen that points the current position of your fingers tip on the imaginary 2D surface of air.

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Ayush-Ranjan/ERA-aircanvas.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/Ayush-Ranjan/ERA-aircanvas/compare?expand=1" target="_blank">`https://github.com/Ayush-Ranjan/ERA-aircanvas/compare?expand=1`</a>.

---

## Team

Our team comprised two members from Team ERA, IIT Kanpur namely:
* Ayush Ranjan
* Sidhartha Watsa

## Bibliography




## Acknowledgments

* We got extensive support and mootivation from the Team ERA-IITK and we are very grateful to them for giving us this opportunity.
* 
* 
