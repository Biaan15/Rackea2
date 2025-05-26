import socket
import time

SERVER_IP = '192.168.1.24'  # Cambiar a la IP del servidor en la red o internet
PORT = 12345
INTERVALO_SEGUNDOS = 1
TOTAL_PAQUETES = 10
NOMBRE_GRUPO = "Rackea2"

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        for i in range(1, TOTAL_PAQUETES + 1):
            mensaje = f"{NOMBRE_GRUPO}_{i}"
            s.sendall(mensaje.encode())
            print(f"Enviado: {mensaje}")
            time.sleep(INTERVALO_SEGUNDOS)

if __name__ == "__main__":
    start_client()