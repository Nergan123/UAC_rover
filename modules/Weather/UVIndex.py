import random
from helpers.BaseClass import BaseClass


class UVIndexSensor(BaseClass):
    """ Measures UV index"""

    def __init__(self):
        super().__init__("uv_sensor")
        self.log.info("Sensor is active")

    def measure(self) -> float:
        """ Returns current UV index"""

        output = random.uniform(0, 1)
        self.log.info(f"UV: {output}")
        return output
