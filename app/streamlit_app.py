import streamlit as st
import joblib
import pandas as pd
import os

# Cargar el modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../modelo/iris.joblib')
model = joblib.load(MODEL_PATH)

st.title('Clasificador de Iris')
st.write('Introduce los valores de las características para predecir la especie de la flor Iris:')

sepal_length = st.number_input('Longitud del sépalo (cm)', min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input('Anchura del sépalo (cm)', min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input('Longitud del pétalo (cm)', min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input('Anchura del pétalo (cm)', min_value=0.0, max_value=10.0, value=0.2)

if st.button('Predecir'):
    features = pd.DataFrame(
        {
            "sepal length (cm)" : [sepal_length],
            "sepal width (cm)" : [sepal_width],
            "petal length (cm)" : [petal_length],
            "petal width (cm)" : [petal_width],
        }
    )
    pred = model.predict(features)[0]
    st.success(f'La especie predicha es: {pred}')
