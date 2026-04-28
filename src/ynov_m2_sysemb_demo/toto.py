import statistics # Importation du module complet 

from pathlib import Path
from random import randint

import cars
import file

def main():
    """
    Il s'agit du point d'entré du script.
    """
    # json_file = file.JsonFile()
    # person = {
    #     "first_name": "Nicolas",
    #     "last_name": "METIVIER",
    #     "company": "NIRAH-TECHNOLOGY"
    # }
    # car_1 = cars.Vehicle("Renault", "Clio", 2012, 75, 180, 3_500)
    # pickle_file = file.PickleFile()
    # pickle_file.save(car_1, Path("cars.bidule"))
    # car_2: cars.Vehicle = pickle_file.load(Path("cars.bidule"))
    # print(car_2.model)*

    vehicle: cars.Vehicle = cars.Moto("Yamaha", "Dragstar", 1998, 50, 140, 5_000)
    vehicle.start()


if (__name__ == "__main__"):
    main()