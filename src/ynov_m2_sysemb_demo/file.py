from pathlib import Path
from json import dumps, loads
from csv import DictReader, DictWriter
import pickle

class JsonFile:

    def save(self, data: dict, json_destination_file: Path):
        json_string = dumps(data)
        try:
            with open(json_destination_file, 'w') as file:
                file.write(json_string)
        except:
            print("Impossible de sauvegarder le JSON.")
        
    def load(self, json_source_file: Path) -> dict:
        with open(json_source_file, 'r') as file:
            data = file.read()
        jsondict: dict = loads(data)
        return jsondict

class CsvFile:
    def save(self, data: list[dict], csv_destination_file: Path):
        header = data[0].keys()
        with open(csv_destination_file, 'w') as file:
            dict_writer = DictWriter(file, fieldnames=header)
            dict_writer.writeheader()
            for entry in data:
                dict_writer.writerow(entry)

    def load(self, csv_source_file: Path) -> dict:

        with open(csv_source_file, 'r') as file:
            dict_reader = DictReader(file)
            for line in dict_reader:
                print(line)
        return dict_reader

class PickleFile:
    def save(self, data: any, pickle_destination_file: Path):
        data_as_bytes = pickle.dumps(data)
        with open(pickle_destination_file, 'wb') as file:
            file.write(data_as_bytes)

    def load(self, pickle_source_file: Path) -> any:
        with open(pickle_source_file, 'rb') as file:
            data = pickle.loads(file.read())
        return data