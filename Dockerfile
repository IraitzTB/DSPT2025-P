FROM python:3.12

RUN mkdir app

COPY app/ app/

RUN mkdir modelo

COPY modelo/ modelo/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_app.py"]