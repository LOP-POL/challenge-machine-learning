import csv
import pandas as pd
import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "raw"

dataset = pd.read_csv(os.path.join(script_dir, rel_path, "data_injection_molding.xlsx"))




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
