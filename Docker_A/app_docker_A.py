from fastapi import FastAPI, Request , HTTPException
import uvicorn

import logging_
import Base_classified as Classified
import requests

app = FastAPI()

df_phishing = requests.get(r"http://data-service:80/dic_predict/df_phishing").json()
df_computer = requests.get(r"http://data-service:80/dic_predict/df_computer").json()
df_titanic = requests.get(r"http://data-service:80/dic_predict/df_titanic").json()

dic_DB = {"df_phishing":{"dic_percentages" : df_phishing["dic"] ,
                         "target_column" :df_phishing["target_column"] ,
                         "dic_detiels_target" :df_phishing["dic_detiels_target"] ,
                        "Accuracy percentages" : df_phishing["Accuracy percentages"]} ,

          "df_computer" : {"dic_percentages" : df_computer["dic"] ,
                         "target_column" :df_computer["target_column"] ,
                         "dic_detiels_target" :df_computer["dic_detiels_target"] ,
                        "Accuracy percentages" : df_computer["Accuracy percentages"]} ,

          "df_titanic" : {"dic_percentages" : df_titanic["dic"] ,
                         "target_column" :df_titanic["target_column"] ,
                         "dic_detiels_target" :df_titanic["dic_detiels_target"] ,
                        "Accuracy percentages" : df_titanic["Accuracy percentages"]}
          }

@app.get("/predict/{database_name}")
async def predict(database_name: str, request: Request):
    data = dic_DB[database_name]
    dic_percentages = data["dic_percentages"]
    target_column = data["target_column"]
    dic_detiels_target = data["dic_detiels_target"]
    Accuracy_percentages = data["Accuracy percentages"]
    classified = Classified.classified(dic_percentages=dic_percentages ,dic_detiels_target=dic_detiels_target , target_column=target_column)

    query = dict(request.query_params)
    print(query)
    # logging_.Logging.Log("Sends a dictionary from the server to the classifier and receives a response")
    res, name = classified.predict_by_input_of_spsific_columns(dic_input=query)
    return {
        "Accuracy percentages" : Accuracy_percentages ,
        "target": name,
        "result": res
    }
if __name__ == "__main__":


    uvicorn.run(app, host="0.0.0.0", port=8001)
