from fastapi import FastAPI, Request , HTTPException
import uvicorn

import model.Base_classified as Base_classified
import json
import pandas as pd
from DATA_CSV.clean_data import clean_nall_and_duplicates
import logging_.Logging
from main import Test,class_Naive_Bayes
import DATA_CSV

app = FastAPI()

df_phishing = pd.read_csv("../DATA_CSV/CSV_phishing.csv", index_col='Index')
df_phishing_clean = clean_nall_and_duplicates(df_phishing)
test = Test.test(df_phishing_clean)
class_Naive_Bayes_df_phishing = class_Naive_Bayes.Naive_Bayes(df_phishing_clean,target_column='Label')
dic_df_phishing = class_Naive_Bayes_df_phishing.get_dic_after_updetes()
dic_detiels_target = class_Naive_Bayes_df_phishing.dic_detiels_target
# phishing_classifier = Base_classified.classified(data_frame=df_phishing_clean, target_column='Label')
# logging_.Logging.Log("CREATE  phishing_classifier ")
# df_computer = pd.read_csv("DATA_CSV/CSV_buy_comuter.csv", index_col='id')
# df_computer_clean = clean_nall_and_duplicates(df_computer)
# computer_classifier = Base_classified.classified(data_frame=df_computer_clean, target_column='Category')
#
# df_titanic = pd.read_csv("DATA_CSV/CSV_titanic.csv")
# df_titanic_clean = clean_nall_and_duplicates(df_titanic)
# titanic_classifier = Base_classified.classified(data_frame=df_titanic_clean, target_column='Survived')

Percentage_dictionary = {
    # 'df_titanic': dic_df_phishing,
    # 'df_computer': computer_classifier,
    'df_phishing': {"dic":dic_df_phishing , "target_column" : "Label" , "dic_detiels_target":dic_detiels_target}
}

@app.get("/dic_predict/{database_name}")
async def predict(database_name: str, request: Request):
    return Percentage_dictionary[database_name]

if __name__ == "__main__":


    uvicorn.run(app, host="0.0.0.0", port=8000)
