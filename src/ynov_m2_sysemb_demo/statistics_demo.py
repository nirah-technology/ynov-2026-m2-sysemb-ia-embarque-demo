import statistics
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from .file import CsvFile

def main():
    csv_file = CsvFile()
    data = csv_file.load(Path("telemetries.csv"))

    dataframe = pd.DataFrame(data)
    # Convertit toutes les colonnes en types numériques (float/int)
    dataframe = dataframe.apply(pd.to_numeric)
    time_x = dataframe["Time"]
    rpm_y = dataframe["Water Temp"]

    data_correlation = dataframe[["Time", "Water Temp", "RPM", "Steering Angle","Pitch Angle"]]

    # print(data_correlation.corr())
    sns.heatmap(data_correlation.corr(), annot=True, cmap="Reds")
    plt.show()



    plt.plot(time_x, rpm_y)
    plt.show()

if (__name__ == "__main__"):
    main()
