A real-time anomaly detection dashboard built with FastAPI.
test_anomaly.py sends 100 random data points to the server. 
dashboard.html shows them live. Red dots = Anomaly, Blue = Normal.

Tech Stack
- Python 3.12
- FastAPI + Uvicorn
- HTML5 Canvas + JavaScript

Installation - PowerShell / CMD
```powershell
pip install fastapi uvicorn pydantic
How to Run - 2 PowerShell Windows

Window 1: Start the API Server
uvicorn app:app --host 127.0.0.1 --port 8000
Window 2: Start the Data Sender
python test_anomaly.py
Open Dashboard in Browser:
http://127.0.0.1:8000/dashboard
API Endpoints
Method	Endpoint	Description	Example Request / Response
GET	/	Health check. Tells if API is running	Response: {"message": "Anomaly Detector API is running"}
POST	/data	Receives a data point from test_anomaly.py	Request: {"x": 1, "y": 45.2, "is_anomaly": false}
GET	/latest	Returns the newest data point. Used by dashboard	Response: {"x": 5, "y": 82.1, "is_anomaly": true}
GET	/history	Returns last 100 data points for the graph	Response: [{"x":1,"y":45}, {"x":2,"y":51}...]
GET	/dashboard	Serves the live HTML dashboard page	Opens in browser
Example Data Format Sent to /data
{
  "x": 10,
  "y": 23.5,
  "is_anomaly": false
}
is_anomaly: true = Red dot, is_anomaly: false = Blue line