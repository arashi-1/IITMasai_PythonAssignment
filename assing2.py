from abc import ABC, abstractmethod

# Abstract base class
class SmartDevice(ABC):
    def __init__(self, name: str):
        self._name = name
        self.__is_on = False  # Private attribute

    @abstractmethod
    def operate(self):
        pass

    def _turn_on(self):
        self.__is_on = True

    def _turn_off(self):
        self.__is_on = False

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self._name} is {status}")

    @property
    def is_on(self):
        return self.__is_on


# SmartLight class
class SmartLight(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.__brightness = 70 

    def operate(self):
        self._turn_on()
        print(f"{self._name}: Light turned on — brightness {self.__brightness}%")

    def set_brightness(self, value: int):
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = value

    def get_brightness(self):
        return self.__brightness


# SmartFan class
class SmartFan(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.__speed = "Medium"

    def operate(self):
        self._turn_on()
        print(f"{self._name}: Fan turned on — speed {self.__speed}")

    def set_speed(self, speed: str):
        if speed not in ("Low", "Medium", "High"):
            raise ValueError("Speed must be 'Low', 'Medium', or 'High'.")
        self.__speed = speed

    def get_speed(self):
        return self.__speed


# SmartAC class
class SmartAC(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.__temperature = 24

    def operate(self):
        self._turn_on()
        print(f"{self._name}: AC turned on — temperature set to {self.__temperature}°C")

    def set_temperature(self, temp: int):
        if not 16 <= temp <= 30:
            raise ValueError("Temperature must be between 16°C and 30°C.")
        self.__temperature = temp

    def get_temperature(self):
        return self.__temperature



if __name__ == "__main__":
    # Create devices
    light = SmartLight("Living Room Light")
    fan = SmartFan("Bedroom Fan")
    ac = SmartAC("Office AC")

    devices = [light, fan, ac]

    # Operate and show status
    for d in devices:
        d.operate()
        d.show_status()
        print()

    # Attempt to access private attributes
    print("Attempting direct access to private attributes…")
    for attr in ("__brightness", "__speed", "__temperature", "__is_on"):
        for dev in devices:
            try:
                print(getattr(dev, attr))
            except AttributeError as e:
                print(f"{dev._name}: {e}")
    print()

    # Use setters
    light.set_brightness(85)
    fan.set_speed("High")
    ac.set_temperature(21)

    # Use getters to verify
    print("After using setters:")
    print(f"{light._name} brightness: {light.get_brightness()}%")
    print(f"{fan._name} speed: {fan.get_speed()}")
    print(f"{ac._name} temperature: {ac.get_temperature()}°C")
