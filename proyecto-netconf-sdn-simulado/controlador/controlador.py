import paramiko
from ncclient import manager

#  Forzamos el tipo de clave aceptada
paramiko.transport._preferred_keys = ['ssh-rsa']

def conectar_nodo(host, port, username, password):
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            allow_agent=False,
            look_for_keys=False,
            timeout=5
        ) as m:
            print(f"✅ Conectado a {host}:{port}")
            print(" Capabilities simuladas:")
            for cap in m.server_capabilities:
                print(cap)
    except Exception as e:
        print(f"❌ No se pudo conectar a {host}:{port} → {e}")

if __name__ == "__main__":
    nodos = [
        {"host": "localhost", "port": 8301, "username": "netconf", "password": "netconf"},
        {"host": "localhost", "port": 8302, "username": "netconf", "password": "netconf"},
        {"host": "localhost", "port": 8303, "username": "netconf", "password": "netconf"}
    ]
    for nodo in nodos:
        conectar_nodo(**nodo)

