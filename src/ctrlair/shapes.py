from typing import NamedTuple

Shape = NamedTuple("Shape", [("Name", str), ("Path", str)])

square = Shape("Square", "M -1 1 L 1 1 L 1 -1 L -1 -1 Z")

up_pointing_triangle = Shape("Up-Pointing Triangle", "M 0 -1 L -1 1 L 1 1 Z")

star = Shape(
    "Star",
    "M 0 0.6 L 0.6 0.9 L 0.5 0.2 L 1 -0.2 L 0.3 -0.3 L 0 -0.9 L -0.3 -0.3 L -1 -0.2 L -0.5 0.2 L -0.6 0.9 L 0 0.6 Z",
)

line_cross = Shape("Line Cross", "M 1 1 L -1 -1 M -1 1 L 1 -1")

lower_left_triangle = Shape("Lower Left Triangle", "M 1 1 L -1 -1 L -1 1 Z")
