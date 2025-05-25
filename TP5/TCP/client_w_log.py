import socket
import time
from datetime import datetime

SERVER_IP = '127.0.0.1'
PORT = 12345
INTERVALO_SEGUNDOS = 1
TOTAL_PAQUETES = 10
NOMBRE_GRUPO = "GrupoX"
LOG_FILE = 'client_log.txt'

def log_event(mensaje):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} Enviado: {mensaje}\n")

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        for i in range(1, TOTAL_PAQUETES + 1):
            mensaje = f"{NOMBRE_GRUPO}_{i}"
            s.sendall(mensaje.encode())
            print(f"Enviado: {mensaje}")
            log_event(mensaje)
            time.sleep(INTERVALO_SEGUNDOS)

if __name__ == "__main__":
    start_client()
