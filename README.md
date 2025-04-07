# Proyecto-SDN-NETCONF
# Proyecto SDN con NETCONF para Redes de Satélites LEO

## Información General

**Título del Proyecto:**

Proyecto de desarrollo de un controlador SDN (Software Defined Networking) utilizando el protocolo NETCONF, enfocado en gestionar la movilidad de una red distribuida de satélites LEO (como Iridium o Starlink).

**Descripción breve:**

Este proyecto simula un controlador SDN conectado mediante SSH simulando NETCONF, que permite gestionar una red distribuida de satélites implementados como contenedores Docker. Se enfoca especialmente en adaptar el plano de control (control plane) a la movilidad propia de redes satelitales LEO.

---

## Objetivo Principal

Implementar un plano de control flexible, capaz de adaptarse dinámicamente a cambios de topología debido al movimiento continuo de los satélites en órbitas bajas.

---

## Lenguaje y Herramientas

- **Docker y Docker Compose** para simular satélites y la infraestructura de red.
- **Python 3** para desarrollar el controlador SDN.
- Librería **`ncclient`** para interacción vía protocolo NETCONF.

---

##  Estructura del Proyecto

```
proyecto-netconf-sdn-simulado/
├── README.md
├── docker-compose.yml
├── controlador
│   └── controlador.py
└── satelite
    ├── Dockerfile
    └── start.sh
```

- **`README.md`**: Documentación sobre requisitos e instrucciones de ejecución.
- **`docker-compose.yml`**: Configuración para creación y gestión de contenedores Docker que simulan los satélites.
- **`controlador/controlador.py`**: Implementación del controlador SDN utilizando Python y NETCONF.
- **`satelite/Dockerfile` y `start.sh`**: Archivos necesarios para configurar y ejecutar satélites simulados.

---

##  Ejecución del Proyecto

### 1. Construir e iniciar los satélites (contenedores Docker)

```bash
sudo docker compose up --build -d
```

### 2. Ejecutar el controlador SDN

```bash
cd controlador
python3 controlador.py
```

### 3. Simular movilidad de satélites

```bash
sudo docker stop satelite2
python3 controlador.py
sudo docker start satelite2
```

---
