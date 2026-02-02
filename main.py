import csv
import pandas as pd
import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "raw"

dataset = pd.read_csv(os.path.join(script_dir, rel_path, "data_injection_molding.xlsx"))



