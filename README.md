\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
ENPM 661- Planning for Autonomous Robots (Spring 23)

Project 3, Phase 1: Implementation A\* algorithm for a mobile Robot
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Team Members:

Name: 
UID:

Name: Poojan Desai 
UID: 119455760

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

GitHub Links: https://github.com/PoojanDesaii99/Project-3_Phase_1_661

Video Drive Link:
https://drive.google.com/drive/u/0/folders/1oVQV58a8_lQ6zpB-\_En5b1gwFF9slW4m

Code: - Code consists of: \'Generating an Obstacle Map, \'Movement in 5
Directions\', \'Using Search Algorithm and Back Tracking\' and
\'Visualizing the Tracked Path\' - The Search Algorithm used here is \'
A Star Algorithm\' to reach end goal and obtain the path. - The code has
been delineated very clearly in the comments provided in the Code.

Dependencies: - python 3.9 (works for any python 3 version) - Python
running IDE. (I used Visual Sudio Code to program the Code and Execute
the Code) - Libraries: numpy, matplotlib.pyplot, heapq, time, math

Instructions to Run the Code:

To get the Output (without Visualization) - Open the program file in any
IDE. (I used VS Code) - Run the Program - In the Console, the program
asks for: \|\-- Robot Radius \|\-- Robot Step Size \'\-- The x and y
coordinates of Start and Goal Node.  - Enter as prompted. Ex: Robot
Radius: 5 (As per requriement); Step size: 1; Start: 50, 50; Initial
Theta: 90; Goal: 400, 20; Final Theta: 60. - The Output Plot with
planned Path should be Visible.

To get the Output (with Visualization) - Open the program file in any
IDE. (I used PyCharm) - UnComment the line used for Visualization i.e.
\'328\', which says-
\"#plt.pause(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)\" -
Run the Program - In the Console, the program asks for: \|\-- The
Obstacle Clearance and Robot Radius \|\-- Robot Step Size and \'\-- The
x and y coordinates of Start and Goal Node.  - Enter as prompted. Ex:
Robot Radius: 5 (As per requriement); Step size: 1; Start: 50, 50;
Initial Theta: 90; Goal: 400, 20; Final Theta: 60. - The Output Plot
with planned Path should be Visible.

Understanding the Output Plot - The Robot movable space is shown in
White Color - The Pixels in Blue are the Obstacles. - The Pixels in Cyan
is the Clearance Space. - The explored path is marked by Green color. -
The Planned Path is shown by Red Dotted Lines.
