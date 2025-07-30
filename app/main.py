import os
import joblib
import pandas as pd
from fastapi import FastAPI

# Aplicación
app = FastAPI()

# Cargar modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../modelo/iris.joblib')
model = joblib.load(MODEL_PATH)

# GET
@app.get("/")
def read_root():
    return {"servidor" : "iris-predict", "version" : "0.2"}

# GET
@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length : float, petal_width: float):

    # Ejecuta el predict de mi modelo
    features = pd.DataFrame(
        {
            "sepal length (cm)" : [sepal_length],
            "sepal width (cm)" : [sepal_width],
            "petal length (cm)" : [petal_length],
            "petal width (cm)" : [petal_width],
        }
    )
    pred = model.predict(features)[0]

    return {"y": pred }
