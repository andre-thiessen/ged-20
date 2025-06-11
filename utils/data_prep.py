import pandas as pd

def create_label(df: pd.DataFrame) -> pd.DataFrame:
    def make_label(row):
        return int(
            (row["dchrg_diff"] > 25)
            and ((row["full_cap_min"] < 2800) or (row["btlow_total"] > 10))
        )
    df["label_ineficiente"] = df.apply(make_label, axis=1)
    return df