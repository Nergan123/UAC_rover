import threading
from helpers.BaseClass import BaseClass
from power_control.SolarPanels import SolarPanels


class PowerControl(BaseClass):
    """ Power handling class """

    SERIALIZABLE_FIELDS = [
        "battery_level",
    ]

    def __init__(self):
        super().__init__("power_controller_main")
        self.log.info("Activating power supply")
        self.battery_level = 0  # volts
        self.panels = []
        for i in range(2):
            self.panels.append(SolarPanels(i))
        self.load_state()

    def check_charge(self):
        """ Checks if power supply in battery is sufficient for operation """

        if self.battery_level < 30:
            self.log.warning(f"Insufficient charge: {self.battery_level}%")
            self.charging()

    def charging(self):
        """ Uses solar panels to charge battery until voltage is sufficient """

        threads = []
        for panel in self.panels:
            threads.append(
                threading.Thread(
                    target=panel.unfold,
                    args=[threading.Lock()]
                )
            )

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
