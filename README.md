# Insurance-Premium-Prediction-API
A REST API built with FastAPI that serves a trained scikit-learn model to predict a customer's insurance premium category from their profile. Requests and responses are validated with Pydantic, and a health-check endpoint reports the loaded model version.

Problem Statement

Insurance premiums are often set through manual underwriting, which is slow and can be inconsistent between customers. This project predicts the premium category of a customer from their BMI, age group, lifestyle risk, city tier, income and occupation, so quotes can be generated instantly and consistently.

This is a screening and quotation aid. It does not replace a final underwriting decision.

Features
POST /predict returns the predicted premium category
GET /health reports service status, model version and whether the model is loaded
Pydantic validation for request and response (invalid input returns 422)
Error handling with proper HTTP status codes
Interactive API docs at /docs (Swagger UI)
Tech Stack

Python, FastAPI, Uvicorn, scikit-learn, pandas, Pydantic

Model
Item	Details
Task	Multi-class classification
Target	<premium categories, e.g. Low / Medium / High>
Algorithm	<e.g. Random Forest> (compared with <e.g. Logistic Regression>)
Dataset	<dataset name and source>, <N> rows
Test macro F1	<value>
Test accuracy	<value>
Input Features
Field	Type	Description
bmi	number	Body mass index
age_group	string	Age bracket of the customer
lifestyle_risk	string	Risk level based on lifestyle habits
city_tier	integer / string	Tier of the customer's city
income_lpa	number	Annual income in lakhs per annum
occupation	string	Type of occupation
Project Structure
.
├── app.py                          # FastAPI application and routes
├── schema/
│   ├── input_user.py               # UserInput (request schema)
│   └── prediction_response.py      # PredictionResponse (response schema)
├── model/
│   ├── predict.py                  # model loading and predict_output()
│   └── model.pkl                   # trained model (see "Run Locally")
├── tests/
│   └── test_api.py                 # pytest tests
├── requirements.txt
└── README.md
Run Locally
bash
# 1. Clone the repository
git clone https://github.com/MadhavKundgir/Insurance-Premium-Prediction-API.git
cd Insurance-Premium-Prediction-API

# 2. Create a virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

# 3. Start the API
python app.py
# or: uvicorn app:app --reload

The API runs at http://127.0.0.1:8000. Open http://127.0.0.1:8000/docs to try the endpoints in the browser.

API Endpoints
GET /
json
{ "message": "Insurance Premium Prediction API" }
GET /health
json
{ "status": "ok", "version": "1.0.0", "model loaded": true }
POST /predict

Request (field names follow the UserInput schema):

json
{
  "<field>": "<value>"
}

Response

json
{ "predicted_category": "High" }

Example with curl

bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"<field>": "<value>"}'
Status codes
Code	Meaning
200	Prediction returned
422	Invalid or missing input (Pydantic validation)
500	Prediction failed inside the model
Run Tests
bash
pip install pytest httpx
pytest
Run with Docker
bash
docker build -t insurance-premium-api .
docker run -p 8000:8000 insurance-premium-api
Future Improvements
Store predictions in a database (MySQL or MongoDB) with a history endpoint
Add authentication (JWT)
Retrain endpoint and model registry
Add feature importance output for each prediction


Author :- Madhav Kundgir