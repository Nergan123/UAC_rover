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
        self.min_battery_level = 2.3

    def check_charge(self, condition) -> None:
        """ Checks if power supply in battery is sufficient for operation """

        if self.battery_level < self.min_battery_level:
            self.log.warning(f"Insufficient charge: {self.battery_level}%")
            self.charging(condition)
        else:
            self.log.info("Charge sufficient")

        self.save_state()

    def charging(self, condition) -> None:
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

        while self.battery_level <= 4.2:
            for panel in self.panels:
                efficiency = panel.calc_efficiency(condition["temp"])
                volt = panel.charge(condition["uv"])
                resulting_voltage = volt * efficiency
                self.receive_charge(resulting_voltage)
                self.log.info(f"Received {volt} volts. "
                              f"Temperature resulted in efficiency {efficiency}, "
                              f"leading to voltage {resulting_voltage}."
                              f"Battery charge: {self.battery_level}")

    def receive_charge(self, val) -> None:
        """ Receives charge and adds it to battery supply"""

        self.battery_level += val

    def give_charge(self, val) -> float:
        """ Removes charge value from battery and returns it"""
        self.battery_level -= val
        return val
