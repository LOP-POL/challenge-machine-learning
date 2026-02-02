from cleanup import dataset
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, LabelEncoder


def impute(dataFrame: pd.DataFrame)->pd.DataFrame:
    return dataFrame

def scale(dataFrame: pd.DataFrame)->pd.DataFrame:
    return dataFrame

def encode(dataFrame)->pd.DataFrame:
    return dataFrame


def main():
    ready_model_for_feature_selection = encode(scale(impute(dataset)))
    return 