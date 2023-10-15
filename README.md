## Question Description:

Design a program to classify input coordinates (x, y) into the X-axis, Y-axis, origin, or one of the four quadrants (I, II, III, IV). 
If the coodinates lies on Quadrant I print I same for other quadrants. If the coordinates on the X or Y axis print X Y respectively.
For origin print O.

## Inputs and output:
### Inputs
You are being given two numerical inputs, x and y respectively, representing the coordinates of a point in a 2D Cartesian plane.
The coordinates can be positive, negative, or zero values.
### Output
Now output a string representing the category in which the given point lies.
- **X-axis:** If the point lies on the X-axis 
- **Y-axis:** If the point lies on the Y-axis 
- **Origin:** If the point is at the origin 
- **Quadrant I:** If the point lies in Quadrant I 
- **Quadrant II:** If the point lies in Quadrant II
- **Quadrant III:** If the point lies in Quadrant III 
- **Quadrant IV:** If the point lies in Quadrant IV

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
Example 1:

Input: 5 2
Output: "Quadrant I"
Explanation: The input coordinates (5, 2) are both positive, so they lie in Quadrant I.

Example 2:

Input: -3 -1
Output: "Quadrant III"
Explanation: The input coordinates (-3, -1) are both negative, so they lie in Quadrant III

Example 3:
   - Input: (0, 0)
   - Expected Output: "Origin"
Explanation: The input coordinates (0, 0) are both zero, so point is in is the origin.
Example 4:
   - Input: (3, 0)
   - Expected Output: "X-axis"
Explanation: The input coordinates' (3, 0) y coordinate is zero,so point lies on the X-axis.
```
