import pandas as pd
import numpy as np

import DATA_CSV.clean_data


class Naive_Bayes:
    def __init__(self , df):
        self.df = df
        self.dict_ = {}
        self.target_column = self.df.columns[-1]
        self.dic_detiels_target = self.get_dic_of_detelis_Target_variable()

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

    def fiil_dict(self):
        dict_with_0 = self.get_all_dic_with_0()

        for key_terget  , val in dict_with_0.items():
            for column , key_column in val.items():

                for val_count  , val_of_val_count in  key_column.items():
                    num_count = self.get_num_of_val_count_in_target(name_target= self.target_column , val_target=key_terget , name_column=column ,name_valu_count=val_count)
                    num_target =self.dic_detiels_target[key_terget]
                    dict_with_0[key_terget][column][val_count] =num_count / num_target
        print(dict_with_0)




    def get_num_of_val_count_in_target(self ,  name_target , val_target , name_column , name_valu_count):
        count =self.df[(df[name_column] == name_valu_count) & (df[name_target] == val_target)].shape[0]
        return count



df = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv" , index_col='id')
df = DATA_CSV.clean_data.clean_nall_and_duplicates(df)
# print(df)
n = Naive_Bayes(df)
# print(n.get_dic_of_val_count_with_0('age'))
# print(n.get_num_of_val_count_in_target())
n.fiil_dict()

