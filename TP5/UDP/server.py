import socket
from datetime import datetime

HOST = '0.0.0.0'
PORT = 12345
LOG_FILE = 'server_udp_log.txt'

def log_event(mensaje):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} Recibido: {mensaje}\n")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"Servidor UDP escuchando en {HOST}:{PORT}...")
        while True:
            data, addr = s.recvfrom(1024)
            mensaje = data.decode()
            print(f"Recibido de {addr}: {mensaje}")
            log_event(mensaje)

if __name__ == "__main__":
    start_server()
