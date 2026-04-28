import statistics
from pathlib import Path
from turtle import st

from .file import CsvFile

def main():
    csv_file = CsvFile()
    data = csv_file.load(Path("telemetries.csv"))

    time_x = [float(line["Time"]) for line in data]
    rpm_y = [float(line["RPM"]) for line in data]
    # print(rpm_y)

    print(statistics.mean(rpm_y))
    print(min(rpm_y))
    print(max(rpm_y))
    print(statistics.median(rpm_y))
    

if (__name__ == "__main__"):
    main()
