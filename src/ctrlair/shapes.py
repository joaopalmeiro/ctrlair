from typing import NamedTuple

Shape = NamedTuple("Shape", [("Name", str), ("Path", str)])

square = Shape("Square", "M -1 1 L 1 1 L 1 -1 L -1 -1 Z")
circle = Shape(
    "Circle", "M -1 0 A 1 1 0 0 0 0 1 A 1 1 0 0 0 1 0 A 1 1 0 0 0 0 -1 A 1 1 0 0 0 -1 0"
)

up_pointing_triangle = Shape("Up-Pointing Triangle", "M 0 -1 L -1 1 L 1 1 Z")
down_pointing_triangle = Shape("Down-Pointing Triangle", "M 0 1 L -1 -1 L 1 -1 Z")
left_pointing_triangle = Shape("Left-Pointing Triangle", "M -1 0 L 1 1 L 1 -1 Z")
right_pointing_triangle = Shape("Right-Pointing Triangle", "M 1 0 L -1 1 L -1 -1 Z")

star = Shape(
    "Star",
    "M 0 0.6 L 0.6 0.9 L 0.5 0.2 L 1 -0.2 L 0.3 -0.3 L 0 -0.9 L -0.3 -0.3 L -1 -0.2 L -0.5 0.2 L -0.6 0.9 L 0 0.6 Z",
)

line_cross = Shape("Line Cross", "M 1 1 L -1 -1 M -1 1 L 1 -1")

lower_right_triangle = Shape("Lower Right Triangle", "M -1 1 L 1 -1 L 1 1 Z")
lower_left_triangle = Shape("Lower Left Triangle", "M 1 1 L -1 -1 L -1 1 Z")
upper_right_triangle = Shape("Upper Right Triangle", "M 1 1 L -1 -1 L 1 -1 Z")
upper_left_triangle = Shape("Upper Left Triangle", "M -1 1 L -1 -1 L 1 -1 Z")
