import unittest

from rover.rover import *


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 10)

        self.assertEqual(plateau.width, 7)
        self.assertEqual(plateau.height, 10)


class TestRoverValidLanding(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(1, 2, "N")

        rover = Rover(plateau, position)
        result = {
            "x": 1,
            "y": 2,
            "head": "N"
        }
        self.assertEqual(rover.current_position, result)


class TestRoverInValidPosition(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(8, 2, "N")

        with self.assertRaises(BaseException) as exc:
            Rover(plateau, position)
        assert "Can not move/land to given location" in str(exc.exception)


class TestRoverFinalPosition(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2, "N")
        rover = Rover(plateau, position)
        cmds = "LMLMLMLMM"
        for i in cmds:
            rover.run_command(i)
        final_position = {
            "x": 1,
            "y": 3,
            "head": "N"
        }
        self.assertEqual(rover.current_position, final_position)
