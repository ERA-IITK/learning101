# Getting Started

### Installation of Linux and Introduction to Linux Ecosystem

 - **Getting Started with Ubuntu**  
   - Install Ubuntu 16.04  
   - Install VS code, Google Chrome  
   - Install git  
   - Install pip, pip3, link pip3 with python3  
   - Login with your GitHub on VScode.  
   - Detect your Webcam from the terminal using V4L,  
   - Capture a selfie using the Terminal.  
   - Find out your IP address using Terminal  

### Programming Languages(C++ and Python)

 - **Installing and Using Python**    
 - **Variables and Expressions**  
    - Try and Except, Conditional Statements, Functions, Loops and IterationsData Structures, Strings, Files, Lists, Tuple, Dictionaries  
- **Object-Oriented Python**  
  - Object-Oriented Definitions and Terminology  
  - Class and Object  
  - Object Life Cycle  
  - Object Inheritance  
- **Basic Structured Query Language**  
- **Object-Oriented C++**  
    - Object-Oriented Definitions and Terminology  
    - Class and Object  
    - Object Life Cycle  
    - Object Inheritance  
- **Hackerrank - C++**  
  - You have to solve until Challenge 20, Abstract Classes - Polymorphism  
  - Write your program locally using your text editor and push to your GitHub repository, Learning101. At the end of the task, submit a pull request to ERA-IITK/learning101.  
- **Hackerrank -Python**  
  - You have to solve from Challenge 9, Nested Lists until Challenge 27, Merge the Tools.  
  - Write your program locally using your text editor and push to your GitHub repository, Learning101. At the end of the task, submit a pull request to ERA-IITK/learning101.  

### GitHub for Work  
   - Fork learning101 from github.com/ERA-IITK. Add your respective codes along with a README.MD detailing the internal structure of your repository in a concise manner. (1 or 2 lines for each subfolder)  
   - On 15th March, send a pull request.  

### Reading  

  - Read the Rules Manual for RoboMaster AI challenge 2020  

### Image Processing  

  - What is an image?  
  - What is the brightness, contrast, saturation, and hue of an image?  
  - What is the difference between image processing and computer vision?  
  - Learn about various color-spaces and bit-wise operations in OpenCV and try to implement skin detection.  
  - Learn about contours in OpenCV and use the previously implemented skin detection with contours.  
  - Read and practice Chapter 1 (except PCA) of the book Programming Computer Vision with Python by Jan Erik Solem (can be found in ERA-IITK/res)  
  - Write a code to detect the best Armour Plate in the given image. Draw a rectangular box around the armor. (Image can be found in ERA-IITK/res)  

### Introduction to Linux Ecosystem- Part 2 

- **Getting into Linux Eco-System**  
  - Kernel vs. Operating System  
  - What is a Daemon?  
  - Difference Between Bash and sh ?  
  - What is Gnome?  
  - What is Shell?  
  - Complete the chapters 1-5 of the book "Linux Shell Scripting Tutorial - written by Vivek Gite" (Found at ERAIITK/res)    
  - Complete Challenges 1-10 (up to Functions and Fractals) on Hackerrank  
*([https://www.hackerrank.com/domains/shell](https://www.hackerrank.com/domains/shell))*  

### Getting into ROS Eco-System

- **Installing and Using ROS**  
  - Installation - one line, Desktop- full, kinetic.  
  - Read through Section 1.1 of Mahtani - found at ERAIITK/res  
  
- **ROS System Levels**  
   - Understand the Filesystem level and The Computation Graph level, and draw flow diagram, illustrating your understanding of each of these  
  
-  **Introduction to Nodes and Topics**  
   - Use Turtle Sim simulator, and use the built-in teleop, Use the RQT graph to see the active
nodes and topics.  
   - Write a node that moves the turtle forward when the input is &#39;f&#39; and backward when input is &#39;b&#39;  
   - Write a node that takes an input &#39;r&#39; from the user and makes the turtle move in c circle of radius &#39;r&#39;  
Getting comfortable with the ROS Eco-System - CMake
  - What is CMake? Why should we be using it
  - Go through &#39;An Introduction to Modern CMake&#39; from [cliutils](https://cliutils.gitlab.io/modern-cmake/)
    - Installing CMake
    - Running CMake
    -  Complete chapter 2- an introduction to the basics.
  - Complete tutorial 1 made by the [Cmake Foundation](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
  - Complete [Using Dependencies Guide](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html)
  - Those who did not complete ROS tasks by making a package need to do it in this way.
2. Having fun with ROS.

-
  - You have to work in pairs to write a subscriber publisher pair that can communicate over the network to your partner&#39;s computer.
    -  Ping the network, Perform simple addition.
    -  You must use a ROS based approach.
    -  Submit these task as a separate compiled workspace
    -  Generate the RQT graph and submit that as an image file
  - Now modify your talker subscriber network such that the talker on your computer is able to control the turtlesim turtle in your partner&#39;s computer.
    -  The movements are forward and backward, turn left 90\* turn right 90\*. The forward-backward motion must be quantized for each keypress irrespective of the duration of the keypress.
  - Now modify your above program to include gesture recognition. Control the turtlesim turtle on your partner&#39;s computer using hand gestures in front of your webcam
    -  The same movement constraints apply as above.
    -  You must get feedback of the current position of the turtle, back on your screen.
    -  Use OpenCV for image processing
  - The above tasks need to be done in the C programming language and compiled as a package
