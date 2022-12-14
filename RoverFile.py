from helpers.BaseClass import BaseClass
from power_control.PowerControl import PowerControl
from modules.Weather.WeatherMain import WeatherMain


class Rover(BaseClass):
    """ Main class. Controls whole rover"""

    SERIALIZABLE_FIELDS = [
        "state",
    ]

    def __init__(self):
        super().__init__("rover_main")
        self.log.info("Rover activation started.")
        self.state = "Activating"
        self.power_handler = PowerControl()
        self.weather_core = WeatherMain()
        self.load_state()

    def run(self) -> None:
        """ Main execution. Starts all processes in rover """

        self.log.info("Running")
        self.battery_check()

    def battery_check(self):
        """ Checks battery conditions"""

        uv = self.weather_core.get_weather()
        temp = self.weather_core.get_weather_temp()
        charging_conditions = {"uv": uv,
                               "temp": temp}
        self.power_handler.check_charge(charging_conditions)
