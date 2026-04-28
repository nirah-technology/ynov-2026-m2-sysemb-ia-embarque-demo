from abc import ABC, abstractmethod

# Interface (très basique)
class AbleToStart(ABC):
    @abstractmethod
    def start(self):
        """Permet de démarrer le véhicule.

        Raises:
            NotImplementedError: _description_
        """
        ...


class Vehicle(AbleToStart):
    def __init__(self, manufacturer: str, model: str, year: int, horses_power: int, max_speed: int, price: int):
        self.__manufacturer: str = manufacturer
        self.__model: str = model
        self.__year: int = year
        self.__horses_power: int = horses_power
        self.__max_speed: int = max_speed
        self.__price: int = price

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer
    
    @property
    def model(self) -> str:
        return self.__model
    
    @property
    def year(self) -> int:
        return self.__year
    
    @property
    def horses_power(self) -> int:
        return self.__horses_power
    
    @property
    def max_speed(self) -> int:
        return self.__max_speed
    
    @property
    def price(self) -> int:
        return self.__price

class Moto(Vehicle):
    def __init__(self, manufacturer, model, year, horses_power, max_speed, price):

        # Appelle à la classe mère pour le d'héritage simple, non probleme.
        # super().__init__(manufacturer, model, year, horses_power, max_speed, price)

        # Appelle à une classe mère spécifique lors de l'héritage multiple, à privilégier.
        Vehicle.__init__(self, manufacturer, model, year, horses_power, max_speed, price)
    
    def start(self):
        print("Démarrage de la moto...")

class Car(Vehicle):
    def __init__(self, manufacturer, model, year, horses_power, max_speed, price):

        # Appelle à la classe mère pour le d'héritage simple, non probleme.
        # super().__init__(manufacturer, model, year, horses_power, max_speed, price)

        # Appelle à une classe mère spécifique lors de l'héritage multiple, à privilégier.
        Vehicle.__init__(self, manufacturer, model, year, horses_power, max_speed, price)
    
    def start(self):
        print("Démarrage de la voiture...")
        print("Mince, elle a calé.")

class CyberpunkMoto(Moto):
    def __init__(self, manufacturer, model, year, horses_power, max_speed, price):

        # Appelle à la classe mère pour le d'héritage simple, non probleme.
        # super().__init__(manufacturer, model, year, horses_power, max_speed, price)

        # Appelle à une classe mère spécifique lors de l'héritage multiple, à privilégier.
        Moto.__init__(self, manufacturer, model, year, horses_power, max_speed, price)

    def start(self):
        super().start()
        print("Démarrage de la moto cyberpunk...")

