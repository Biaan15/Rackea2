## Resultados

En primer lugar se configuraron manualmente las direcciones IP en los dispositivos participantes. Cada grupo de trabajo cuenta con su propia red local. Dentro de cada red, los dispositivos (PCs) están conectados a un mismo switch, el cual a su vez se conecta a un router que actúa como puerta de enlace hacia otras redes.

En una primera instancia, la red consistió en 2 computadoras del mismo grupo conectadas a un switch mediante la interfaz fastEthernet, las cuales interactúan entre sí.

![Figura 1](imagenes/IP_10.10.10.10.png)
![Figura 2](imagenes/IP_10.10.10.11.png)

Una vez conectadas, mediante el cable UTP, se verificó la conectividad mediante comandos ICMP (ping) entre los hosts del mismo grupo.
**Ejemplo de ping entre PCs del mismo grupo:**

```bash
ping 10.10.10.10
ping 10.10.10.11
```

![Figura 3](imagenes/Ping_H2(1).png)
![Figura 4](imagenes/Ping_H1.png)

Como se puede observar, nuestro grupo se configuró en la red 10.10.10.x. La propuesta de direccionamiento por grupo planteada es:

| GRUPO | DISPOSITIVO | SUBRED          | IPV4         |
|-------|-------------|------------------|--------------|
| 0     | PC0         | 10.10.10.0/24    | 10.10.10.10  |
|       | PC1         | 10.10.10.0/24    | 10.10.10.11  |
| 1     | PC2         | 10.10.11.0/24    | 10.10.11.2   |
|       | PC3         | 10.10.11.0/24    | 10.10.11.3   |
| 2     | PC4         | 10.10.12.0/24    | 10.10.12.16  |
|       | PC5         | 10.10.12.0/24    | 10.10.12.17  |

Para probar conectividad con dispositivos de otros grupos, tenemos que tener en cuenta que estos pertenecen a redes diferentes, por lo que los paquetes que se mandan de una PC a otra en otro grupo deben ser encaminados por los routers. Esta parte no pudo ser realizada en laboratorio, por lo que fue simulada para entender a fondo la topología planteada. 

Para permitir esta comunicación entre routers, es necesario configurar interfaces con direcciones IP que pertenezcan a subredes distintas. Para estos enlaces se utilizan subredes /30, ya que solo se requiere una dirección IP para cada extremo de la conexión punto a punto. La propuesta de direccionamiento de interfaces de los routers planteada fue:

| DISPOSITIVO | INTERFAZ |   LINK HACIA          |  SUBRED           | IPV4        |
|-------------|----------|------------------|-------------|-------------|
| R0          | G0/0     | S0         | 10.10.10.0/24  | 10.10.10.1  |
|             | G0/1     | R1         | 172.16.1.0/30  | 172.16.1.1  |
|             | G0/2     | R2         | 172.16.1.4/30  | 172.16.1.5  |
| R1          | G0/0     | R0         | 172.16.1.0/30  | 172.16.1.2  |
|             | G0/1     | S1         | 10.10.11.0/24  | 10.10.11.1  |
|             | G0/2     | R2         | 172.16.1.8/30  | 172.16.1.9  |
| R2          | G0/0     | R0         | 172.16.1.4/30  | 172.16.1.6  |
|             | G0/1     | R1         | 172.16.1.8/30  | 172.16.1.10 |
|             | G0/2     | S2         | 10.10.12.0/24  | 10.10.12.1  |

Además de las IP asignadas a cada host, es importante que cada dispositivo debe tener como gateway la dirección IP de la interfaz que conecta al switch de su grupo.

En cada PC se asignó una dirección IP fija, junto con su máscara de subred y default gateway, de acuerdo al grupo al que pertenece. Ejemplo de la configuración en una de ellas:

![Figura 5](imagenes/simulacion/config_IP_host.png)

En los routers, la configuración se realizó mediante línea de comandos. Se habilitaron las interfaces necesarias y se les asignaron las direcciones IP correspondientes a cada subred, según el esquema previamente definido. Ejemplo de uno de los routers:

![Figura 6](imagenes/simulacion/config_Router.png)

Con esta configuración básica, se procedió a realizar pruebas de conectividad mediante el envío de mensajes ICMP (ping) entre distintos dispositivos de la red. Los resultados son:
Entre computadoras de una misma subred, la comunicación fue exitosa, lo que confirma que la configuración IP local y la conexión a través del switch están correctamente establecidas. Ej de ping desde PC0 hacia PC1:

![Figura 7](imagenes/simulacion/ping_PC0_PC1.png)

Entre computadoras de diferentes subredes, los intentos de ping fallaron. Esto se debe a que, si bien los routers ya tienen sus interfaces configuradas, aún no se han definido las rutas estáticas que les permitan reenviar paquetes hacia redes que no conocen directamente. Al hacer ping de PC0 a PC2 ocurre:

	![Figura 8](imagenes/simulacion/ping_PC0_PC2_sinrutas.png)

Para lograr la comunicación completa entre todas las PCs de la topología, es necesario establecer un esquema de ruteo estático que indique a cada router por qué interfaz debe enviar los paquetes destinados a cada red. Esto se hace por terminal, desde cada router, especificando 

``` bash
ip route RED_DESTINO MASCARA IP_DEL_SIGUIENTE_SALTO
```

Ej de aplicación, sobre el router 2:

![Figura 9](imagenes/simulacion/rutas_estaticas_R2.png)

Con esto le estamos indicando, en la primera linea, que si el R2 recibe un paquete con destino a la red del grupo 1 (10.10.10.0/24), debe enviarlo al siguiente salto, que es la IP 172.16.1.5, correspondiente a la interfaz del R0 que apunta hacia R2.

Con las rutas ya definidas en cada router probamos nuevamente conexión entre PC0 (grupo 0) y PC2 (grupo 1) y obtenemos:

![Figura 10](imagenes/simulacion/ping_PC0_PC2_conrutas.png)

De esta forma finalizamos la simulación de la primera etapa, para garantizar que todos los hosts de las distintas redes puedan establecer comunicación entre ellos. 




---
## PARTE 4 LUEGO BORRO ESTO 

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

---
