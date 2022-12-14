import random
from helpers.BaseClass import BaseClass


class TemperatureSensor(BaseClass):
    """ Temperature sensor. """

    def __init__(self):
        super().__init__("temp_sensor")
        self.log.info("Temperature Sensor is active")

    def measure(self):
        """Get temperature from normal distribution"""
        output = round(random.uniform(-10, 25), 1)
        self.log.info(f"Temperature: {output}")
        return output
