import time
from helpers.BaseClass import BaseClass
from modules.Weather.UVIndex import UVIndexSensor


class WeatherMain(BaseClass):
    """ Module responsible for weather measurements"""
    SERIALIZABLE_FIELDS = [
        "state",
        "last_measurement",
        "date_measurement",
    ]

    def __init__(self):
        super().__init__("weather_main")
        self.state = "active"
        self.uv_sensor = UVIndexSensor()
        self.last_measurement = 0.5
        self.date_measurement = time.time()
        self.log.info("Weather module active")
        self.load_state()

    def get_weather(self):
        """ Outputs UV index value"""

        date = time.time()
        if date - self.last_measurement < 30:
            output = self.uv_sensor.measure()
            self.log.info(f"Current UV = {output}")
            self.last_measurement = output
            self.date_measurement = date
        else:
            self.log.info("Last measurement happened less "
                          "than 30 sec ago. Returning previous "
                          "value")
            output = self.last_measurement

        output = int(output * 255).to_bytes(2, byteorder='big')
        self.save_state()

        return output
