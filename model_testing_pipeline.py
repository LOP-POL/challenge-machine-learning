import csv
import pandas as pd
import os
import re
import joblib
from autogluon.tabular import TabularPredictor

script_dir = os.path.dirname(__file__)
rel_path = "raw"

final_dataset = pd.read_excel(os.path.join(script_dir, rel_path, "eval_set_1_no_target.xlsx"))

modelfile = ("autogluon_models")
# modelfile = "pkl\mlp_optimized.pkl"
# scalerfile = "pkl\mlp_scaler.pkl"
output = "eval_set_1_with_target.xlsx"
SZx = "SZx [Sch]"
# features = ["ZSx [s]", "ACPx [cm³]", "ZDx [s]", "ZEx [s]", "GEx [kWh]", "H16x [°C]", "H10x [°C]"]
features = ['ZUs [s]', 'ZSx [s]', 'ACPx [cm³]', 'ZDx [s]', 'ZEx [s]', 'APHu [bar]', 'GEx [kWh]', 'GPx [kW]', 'HPx [kW]', 'HEx [kWh]', 'MPx [kW]', 'ESPx [kWh/kg]', 'H16x [°C]', 'H15x [°C]', 'H10x [°C]', 'H12x [°C]', 'H9x [°C]', 'H11x [°C]']

# final_dataset = final_dataset[final_dataset['ZDx [s]'] > 0.1]
# final_dataset = final_dataset[final_dataset['ZDx [s]'] < final_dataset['ZDx [s]'].quantile(0.999)]
# final_dataset = final_dataset[final_dataset['ZSx [s]'] >= final_dataset['ZSx [s]'].quantile(0.005)]
# final_dataset = final_dataset[final_dataset['ZUs [s]'] >= final_dataset['ZUs [s]'].quantile(0.005)]
# final_dataset = final_dataset[final_dataset['ZUs [s]'] <= final_dataset['ZUs [s]'].quantile(0.999)]

colms_to_drop = ['StZx [Stk]', 'Datum [ ]', 'Zeit [ ]']
final_dataset = final_dataset.drop(columns=[c for c in colms_to_drop if c in final_dataset.columns])

# scaler = joblib.load(scalerfile)
# scaleddata = scaler.transform(final_dataset[features])
#
# model = joblib.load(modelfile)
# preds  = model.predict(scaleddata)

model = TabularPredictor.load(modelfile)
preds = model.predict(final_dataset[features])


result = pd.DataFrame({SZx: final_dataset[SZx],"failure": preds})


result.to_excel(output, index=False)
