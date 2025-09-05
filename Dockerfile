FROM python:3.12

# Creo las carpetas para el código
RUN mkdir app
# Copio
COPY app/ app/

# Creo la carpeta del modelo y los copio
RUN mkdir modelo
COPY modelo/ modelo/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "app/streamlit_app.py"]

EXPOSE 8501