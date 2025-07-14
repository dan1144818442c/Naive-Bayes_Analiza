import pandas
import pandas as pd
import DATA_CSV.clean_data
import class_Naive_Bayes
import  copy
from sklearn.model_selection import train_test_split

import logging_.Logging


class test:
    def __init__(self , df , target_column = False):
        self.len_df = len(df)
        self.df_70  , self.df_30 = train_test_split(df, test_size=0.3, random_state=42)
        # self.df_30 = df[df.index>60]
        # self.df_70 = df[df.index<7560]
        self.Naive_Bayes = class_Naive_Bayes.Naive_Bayes(self.df_70 , target_column=target_column)
        self.list_of_dicts = self.df_30.to_dict(orient='records')


    def get_list_dic_predict(self):
        self.Naive_Bayes.get_dic_after_updetes()
        list_dic_predict = []

        for dic_row in self.list_of_dicts:
            row_copy = dic_row.copy()
            row_copy[self.Naive_Bayes.target_column] = self.Naive_Bayes.predict_by_row(dic_row)
            list_dic_predict.append(row_copy)

        return list_dic_predict

    def check_good(self):
        logging_.Logging.Log("Checks the success rate of the classifier")
        num = 0
        target_column = self.Naive_Bayes.target_column
        list_dic_predict = self.get_list_dic_predict()
        for i in range(len(self.list_of_dicts)):
            if (self.list_of_dicts[i][target_column]) == (list_dic_predict[i][target_column]):
                num +=1
        return num / len(self.list_of_dicts)


# df = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv" ,index_col='Index')
# print(df.columns)
#
# print(df.shape)
# df1 = DATA_CSV.clean_data.clean_nall_and_duplicates(df)
# print(df1.shape)
# # print(df.columns)
# # df_70 = df[df[]]
# # print(dict(df_70))
# # def get_70_present(df):
#
# # n = class_Naive_Bayes.Naive_Bayes(df_70)
#
#
# # n.update_if_have_zero()
#
# # print(df_30)
# tast_ = test(df1)
# # print(tast_.list_of_dicts[7])
# # print(tast_.get_list_dic_predict()[7])
# print(tast_.check_good())
# print(len(tast_.df_30))
# print(len(tast_.df_70))
