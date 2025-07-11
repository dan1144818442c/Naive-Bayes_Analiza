from fastapi import FastAPI, Request
import uvicorn
import UI_all_CSV_DB.classified_phishing_csv as phishing_module
import UI_all_CSV_DB.classified_computer_csv as computer_module
import json

app = FastAPI()


@app.get("/predict")
async def predict(request: Request):
    query = dict(request.query_params)
    print(query)

    res, name = phishing_classifier.predict_by_input_of_spsific_columns(dic_input=query)

    return {
        "target": name,
        "result": res
    }

if __name__ == "__main__":
    phishing_classifier = phishing_module.classified()
    computer_classifier = computer_module.classified()
    uvicorn.run(app, host="127.0.0.1", port=8000)
