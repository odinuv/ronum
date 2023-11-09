FROM python:3.11

# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir flake8 streamlit

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir .

# Copy app code and set working directory

# Run
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
