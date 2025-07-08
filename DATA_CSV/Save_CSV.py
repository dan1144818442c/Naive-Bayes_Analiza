import pandas as pd
import clean_data
def save_CSV():
    df = pd.read_csv(r"C:\Users\1\Downloads\data for NB buys computer - Sheet1 (1).csv" , index_col= 'id')
    df =  clean_data.clean_nall_and_duplicates(df)
    df.to_csv('CSV_buy_comuter.csv')
save_CSV()