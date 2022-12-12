import os
import logging
from RoverFile import Rover


def main():
    """ Main function which runs all processes """
    rover = Rover()
    rover.run()


if __name__ == "__main__":
    if not os.path.isdir('rover_logs'):
        os.makedirs('rover_logs')

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s]: %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler("rover_logs/expedition.log", 'w'),
            logging.StreamHandler()
        ]
    )
    main()
