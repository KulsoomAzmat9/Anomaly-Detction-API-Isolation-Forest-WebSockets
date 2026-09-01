from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import asyncio
import random
from sklearn.ensemble import IsolationForest
import numpy as np

app = FastAPI()

# Train model once
model = IsolationForest(contamination=0.15, random_state=42)
X_train = np.random.randn(200, 2)
model.fit(X_train)

@app.get("/")
async def get_dashboard():
    return FileResponse("dashboard.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Dashboard Connected")
    try:
        while True:
            # 20% chance to make an obvious anomaly so you see red
            if random.random() < 0.2:
                x = random.uniform(4, 6)
                y_value = random.uniform(4, 6)
            else:
                x = random.uniform(-2, 2)
                y_value = random.uniform(-2, 2)

            data_point = np.array([[x, y_value]])
            is_anomaly = model.predict(data_point)[0] == -1

            await websocket.send_json({"x": x, "y": y_value, "is_anomaly": bool(is_anomaly)})
            await asyncio.sleep(0.8) # faster updates

    except WebSocketDisconnect:
        print("Dashboard Disconnected")