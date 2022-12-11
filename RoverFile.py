from helpers.BaseClass import BaseClass
from power_control.PowerControl import PowerControl


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
        self.load_state()

    def run(self) -> None:
        """ Main execution. Starts all processes in rover """

        self.log.info("Running")
        print("Run")
        self.power_handler.check_charge()
