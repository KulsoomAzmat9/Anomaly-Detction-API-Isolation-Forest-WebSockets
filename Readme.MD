Real-Time Anomaly Detection Dashboard
 Isolation Forest + FastAPI + WebSockets + Chart.js.

Built with FastAPI + Scikit-learn for real-time ML visualization.

Algorithm Used: Isolation Forest
This project uses `IsolationForest` from Scikit-learn for anomaly detection. 
It’s an unsupervised algorithm that isolates anomalies because they are few and different from normal data. 
Output `1` = Normal, Output `-1` = Anomaly. 
Chosen because it’s fast and works well for real-time data.

A live dashboard that detects anomalies in real-time and plots them on a scatter chart.

What it does
1.  Trains an IsolationForest model to learn "normal" data
2.  Streams new data points every 0.8 seconds via WebSocket
3.  Shows *Blue dots* = Normal data
4.  Shows *Red dots* = Anomalies detected by the model

#Tech Stack*
- *Backend*: Python, FastAPI, Uvicorn, Scikit-learn, NumPy
- *Frontend*: HTML, JavaScript, Chart.js
- *Protocol*: WebSock

How to Run

 Install dependencies
    ```bash
    pip install -r requirements.txt.

.  Start the server
    py -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload

 Open Dashboard  
    Go to your browser: http://127.0.0.1:8000/

    The chart will start automatically. Wait 10-20 seconds to see red anomaly dots appear.
