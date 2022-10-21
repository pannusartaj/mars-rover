import json

from rover.rover import *

with open("input.json", "rb") as input_file:
    inputs = json.loads(input_file.read())

for input_ in inputs:
    plateau = Plateau(*input_["plateau"])
    landing = Position(*input_["landing"])
    rover = Rover(plateau, landing)
    for cmd in input_["command"]:
        rover.run_command(cmd)
    # custom code to print as required
    position = rover.current_position
    position = [str(x) for x in position.values()]
    print(f'{input_["name"]}:{" ".join(position)}')
