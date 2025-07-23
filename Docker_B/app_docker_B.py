from fastapi import FastAPI, Request
import uvicorn
import pandas as pd

from DATA_CSV.clean_data import clean_nall_and_duplicates
import Test, class_Naive_Bayes

app = FastAPI()


# df_phishing
df_phishing = pd.read_csv("DATA_CSV/CSV_phishing.csv", index_col='Index')
df_phishing_clean = clean_nall_and_duplicates(df_phishing)
df_phishing_test = Test.test(df_phishing_clean)
df_phishing_Accuracy_percentages = df_phishing_test.check_good()
df_phishing_class_Naive_Bayes = class_Naive_Bayes.Naive_Bayes(df_phishing_clean, target_column='class')
dic_df_phishing = df_phishing_class_Naive_Bayes.get_dic_after_updetes()
df_phishing_dic_detiels_target = df_phishing_class_Naive_Bayes.dic_detiels_target
df_phishing_target_column = df_phishing_class_Naive_Bayes.target_column
# logging_.Logging.Log("CREATE  phishing_classifier ")


# df_computer
df_computer = pd.read_csv("DATA_CSV/CSV_buy_comuter.csv", index_col='id')
df_computer_clean = clean_nall_and_duplicates(df_computer)
df_computer_test = Test.test(df_computer_clean)
df_computer_Accuracy_percentages = df_computer_test.check_good()
df_computer_class_Naive_Bayes  = class_Naive_Bayes.Naive_Bayes(df=df_computer_clean, target_column='Category')
dic_df_computer = df_computer_class_Naive_Bayes.get_dic_after_updetes()
df_computer_dic_detiels_target = df_computer_class_Naive_Bayes.dic_detiels_target
df_computer_target_column = df_computer_class_Naive_Bayes.target_column

# df_titanic

df_titanic = pd.read_csv("DATA_CSV/CSV_titanic.csv")
df_titanic_clean = clean_nall_and_duplicates(df_titanic)
df_titanic_test = Test.test(df_titanic_clean)
df_titanic_Accuracy_percentages = df_titanic_test.check_good()
df_titanic_class_Naive_Bayes  = class_Naive_Bayes.Naive_Bayes(df=df_titanic_clean, target_column='Survived')
dic_df_titanic = df_titanic_class_Naive_Bayes.get_dic_after_updetes()
df_titanic_dic_detiels_target = df_titanic_class_Naive_Bayes.dic_detiels_target
df_titanic_target_column = df_titanic_class_Naive_Bayes.target_column


# logging_.Logging.Log("CREATE  phishing_classifier ")

# df_titanic = pd.read_csv("DATA_CSV/CSV_titanic.csv")
# df_titanic_clean = clean_nall_and_duplicates(df_titanic)
# titanic_classifier = Base_classified.classified(data_frame=df_titanic_clean, target_column='Survived')

Percentage_dictionary = {
    # 'df_titanic': dic_df_phishing,
    # 'df_computer': computer_classifier,
    'df_phishing': {"dic":dic_df_phishing ,
                    "target_column" : df_phishing_target_column,
                    "dic_detiels_target":df_phishing_dic_detiels_target ,
                    "Accuracy percentages" : df_phishing_Accuracy_percentages},

    'df_computer': {"dic":dic_df_computer ,
                    "target_column" : df_computer_target_column,
                    "dic_detiels_target":df_computer_dic_detiels_target ,
                    "Accuracy percentages" : df_computer_Accuracy_percentages} ,
    'df_titanic': {"dic":dic_df_titanic ,
                    "target_column" : df_titanic_target_column,
                    "dic_detiels_target":df_titanic_dic_detiels_target ,
                    "Accuracy percentages" : df_titanic_Accuracy_percentages}

}

@app.get("/dic_predict/{database_name}")
async def predict(database_name: str, request: Request):
    return Percentage_dictionary[database_name]

if __name__ == "__main__":


    uvicorn.run(app, host="0.0.0.0", port=8000)
