import pandas
import pandas as pd
import  numpy as np
def clean_nall_and_duplicates(df : pandas.DataFrame):
        if 'Unnamed: 0' in df.columns:

                df.drop(columns=['Unnamed: 0'], inplace=True)

        df =  df.dropna().drop_duplicates().reset_index(drop=True)

        return df


