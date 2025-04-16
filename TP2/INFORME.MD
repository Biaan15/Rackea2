














----------------PARTE 4 LUEGO BORRO ESTO ------------------------------------------------------------------------------------------------------------------------------

Se analiza el rendimiento **TCP** y **UDP** bajo dos configuraciones: _Cliente_ y _Servidor_.
Las pruebas se llevaron a cabo utilizando la herramienta iPerf3, que permitió establecer conexiones específicas entre las direcciones IP asignadas al cliente y al servidor. En este caso, el **Cliente** (tanto TCP como UDP) inició la comunicación desde la IP `10.10.10.11`, mientras que el **Servidor** (tanto TCP como UDP) respondió desde la IP `10.10.10.10`.

### **Protocolo TCP Cliente y Servidor**

**Resultados comparativos**

A través de las _figuras 11 y 12_, que se mostraron con anterioridad, podemos concluir lo siguiente:

| Parámetro| TCP Cliente| TCP Servidor|
|----------|----------|----------|
| **Ancho de banda promedio**    | 896 Mbits/seg  | 896 Mbits/seg  |
| **Duración de la prueba**    | 10.00 seg | 10.01 seg   |
| **Tamaño promedio de paquetes**    | 106.8 MBytes   | 106.9 MBytes|
| **Pérdida de paquetes**    | No detectada | No detectada   | |

El tamaño promedio de los paquetes se calculó tomando los valores de datos transferidos en cada intervalo (en MBytes) y obteniendo su promedio aritmético. Esto significa que se sumaron todos los tamaños de transferencia para cada intervalo de tiempo (habitualmente de 1 segundo) y luego se dividió entre el número total de intervalos:

$$ \text{Tamaño promedio} = \frac{Suma de los tamaños de paquetes por intervalo}{Número total de intervalos} $$

En ambas pruebas no se detectó pérdida de paquetes. Esto se debe a la estabilidad del protocolo TCP, que maneja de forma eficiente la transmisión de datos mediante retransmisiones en caso de errores. Además, la estabilidad observada en el ancho de banda promedio **(896 Mbits/seg)** en ambos casos indica que no hubo interrupciones significativas en la conexión. Por lo tanto, no se observó una relación directa entre los parámetros evaluados y la pérdida de paquetes en el entorno de prueba controlado. 

### **Protocolo UDP Cliente y Servidor**

**Resultados comparativos**

A través de las _figuras 13 y 14_, podemos observar las siguientes características:

| Parámetro| UDP Cliente| UDP Servidor|
|----------|----------|----------|
| **Ancho de banda promedio**    | 1.04 Mbits/seg  | 1.04 Mbits/seg  |
| **Duración de la prueba**    | 10.01 seg | 10.01 seg   |
| **Tamaño promedio de paquetes**    | 127.2 KBytes   | 126.4 KBytes   |
| **Jitter promedio**    | 0.216 ms | 0.216 ms   |
| **Pérdida de paquetes**    | 1/159 (0.63%) | 1/159 (0.63%)   | |

En ambas pruebas UDP, se observó una pérdida mínima de paquetes *(0.63%)*. Este comportamiento está relacionado con la naturaleza del protocolo UDP, ya que no cuenta con mecanismos para retransmitir paquetes perdidos. A pesar de esto, el jitter promedio fue bajo *(0.216 ms)*, lo que indica que las variaciones en el tiempo de llegada de los paquetes tuvieron un impacto reducido en la calidad de la conexión. El _jitter_ se refiere a las fluctuaciones en el tiempo que tardan los paquetes en llegar al destino, las cuales, cuando son bajas, aseguran estabilidad en la transmisión de datos. 

En las pruebas realizadas con los protocolos UDP y TCP, se observan diferencias notables en su desempeño y características. **TCP** garantiza la entrega de datos mediante retransmisiones y confirmaciones, lo que resultó en la ausencia de pérdida de paquetes en las pruebas. Su desempeño mostró estabilidad en el ancho de banda y tamaño de transferencia, confirmando su fiabilidad en entornos controlados. 

Por otro lado, **UDP** registró una pérdida mínima de paquetes y un promedio bajo de jitter. UDP prioriza la velocidad y la simplicidad sobre la confiabilidad, lo que lo hace más susceptible a la pérdida de datos en redes más dinámicas. 

----------------------------fin-------------------------------------------------------------------------------------------------------------------------------------
