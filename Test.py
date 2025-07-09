import pandas as pd
import DATA_CSV.clean_data
import class_Naive_Bayes
import  copy



class test:
    def __init__(self , df):
        self.len_df = len(df)
        self.df_30 = df[df.index < int(self.len_df * 0.3)]
        self.df_70 = df[df.index >= int(self.len_df * 0.3)]
        # self.df_30 = df[df.index>60]
        # self.df_70 = df[df.index<7560]
        self.Naive_Bayes = class_Naive_Bayes.Naive_Bayes(self.df_70)
        self.list_of_dicts = self.df_30.to_dict(orient='records')


    def get_list_dic_predict(self):
        list_dic_predict = copy.deepcopy(self.list_of_dicts)
        self.Naive_Bayes.get_dic_after_updetes()
        for dic_row in self.list_of_dicts:
            dic_row[self.Naive_Bayes.target_column] = self.Naive_Bayes.predict_by_row(dic_row)
        return list_dic_predict

    def check_good(self):
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