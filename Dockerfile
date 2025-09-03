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

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_app.py"]