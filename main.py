import csv
import pandas as pd
import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "raw"

dataset = pd.read_csv(os.path.join(script_dir, rel_path, "data_injection_molding.xlsx"))
final_dataset = pd.read_excel(os.path.join(script_dir, rel_path, "eval_set_final_secret_no_target.xlsx"))




