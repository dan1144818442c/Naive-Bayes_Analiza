import pandas
import pandas as pd
import  numpy as np
def clean_nall_and_duplicates(df : pandas.DataFrame):
        return df.dropna().drop_duplicates().reset_index(drop=True)


