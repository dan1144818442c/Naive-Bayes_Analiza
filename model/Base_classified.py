import DATA_CSV
import pandas as pd
import Test
import class_Naive_Bayes
import logging_.Logging


class classified:
    def __init__(self  ,data_frame  , target_column = False):
        self.Accuracy_percentages = Test.test(data_frame , target_column=target_column).check_good()
        self.Naive_Bayes = class_Naive_Bayes.Naive_Bayes(data_frame,target_column)
        self.dic_percentages = self.Naive_Bayes.get_dic_after_updetes()
        self.dic_detiels_target = self.Naive_Bayes.dic_detiels_target
        self.name_target_column = self.Naive_Bayes.target_column

    def predict_by_input_of_all_columns(self):
        return self.Naive_Bayes.predict__by_full_dic_columns(self.Naive_Bayes.get_dic_by_input())

    def predict_by_input_of_spsific_columns(self , dic_input):
        logging_.Logging.Log("Identifies according to a given dictionary.")
        dic_res = {}
        for target , val in self.dic_percentages.items():
            predict = 1
            for column , val_column in dic_input.items():
                try:
                    # print(int(val_column))
                    # print(val[column])
                    # print(column)
                    predict *= val[column][int(val_column)]

                except:
                    predict *= val[column][val_column]

            target_percent = (self.dic_detiels_target[target])/ (sum(self.dic_detiels_target.values()))
            predict *= target_percent
            dic_res[target] = predict
        max_key = max(dic_res, key=dic_res.get)
        return max_key , self.name_target_column

        # return self.Naive_Bayes.predict__by_dic(dic_input)



# a =classified().predict_by_input()
