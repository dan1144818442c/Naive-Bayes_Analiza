import pandas as pd
import  numpy as np
def clean_nall_and_duplicates(df):
    df = df.drop_duplicates()
    df = df.dropna()

    return df


