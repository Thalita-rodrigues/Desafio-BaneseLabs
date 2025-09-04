install:
	pip install -r requirements.txt || pip install fastapi uvicorn pandas pyarrow scikit-learn joblib streamlit pydantic

run-api:
	uvicorn app:app --reload --port 8000

run-ui:
	streamlit run ui_streamlit.py --server.port 8501

train:
	python train.py

test:
	pytest -q
