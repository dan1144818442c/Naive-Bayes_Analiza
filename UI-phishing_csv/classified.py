import DATA_CSV
import pandas as pd
import Test
import class_Naive_Bayes


class classified:
    def __init__(self):
        data_frame = DATA_CSV.clean_data.clean_nall_and_duplicates(pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv" ,index_col='Index'))
        self.Accuracy_percentages = Test.test(data_frame).check_good()
        self.Naive_Bayes = class_Naive_Bayes.Naive_Bayes(data_frame)
        self.dic_percentages = self.Naive_Bayes.get_dic_after_updetes()
    def predict_by_input(self):
        return self.Naive_Bayes.predict_by_input()

a =classified()
while True:
    print(f"Accuracy_percentages : {a.Accuracy_percentages}")
    answer = a.predict_by_input()
    print(answer)
    print("#######################################3##############################################################3")

