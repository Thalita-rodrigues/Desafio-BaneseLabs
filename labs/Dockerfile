FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pandas pyarrow scikit-learn joblib streamlit pydantic

EXPOSE 8000 8501

CMD ["/bin/sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run ui_streamlit.py --server.port 8501 --server.address 0.0.0.0"]
