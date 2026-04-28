import statistics
from pathlib import Path

from .file import CsvFile

def main():
    csv_file = CsvFile()
    data = csv_file.load(Path("telemetries.csv"))
    print(data["Time"])


if (__name__ == "__main__"):
    main()
