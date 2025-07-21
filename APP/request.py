from fastapi import FastAPI, Request , HTTPException
import uvicorn
import model.Base_classified as Base_classified
import json
import pandas as pd
from DATA_CSV.clean_data import clean_nall_and_duplicates

import logging_.Logging

app = FastAPI()


@app.get("/predict/{database_name}")
async def predict(database_name: str, request: Request):
    if database_name not in classifiers :
        raise HTTPException(status_code=404, detail=f"Database '{database_name}' not found")
    else:
        model = classifiers[database_name]

    query = dict(request.query_params)
    print(query)
    logging_.Logging.Log("Sends a dictionary from the server to the classifier and receives a response")
    res, name = model.predict_by_input_of_spsific_columns(dic_input=query)
    return {
        "target": name,
        "result": res
    }


if __name__ == "__main__":
    df_phishing = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv", index_col='Index')
    df_phishing_clean = clean_nall_and_duplicates(df_phishing)
    phishing_classifier = Base_classified.classified(data_frame=df_phishing_clean, target_column='Label')

    df_computer = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv", index_col='id')
    df_computer_clean = clean_nall_and_duplicates(df_computer)
    computer_classifier = Base_classified.classified(data_frame=df_computer_clean, target_column='Category')

    df_titanic = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_titanic.csv")
    df_titanic_clean = clean_nall_and_duplicates(df_titanic)
    titanic_classifier = Base_classified.classified(data_frame=df_titanic_clean, target_column='Survived')
    classifiers = {
        'df_titanic': titanic_classifier,
        'df_computer': computer_classifier,
        'df_phishing': phishing_classifier
    }

    uvicorn.run(app, host="127.0.0.1", port=8000)
