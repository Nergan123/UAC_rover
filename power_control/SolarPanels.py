import time
from helpers.BaseClass import BaseClass


class SolarPanels(BaseClass):
    """ Solar panel. Charges when unfolded"""

    SERIALIZABLE_FIELDS = [
        "state",
        "identifier",
    ]

    def __init__(self, identifier=0):
        self.identifier = identifier
        self.__class__.__name__ = self.__class__.__name__.replace(f"_{self.identifier - 1}", "")
        self.__class__.__name__ = self.__class__.__name__ + f"_{self.identifier}"
        super().__init__(f"solar_panel_{self.identifier}")
        self.state = "folded"
        self.load_state()

    def unfold(self, lock) -> None:
        """Unfolding solar panels"""

        with lock:
            self.log.info("Unfolding panels")
            self.state = "unfolding"

            for i in range(100):
                self.log.info(f"Unfolding: {i}%")
                time.sleep(0.5)

        self.state = "unfolded"
        self.log.info("Successfully unfolded.")
        self.save_state()

    @staticmethod
    def charge(conditions) -> float:
        """ Receives weather conditions and returns voltage"""

        output = int.from_bytes(conditions, "big")/255 * 0.1
        time.sleep(1)
        return output
