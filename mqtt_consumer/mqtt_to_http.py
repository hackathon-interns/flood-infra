import paho.mqtt.client as mqtt
import requests
import json
import logging


# Configurações do broker MQTT
BROKER = "mqtt-broker"  # Endereço do broker MQTT
PORT = 1883  # Porta para conexão
TOPIC = "sensors/"  # Tópico para subscrição

# Configurações do endpoint HTTP
HTTP_ENDPOINT = "http://localhost:8080/api/device-data/"

# Função de callback para conexão


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Inscreve-se no tópico
    client.subscribe(TOPIC)

# Função de callback para mensagens recebidas


def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
    try:
        # Envia os dados para o endpoint HTTP
        response = requests.post(HTTP_ENDPOINT, json=json.loads(msg.payload))
        print(f"HTTP Status Code: {response.status_code}")
        if response.status_code == 200 or response.status_code == 201:
            pass
        else:
            print(f"Response Body: {response.text}")
    except json.JSONDecodeError:
        print("Error decoding JSON from MQTT message")
    except requests.RequestException as e:
        print(f"Error sending data to HTTP endpoint: {e}")


# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao broker MQTT
client.connect(BROKER, PORT, 60)

# Loop para manter a conexão
client.loop_start()

try:
    # Manter o script em execução
    while True:
        pass
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    # Encerrar o loop e desconectar
    client.loop_stop()
    client.disconnect()
