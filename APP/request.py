from fastapi import FastAPI
import uvicorn
import UI_all_CSV_DB.classified_phishing_csv as classified
import json
app = FastAPI()

@app.get("/{dic}")
async def root(dic):
    dic = json.loads(dic)
    res , name = classified_phishing_csv.predict_by_input_of_spsific_columns(dic_input=dic)
    return {"Hello World":res}

if __name__ == "__main__":
    classified_phishing_csv = classified.classified()
    uvicorn.run(app, host="127.0.0.1", port=8000)
