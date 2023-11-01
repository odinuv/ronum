# FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install the xz-utils package
# RUN apt-get update && apt-get install -y xz-utils

# RUN [ -f packages.txt ] && sudo apt update && sudo apt upgrade -y && sudo xargs apt install -y <packages.txt; [ -f requirements.txt ] && pip3 install --user -r requirements.txt; pip3 install --user streamlit; echo '✅ Packages installed and Requirements met'

# RUN [ -f packages.txt ] && sudo apt update && sudo apt upgrade -y && sudo xargs apt install -y <packages.txt; [ -f requirements.txt ] && pip3 install -r requirements.txt; pip3 install streamlit; echo '✅ Packages installed and Requirements met'

# COPY Hello.py .
# COPY README.md .
# COPY pages .

# CMD streamlit run Hello.py --server.enableCORS false --server.enableXsrfProtection false

# EXPOSE 8501

FROM python:3.11

# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -U pip
RUN pip3 install -U streamlit
RUN pip3 install -r requirements.txt

# Copy app code and set working directory
# COPY . /app
WORKDIR /app

# Run
CMD ["streamlit", "run", "Hello.py", "--server.port=8501", "--server.address=0.0.0.0"]

