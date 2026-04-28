import statistics
from pathlib import Path

from .file import CsvFile

def main():
    csv_file = CsvFile()
    data = csv_file.load(Path("telemetries.csv"))
    for line in data:
        print(line["Time"])
    

if (__name__ == "__main__"):
    main()
