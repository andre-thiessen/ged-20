import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_label(df: pd.DataFrame) -> pd.DataFrame:
    EPS = 0.1   # evita divisão por zero para devices sem son_hrs registrado
    df["drain_rate"] = df["dchrg_diff"] / (df["son_hrs"] + EPS)   # % por hora  
    thr_rate = df["drain_rate"].quantile(0.90)
    
    def make_label(row):
        drain_flag = row["drain_rate"] > thr_rate
        health_flag = (row["full_cap_min"] < 2800)
        return int(drain_flag and health_flag)
    
    df["label_ineficiente"] = df.apply(make_label, axis=1)
    return df