import DATA_CSV
import pandas as pd
import Test
import class_Naive_Bayes
from UI_all_CSV_DB.Base_classified import classified as classified_base


class classified(classified_base):
    def __init__(self):
        data_frame = DATA_CSV.clean_data.clean_nall_and_duplicates(pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv" ,index_col='Index'))
        super().__init__(data_frame)


