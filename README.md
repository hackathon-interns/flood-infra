# Projeto de Monitoramento de Sensores de Enchentes

Este projeto utiliza Docker Compose para configurar um broker MQTT e um serviço adicional que consome dados dos tópicos MQTT e envia para um endpoint HTTP.

## Pré-requisitos

- Docker
- Docker Compose

## Como executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Execute o Docker Compose:
    ```bash
    docker-compose up
    ```

Isso iniciará todos os serviços definidos no arquivo `docker-compose.yml`.

## Serviços

- **MQTT Broker**: Recebe dados dos sensores de enchentes.
- **Data Consumer**: Consome dados dos tópicos MQTT e envia para um endpoint HTTP.