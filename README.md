# Simple STOP/START button for OctoPi/OctoPrint

Easy STOP/START button solution for stopping and starting the 3D print job on octoprint, running on raspberry pi from the printers location. The script can be edited to work on any device with GPIO and is meant to be a baseline for more complicated projects.

The code is very simple, every time the physical button is pressed the server check if there is a printer job running, if there is one it stops it otherwise it starts a job that is preselected.

 
