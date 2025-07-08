import pandas as pd
import numpy as np

import DATA_CSV.clean_data


class Naive_Bayes:
    def __init__(self , df):
        self.df = df
        self.dict_ = {}
        self.target_column = self.df.columns[-1]
    def  get_dict_and_enter_df(self):

        pass


    def get_df_Target_variable(self):
        df_Target_variable  = self.df.value_counts(self.target_column)
        return df_Target_variable

    def get_dic_of_detelis_Target_variable(self):
        df_target = self.get_df_Target_variable()
        dic_deteils_target = {}
        for key, val in df_target.items():
            dic_deteils_target[key] = val

        return dic_deteils_target

    def get_all_dic_with_0(self):
        val_target = self.get_dic_of_detelis_Target_variable().keys()

        for key in val_target:
            self.dict_[key] = {}
            for colum in self.columsname_without_target():
                self.dict_[key][colum] = self.get_dic_of_val_count_with_0(colum)

        return self.dict_


    def columsname_without_target(self):
        columns = self.df.columns
        list_resulot = [col for col in columns if col != self.target_column]
        return list_resulot

    def get_dic_of_val_count_with_0(self,column):
        dic = {}
        for val in self.df.value_counts(column).index.to_list():
            dic[val] = 0
        return dic




df = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv" , index_col='id')
df = DATA_CSV.clean_data.clean_nall_and_duplicates(df)
# print(df)
n = Naive_Bayes(df)
print(n.get_dic_of_val_count_with_0('age'))
# print(n.get_dic_with_all_static())


