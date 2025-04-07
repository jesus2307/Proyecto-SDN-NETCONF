# Proyecto SDN + NETCONF (Simulación)

Este proyecto simula un controlador SDN conectado a una red de satélites (contenedores Docker) a través de SSH simulando NETCONF.

## Requisitos

- Docker
- docker-compose
- Python 3 con `ncclient`

## Ejecución

1. Construir e iniciar contenedores:

```
sudo docker compose up --build -d
```

2. Ejecutar el controlador:

```
cd controlador
python3 controlador.py
```

3. Simular movilidad:

```
sudo docker stop satelite2
python3 controlador.py
sudo docker start satelite2
```

Este sistema simula una red de satélites con conectividad cambiante.