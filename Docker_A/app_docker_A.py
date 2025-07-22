from fastapi import FastAPI, Request , HTTPException
import uvicorn
import logging_
import Base_classified as Classified
import requests
app = FastAPI()


@app.get("/predict/{database_name}")
async def predict(database_name: str, request: Request):
    url = f"http://localhost:8000/dic_predict/{database_name}"
    response = requests.get(url)
    data = response.json()
    dic_percentages = data["dic"]
    target_column = data["target_column"]
    dic_detiels_target = data["dic_detiels_target"]
    classified = Classified.classified(dic_percentages=dic_percentages ,dic_detiels_target=dic_detiels_target , target_column=target_column)

    query = dict(request.query_params)
    print(query)
    logging_.Logging.Log("Sends a dictionary from the server to the classifier and receives a response")
    res, name = classified.predict_by_input_of_spsific_columns(dic_input=query)
    return {
        "target": name,
        "result": res
    }
if __name__ == "__main__":


    uvicorn.run(app, host="0.0.0.0", port=8001)
