import csv
import pandas as pd
import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "raw"

dataset = pd.read_excel(os.path.join(script_dir, rel_path, "data_injection_molding.xlsx"), skiprows=77)

dataset.info()
dataset.head()
dataset.describe()

print(dataset.isnull().sum())
print("----------------------------------------------------")
print(dataset.duplicated().sum())

def main():
    return dataset
if __name__ == "main":
    main()
    