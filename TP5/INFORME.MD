 \( t_{\text{envio},i} \): Timestamp de envío desde el cliente
- \( t_{\text{recepcion},i} \): Timestamp de recepción en el servidor
- \( L_i = t_{\text{recepcion},i} - t_{\text{envio},i} \): Latencia del paquete \( i \)

#### 1. Latencia promedio:
\[
\text{Latencia}_{\text{promedio}} = \frac{1}{N} \sum_{i=1}^{N} L_i
\]
