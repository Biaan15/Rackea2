import socket
from datetime import datetime
from cryptography.fernet import Fernet

HOST = '0.0.0.0'
PORT = 12345
LOG_FILE = 'server_encrypted_log.txt'

FERNET_KEY = b'9nDAkanw82eYdCFv_ODKRmo5Bm_RlBov5CzO_fRodRs='
fernet = Fernet(FERNET_KEY)

def log_event(mensaje):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} Recibido: {mensaje}\n")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Conexión establecida con {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    mensaje = fernet.decrypt(data).decode()
                except Exception as e:
                    print("Error al desencriptar:", e)
                    continue
                print(f"Recibido: {mensaje}")
                log_event(mensaje)

if __name__ == "__main__":
    start_server()
