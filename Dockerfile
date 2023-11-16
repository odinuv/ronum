FROM python:3.11-slim

EXPOSE 8501
RUN python -m pip install --no-cache-dir --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir .

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
