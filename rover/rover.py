import copy


class Plateau(object):
    """
    Class for Plateau object as rectange with four vertices
    """

    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.MIN_WIDTH = min_width
        self.MIN_HEIGHT = min_height

    def is_position_valid(self, position):
        """
        Checking if the given position lies within Plateau or not
        """
        return self.MIN_WIDTH <= position.x <= self.width and self.MIN_HEIGHT <= position.y <= self.height


class Position(object):
    """
    Position class storing x, y coordinates with heading
    """
    x = 0
    y = 0
    head = "N"

    def __init__(self, x=0, y=0, head="N"):
        self.x = x
        self.y = y
        self.head = head


class Rover(object):

    #   directions are considered in a clockwise manner
    directions = ["N", "E", "S", "W"]
    total_directions = len(directions)

    # Rover default position
    default_position = Position(0, 0, "N")

    def __init__(self, plateau, landing_position=None):
        """
        Initializing mars rover with below params
        :param plateau
        :param landing position 
        """
        self.plateau = plateau
        self.position = self.default_position
        if landing_position:
            #  To validate if landing position is valid
            self.update_position(landing_position)

    def update_position(self, new_position):
        # Check if new position is valid or not
        if self.plateau.is_position_valid(new_position):
            self.position = new_position
        else:
            raise BaseException("Can not move/land to given location")

    @property
    def current_position(self):
        return {"x": self.position.x, "y": self.position.y, "head": self.position.head}

    def run_command(self, command):
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            self.move()
        else:  # Unrecognized instruction
            print("Wrong parameters!..")

    def move(self):
        # Assume that the square directly North from (x, y) is (x, y+1).
        new_position = copy.deepcopy(self.position)
        current_head = self.position.head

        if current_head == "N":
            new_position.y += 1
        elif current_head == "E":
            new_position.x += 1
        elif current_head == "S":
            new_position.y -= 1
        elif current_head == "W":
            new_position.x -= 1

        self.update_position(new_position)

    def turn_left(self):
        """
        Will move from right to left in the directions array
        """
        current_index = self.directions.index(self.position.head)
        self.position.head = self.directions[-1] if current_index == 0 else self.directions[current_index - 1]

    def turn_right(self):
        """
        Will move from left to right in the directions array
        """
        current_index = self.directions.index(self.position.head)
        self.position.head = self.directions[0] if current_index == len(
            self.directions) - 1 else self.directions[current_index + 1]
