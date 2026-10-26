from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.prediction_response import PredictionResponse
from schema.input_user import UserInput
from model.predict import predict_output, model,MODEL_VERSION


app = FastAPI()
  

# Human readable
@app.get('/')
def home():
    return {
        'message':'Insurance Premium Prediction API'
        }

# Machine readable
@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'version':MODEL_VERSION,
        'model loaded': model is not None
    }

        
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data : UserInput):

    user_input = {
        'bmi' : data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier' : data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        predcition =  predict_output(user_input)

        return JSONResponse(status_code=200, content={"predicted_category":predcition})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

