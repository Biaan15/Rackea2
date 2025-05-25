import socket

HOST = '0.0.0.0'  # Escucha en todas las interfaces disponibles
PORT = 12345

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
                print(f"Recibido: {data.decode()}")

if __name__ == "__main__":
    start_server()
