import json
import os
from helpers.LoggerBase import LoggingHandler


class BaseClass(LoggingHandler):
    """ Base class to save, log, load states """
    SERIALIZABLE_FIELDS = [

    ]

    def __init__(self, name):
        super().__init__()
        self.log.info(f"Base Class for {name} activated")
        self.json_name = name

    def save_state(self) -> None:
        """ Saves the current state to .json object """

        self.log.info(f"{self.json_name} saving state to 'states/{self.json_name}_data.json'")

        state = {}
        for property_name in self.SERIALIZABLE_FIELDS:
            state[property_name] = self.__getattribute__(property_name)

        if not os.path.isdir("states"):
            self.log.warning("No 'states' directory found. Creating...")
            os.mkdir("states")

        with open(f"states/{self.json_name}_data.json", "w", encoding="utf-8") as file:
            json.dump(state, file)
            self.log.info(f"{self.json_name} saved state to 'states/{self.json_name}_data.json'")

    def load_state(self) -> None:
        """ Loads the current state from .json object """

        self.log.info(f"{self.json_name} loading state from 'states/{self.json_name}_data.json'")

        try:
            with open(f"states/{self.json_name}_data.json", "r", encoding="utf-8") as file:
                state = json.loads(file.read())

            for property_name in self.SERIALIZABLE_FIELDS:
                self.__setattr__(property_name, state[property_name])
                self.log.info(f"{self.json_name} loaded state from "
                              f"'states/{self.json_name}_data.json'")

        except FileNotFoundError as error:
            self.log.error(f"Can't Load {self.json_name}: {error}")
            self.log.info(f"Solving {error.errno}. Attempting to "
                          f"save state to 'states/{self.json_name}_data.json'")
            self.save_state()

        except KeyError as error:
            self.log.error(f"File corrupted. error: {error}. 'states/{self.json_name}_data.json'")
