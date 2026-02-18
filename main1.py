import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.inspection import permutation_importance
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
import joblib

script_dir = os.getcwd()
rel_path = "intermediate"

dataset = pd.read_csv(os.path.join(script_dir, rel_path, "CLEAN_eval_set_1_no_target.csv"))

knn_model = joblib.load('pkl/knn_smote.pkl')
knn_features = ['ZSx [s]', 'ACPx [cm³]', 'ZDx [s]', 'ZEx [s]', 'GEx [kWh]', 'H16x [°C]', 'H10x [°C]']
knn_input = dataset[knn_features]


knn_preds = knn_model.predict(knn_input)

script_dir = os.getcwd()
rel_path = "raw"

targets_df = pd.read_excel(os.path.join(script_dir, rel_path, "eval_set_1_with_target_example.xlsx"))

#Merge targets to dataset by SZx
aligned_data = pd.merge(dataset, targets_df, on='SZx [Sch]', how='inner')

y_true = aligned_data['failure']
X_test = aligned_data[knn_features]


# Predict using the aligned features
y_pred = knn_model.predict(X_test)

# Compare
print("KNN Model Performance")
print(f"Accuracy: {accuracy_score(y_true, y_pred)}")
print(classification_report(y_true, y_pred))