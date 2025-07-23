import pandas
import pandas as pd
import DATA_CSV
import  numpy as np
def clean_nall_and_duplicates(df : pandas.DataFrame):
        if 'Unnamed: 0' in df.columns:
                df.drop(columns=['Unnamed: 0'], inplace=True)
        df =  df.dropna().drop_duplicates().reset_index(drop=True)

        return df


def get_clean_data(name_of_data):
        if name_of_data == "CSV_titanic":
                return DATA_CSV.clean_data.clean_nall_and_duplicates(pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_titanic.csv" ) )
        elif name_of_data == "CSV_phishing":
                return DATA_CSV.clean_data.clean_nall_and_duplicates(pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv" ,index_col='Index'))
        elif name_of_data == "CSV_buy_comuter":
                return DATA_CSV.clean_data.clean_nall_and_duplicates(pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv" ,index_col='id') )

def get_clean_df( file_path, index_col, preprocess_fn):
    df = pd.read_csv(file_path, index_col=index_col)
    return preprocess_fn(df)
