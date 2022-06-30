# CometTrajectory
## Introduction
Using the astrometry data of a comet, I tried to predict the trajectory of the comet using Python. 
## Libraries used
I used the following libraries to predict the trajectory.
- Pandas
- Numpy
- Matplotlib
- Scipy
## Data
The data given consists of the following variables
- Timestamp of Observation
- Distance of comet from earth
- Angle between comet and Sun
## Approach
I used simple geometrical apporach to find the trajectory of the comet. 
- I found out the distance between comet and Sun using cosine rule from trignonmetry from the given values.
- I assumed the ray passing through earth and Sun at timestamp 0 to be the reference axis.
- I calculated the angle between earth and the reference axis at each timestamp by assuming that earth is rotating in circular motion.
- I calculated the angle between earth and comet as seem from Sun by using sine rule from trigonometry.
- I calculated the angle made by comet with the reference axis at each timestamp by doing algebraic sum of earth-axis angle and earth-comet angle.
- Since we have distance and angle at each timestamp from Sun, I used Scipy library to predict the nature of the curve using polar conic equation and ``scipy.optimize.curve_fit``.
- I got the eccentricity to be 0.28, which indicates that the orbit around the Sun is elliptical.
- Looking at the graph between polar angle and time, we can see that the trajectory keeps repeating. We can approximate from the graph and we get the time period to be 348 days.
## Final answers
Trajectory: Ellipse<br>
Eccentricity: 0.28<br>
Time Period: 348 days<br>
## Problem Statement
This Problem Statement is given by Team Krithikaa of IITB. Link: https://github.com/krittikaiitb/KSP2021-selection
