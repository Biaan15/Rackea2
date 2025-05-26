from datetime import datetime

def parse_log(filepath):
    tiempos = {}
    with open(filepath, 'r') as f:
        for linea in f:
            if 'Rackea2_' in linea:
                tiempo_str = linea[1:20]
                mensaje = linea.strip().split(': ')[-1]
                timestamp = datetime.strptime(tiempo_str, "%Y-%m-%d %H:%M:%S")
                tiempos[mensaje] = timestamp
    return tiempos

envios = parse_log('client_udp_log.txt')
recepciones = parse_log('server_udp_log.txt')

latencias = []
mensajes_comunes = sorted(set(envios.keys()) & set(recepciones.keys()), key=lambda x: int(x.split('_')[1]))

for msg in mensajes_comunes:
    envio = envios[msg]
    recepcion = recepciones[msg]
    latencia = (recepcion - envio).total_seconds()
    latencias.append(latencia)

# Cálculos
promedio = sum(latencias) / len(latencias)
lat_min = min(latencias)
lat_max = max(latencias)
jitter = sum(abs(latencias[i] - latencias[i - 1]) for i in range(1, len(latencias))) / (len(latencias) - 1)

print(f"Latencia promedio: {promedio:.3f} s")
print(f"Latencia mínima: {lat_min:.3f} s")
print(f"Latencia máxima: {lat_max:.3f} s")
print(f"Jitter: {jitter:.3f} s")
