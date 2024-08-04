# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o script e os arquivos de requisitos para o contêiner
COPY mqtt_to_http.py .
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o script
CMD ["python", "mqtt_to_http.py"]
