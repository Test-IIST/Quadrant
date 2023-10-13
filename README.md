## Question Description:

Design a program to classify input coordinates (x, y) into the X-axis, Y-axis, origin, or one of the four quadrants (I, II, III, IV). 
If the coodinates lies on Quadrant I print I same for other quadrants. If the coordinates on the X or Y axis print X Y respectively.
For origin print O.

## Possible Inputs:

The program should take two numerical inputs, x and y respectively, representing the coordinates of a point in a 2D Cartesian plane.
The coordinates can be positive, negative, or zero values.

## General Information:

In a 2D Cartesian plane, the X-axis is the horizontal line at y = 0, and the Y-axis is the vertical line at x = 0.
The origin is the point (0, 0) where the X and Y axes intersect.

The four quadrants are divided by the X and Y axes as follows:
Quadrant I: x > 0 and y > 0
Quadrant II: x < 0 and y > 0
Quadrant III: x < 0 and y < 0
Quadrant IV: x > 0 and y < 0

## Examples

``` pyhton
Input: 5 2

Output: I.

Explanation:
The input coordinates (5, 2) are both positive, so they lie in Quadrant I.
Example 2:

Input: -3 -1

Output: III.

Explanation:
The input coordinates (-3, -1) are both negative, so they lie in Quadrant III.
```
