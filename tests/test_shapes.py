import unittest
from ctrlair import shapes

VALID_SVG_PATH_COMMANDS = ["M", "L", "H", "V", "C", "S", "Q", "T", "A", "Z"]


def svg_path_string_within_square_bounding_box(path: str) -> bool:
    numbers = [int(p) for p in path.split() if p.lstrip("-").isdigit()]

    return all(num >= -1 and num <= 1 for num in numbers)


def svg_path_string_commands(path: str) -> bool:
    letters = [p for p in path.split() if not p.lstrip("-").isdigit()]

    return all(letter in VALID_SVG_PATH_COMMANDS for letter in letters)


class TestShapes(unittest.TestCase):
    def test_square(self):
        self.assertTrue(svg_path_string_within_square_bounding_box(shapes.square.Path))
        self.assertTrue(svg_path_string_commands(shapes.square.Path))


if __name__ == "__main__":
    unittest.main()
