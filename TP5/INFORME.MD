
# Trabajo Práctico N° 5: 
# Manipulación de librerías de networking y análisis de la capa de transporte en sistemas encriptados. 
**Nombres**  
_Jorge A. Arbach_
_Bianca A. Fraga_
_Sol A. Nou_
_Felipe Pillichody_

**Rackea2**

**Universidad Nacional de Córdoba**  
**Redes de Computadoras**
**Profesores**: Santiago Henn   
**Fecha**: Jueves 22/05/2025

---

### Información de los autores
 
- **Información de contacto**: _jorge.arbach@mi.unc.edu.ar_, _bianca.fraga@mi.unc.edu.ar_, _felipe.pillichody@mi.unc.edu.ar_, _sol.nou@mi.unc.edu.ar_

---























## Desarrollo

Se han desarrollado scripts en _Python_ que permiten el envío y recepción secuencial de paquetes **TCP** a intervalos de tiempo configurables. Cada paquete contiene información identificatoria única, compuesta por el nombre del grupo y un número incremental. Para la implementación, se han utilizado las librerías estándar `socket` y `time`, garantizando una comunicación eficiente entre dispositivos dentro de una red local.

Se desarrollaron dos scripts diferentes:

* **Script del [servidor](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/server.py):** Responsable de recibir los paquetes enviados por el cliente y procesar la información contenida.  

* **Script del [cliente](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/client.py):** Encargado de generar y enviar los paquetes TCP con la información identificatoria correspondiente.

Para validar el correcto funcionamiento de estos scripts, se llevó a cabo una prueba entre dos computadoras pertenecientes a una misma red de área local (LAN): 

* **Cliente:** Laptop con sistema operativo Linux, dirección IP `192.168.1.33`.
* **Servidor:** Computadora de escritorio con sistema operativo Windows, dirección IP `192.168.1.24`. 

El _script del cliente_ fue configurado para enviar un total de **10 paquetes** con un intervalo de **1 segundo** entre cada transmisión. Se realizó la captura del tráfico de red para verificar que los paquetes fueran transmitidos correctamente. 

Los resultados fueron los siguientes:

![Figura 1](imagen/Figura1.png)

![Figura 2](imagen/Figura2.png)

A través de estas dos imágenes, podemos observar que el sistema cumple con el objetivo de enviar y recibir paquetes **TCP** de manera secuencial y con un intervalo de tiempo definido. La ejecución del _script del cliente_ [Figura 1] confirma el envío exitoso de los paquetes con la información identificatoria requerida, mientras que la [Figura 2] muestra la correcta recepción y procesamiento de los datos. 

Desde el _servidor_, se usó **Wireshark** para capturar el tráfico TCP entre las dos computadoras.Una vez finalizada la transmisión de datos, se aplicó el filtro `tcp.port == 12345`, lo que permitió visualizar únicamente los paquetes TCP asociados a dicho puerto, establecido como el puerto de escucha del servidor. 

![Figura 3](imagen/Figura3.png)

En este tráfico capturado, se observa de manera efectiva que la comunicación establecida se produce entre la dirección IP `192.168.1.24` **(cliente)** y la dirección `192.168.1.33` **(servidor)**. Durante la transmisión, el cliente envía paquetes desde un puerto aleatorio (`52498`) hacia el puerto `12345` del servidor. Esto es completamente normal en conexiones TCP, ya que los clientes eligen un puerto aleatorio para establecer una comunicación.  
Al principio de la captura, se puede identificar el **three-way Handshake**, un mecanismo fundamental para la inicialización de una sesión TCP. Se observa la siguiente secuencia clásica de intercambio de paquetes: 
* **SYN:** el cliente inicia la conexión enviando un paquete con la bandera `SYN`. 
* **SYN-ACK:** el servidor responde con `SYN, ACK`, confirmando la recepción del mensaje y proponiendo el establecimiento de la comunicación.
* **ACK:** el cliente envía una confirmación con `ACK`, completando la negociación y estableciendo exitosamente el canal de comunicación TCP. 

Esto indica que el canal TCP está correctamente establecido. Además, se identifican 10 paquetes con las flags  `PSH, ACK`, lo cual es el comportamiento esperado: 

* `PSH (Push)`: indica al receptor que debe procesar los datos de inmediato en lugar de almacenarlos temporalmente en el búfer. 
* `ACK (Acknowledgement)`: confirma la recepción de datos enviados previamente.


Estos paquetes contienen la **carga útil correspondiente** a los mensajes enviados, como _Rackea2_1, Rackea2_2, etc_. Su correcta transmisión y recepción confirma la funcionalidad del sistema implementado.
En la captura de tráfico, al analizar el paquete número **9440**, se observa que corresponde al **séptimo paquete** transmitido, lo cual se puede verificar revisando su carga útil a través del _hex dump_. De esta manera, se evidencia la secuencia de bytes que representa los datos enviados, confirmando la correcta identificación del mensaje dentro del flujo de comunicación.

![Figura 4](imagen/Figura4.png)

Hacia el final de la captura, se registra un intercambio de **FIN, ACK** por parte del cliente, seguido de una respuesta **ACK** del servidor. Esto indica que el cliente está cerrando correctamente la conexión después de enviar los **10 paquetes**.

Ahora, se sumará una _feature_ en ambos scripts para la **generación de logs**, lo que permitirá registrar detalladamente cada etapa del envío y recepción de los paquetes TCP. Además, se incrementará la cantidad de paquetes transmitidos a **100 paquetes** para poder calcular, en base a los logs y un script adicional, la **latencia promedio, máxima, mínima** y el **jitter** de la conexión. Cabe recordar que la **frecuencia de envío** es de **1 segundo** entre cada paquete, manteniendo el mismo intervalo utilizado en las pruebas anteriores. 

A continuación, adjuntamos los resultados obtenidos:

|                 CLIENTE                  |  SERVIDOR                                 |
|------------------------------------------|-------------------------------------------|
|[2025-05-25 22:12:31] Enviado: Rackea2_1  |[2025-05-25 22:12:33] Recibido: Rackea2_1  |
|[2025-05-25 22:12:32] Enviado: Rackea2_2  |[2025-05-25 22:12:34] Recibido: Rackea2_2  |
|[2025-05-25 22:12:33] Enviado: Rackea2_3  |[2025-05-25 22:12:35] Recibido: Rackea2_3  |
|[2025-05-25 22:12:34] Enviado: Rackea2_4  |[2025-05-25 22:12:36] Recibido: Rackea2_4  |
|[2025-05-25 22:12:35] Enviado: Rackea2_5  |[2025-05-25 22:12:37] Recibido: Rackea2_5  |
|[2025-05-25 22:12:36] Enviado: Rackea2_6  |[2025-05-25 22:12:38] Recibido: Rackea2_6  |
|[2025-05-25 22:12:37] Enviado: Rackea2_7  |[2025-05-25 22:12:39] Recibido: Rackea2_7  |
|[2025-05-25 22:12:38] Enviado: Rackea2_8  |[2025-05-25 22:12:40] Recibido: Rackea2_8  |
|[2025-05-25 22:12:39] Enviado: Rackea2_9  |[2025-05-25 22:12:41] Recibido: Rackea2_9  |
|[2025-05-25 22:12:40] Enviado: Rackea2_10 |[2025-05-25 22:12:42] Recibido: Rackea2_10 |
|[2025-05-25 22:12:41] Enviado: Rackea2_11 |[2025-05-25 22:12:43] Recibido: Rackea2_11 |
|...                                       |...                                        |
|[2025-05-25 22:14:05] Enviado: Rackea2_95 |[2025-05-25 22:14:08] Recibido: Rackea2_95 |
|[2025-05-25 22:14:06] Enviado: Rackea2_96 |[2025-05-25 22:14:09] Recibido: Rackea2_96 |
|[2025-05-25 22:14:07] Enviado: Rackea2_97 |[2025-05-25 22:14:10] Recibido: Rackea2_97 |
|[2025-05-25 22:14:08] Enviado: Rackea2_98 |[2025-05-25 22:14:11] Recibido: Rackea2_98 |
|[2025-05-25 22:14:09] Enviado: Rackea2_99 |[2025-05-25 22:14:12] Recibido: Rackea2_99 |
|[2025-05-25 22:14:10] Enviado: Rackea2_100|[2025-05-25 22:14:13] Recibido: Rackea2_100|


### Cálculo de latencia y jitter

Para evaluar el rendimiento de la comunicación TCP entre cliente y servidor, se analizaron los tiempos de transmisión de cada paquete intercambiado. Se registraron los **timestamps** de envío y recepción para calcular la **latencia** y el **jitter** de la conexión.

Para cada paquete $i$ enviado y recibido, se definen los siguientes parámetros:

- $t_{\text{envio},i}$: Timestamp de envío desde el cliente.  
- $t_{\text{recepcion},i}$: Timestamp de recepción en el servidor.  
- $L_i = t_{\text{recepcion},i} - t_{\text{envio},i}$: Latencia del paquete $i$, es decir, el tiempo que tarda en llegar desde el cliente al servidor.   

A partir de estos valores, se calcularon las siguientes métricas claves:

#### 1. Latencia promedio: Se obtiene calculando el promedio de las latencias individuales de los $N$ paquetes transmitidos.

$$
Latencia_\text{promedio} = \frac{1}{N} \sum_{i=1}^{N} L_i
$$

#### 2. Latencia mínima: Corresponde al menor tiempo de transmisión registrado entre cliente y servidor.

$$
\text{Latencia}_{\text{min}} = \min(L_i)
$$  

#### 3. Latencia máxima: Corresponde al mayor tiempo registrado en la transmisión de un paquete.

$$
\text{Latencia}_{\text{max}} = \max(L_i)
$$  

#### 4. Jitter (según **RFC 3550**): Representa la variabilidad en los tiempos de llegada de los paquetes. Se calcula como la diferencia entre latencias consecutivas.

$$
\text{Jitter} = \frac{1}{N - 1} \sum_{i=2}^{N} \left| L_i - L_{i-1} \right|
$$  

Donde $N$ es la cantidad total de paquetes medidos.

**Resultados obtenidos**

A partir del procesamiento de los datos registrados, se obtuvieron los siguientes valores: 

* **Latencia promedio:** 2.760 s
* **Latencia mínima:** 2.000 s
* **Latencia máxima:** 3.000 s
* **Jitter:** 0.010 s

Siguiendo el mismo procedimiento realizado con el protocolo TCP, se desarrollaron **scripts análogos** para la comunicación utilizando el protocolo **UDP**. En este caso, la transmisión de datos se realiza sin verificación de conexión, lo que permite una comunicación más rápida pero sin garantía de entrega de los paquetes.

Para ello, se desarrollaron los siguientes scripts:
 
* **Script del [servidor](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/server_w_log.py):** Encargado de recibir los datagramas enviados por el cliente.  

* **Script del [cliente](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/client_w_log.py):** Responsable de generar y enviar los datagramas UDP con la información identificatoria correspondiente.

Para validar el correcto funcionamiento de la transmisión con **UDP**, se configuraron las siguientes condiciones:

* Se enviaron **10 datagramas** con un **intervalo de 1 segundo** entre cada uno. 
* Se utilizó la misma infraestructura de prueba que en la implementación TCP:
     * **Cliente:** Laptop con sistema operativo Linux, dirección IP `192.168.1.33`.
     * **Servidor:** Computadora de escritorio con sistema operativo Windows, dirección IP `192.168.1.24`.

**Resultados obtenidos**

![Figura 5](imagen/Figura5.png)

![Figura 6](imagen/Figura6.png)

Los resultados obtenidos demuestran que la comunicación **UDP** entre cliente y servidor se realizó de manera efectiva. La correcta recepción de los **10 datagramas** confirma que la transmisión se llevó a cabo sin pérdidas dentro de la red local. A diferencia de TCP, donde se garantiza la entrega, UDP no realiza comprobaciones de conexión, pero en esta prueba, los paquetes llegaron correctamente.
Al capturar el tráfico con _Wireshark_ con el filtro `udp.port == 12345`, observamos en la figura a continuación exclusivamente la transmisión de los **10 datagramas**, lo que confirma que la comunicación entre cliente y servidor se ha realizado según lo esperado. 

![Figura 7](imagen/Figura7.png)

Esto ocurre ya que, a diferencia de TCP, **UDP** es un protocolo no orientado a la conexión, lo que significa que los datagramas se envían directamente sin una confirmación de recepción por parte del servidor. 

En la captura, a su vez, se pueden identificar los paquetes con su respectiva carga útil, incluyendo los identificadores secuenciales esperados, lo que indica que la transmisión se realizó correctamente dentro de la red local.

Ahora analizamos en detalle el contenido de un **datagrama en particular**: 

![Figura 8](imagen/Figura8.png)

En la figura anterior, se observa la estructura del paquete, donde se representa la información en **formato hexadecimal** y su correspondiente traducción en **ASCII**.

Dentro del campo de **datos del datagrama**, podemos identificar que la carga útil contiene el texto `Rackea2_9`, lo que confirma que este paquete corresponde al noveno mensaje enviado durante la prueba. Esta representación hexadecimal es útil para analizar la integridad de los datos transmitidos, permitiendo verificar si la información se ha preservado correctamente a lo largo de la transmisión. 

Tal como dijimos anteriormente, en **UDP**, los datos son enviados de forma directa sin procesos de confirmación, lo que implica que la carga útil viaja sin correcciones automáticas en caso de errores. Pero esta captura valida que el envío de los mensajes se realizó como se esperaba.

Para evaluar el rendimiento de la comunicación **UDP**, se realizó una prueba enviando **100 datagramas** con un intervalo de **1 segundo** entre cada envío. Esta prueba permite obtener métricas clave sobre la _latencia_ y el _jitter_, analizando los tiempos de transmisión y recepción.

Se implementó un sistema de _logs_ en ambos scripts (cliente y servidor) para registrar los _timestamps_ de los paquetes enviados y recibidos. A continuación, se presentan fragmentos de los registros obtenidos:

|                 CLIENTE                  |  SERVIDOR                                 |
|------------------------------------------|-------------------------------------------|
|[2025-05-25 23:19:39] Enviado: Rackea2_1  |[2025-05-25 23:19:42] Recibido: Rackea2_1  |
|[2025-05-25 23:19:40] Enviado: Rackea2_2  |[2025-05-25 23:19:43] Recibido: Rackea2_2  |
|[2025-05-25 23:19:41] Enviado: Rackea2_3  |[2025-05-25 23:19:44] Recibido: Rackea2_3  |
|[2025-05-25 23:19:42] Enviado: Rackea2_4  |[2025-05-25 23:19:45] Recibido: Rackea2_4  |
|[2025-05-25 23:19:43] Enviado: Rackea2_5  |[2025-05-25 23:19:46] Recibido: Rackea2_5  |
|[2025-05-25 23:19:44] Enviado: Rackea2_6  |[2025-05-25 23:19:47] Recibido: Rackea2_6  |
|[2025-05-25 23:19:45] Enviado: Rackea2_7  |[2025-05-25 23:19:48] Recibido: Rackea2_7  |
|...                                       |...                                        |
|[2025-05-25 23:21:11] Enviado: Rackea2_93 |[2025-05-25 23:21:14] Recibido: Rackea2_93 |
|[2025-05-25 23:21:12] Enviado: Rackea2_94 |[2025-05-25 23:21:15] Recibido: Rackea2_94 |
|[2025-05-25 23:21:13] Enviado: Rackea2_95 |[2025-05-25 23:21:16] Recibido: Rackea2_95 |
|[2025-05-25 23:21:14] Enviado: Rackea2_96 |[2025-05-25 23:21:17] Recibido: Rackea2_96 |
|[2025-05-25 23:21:15] Enviado: Rackea2_97 |[2025-05-25 23:21:18] Recibido: Rackea2_97 |
|[2025-05-25 23:21:16] Enviado: Rackea2_98 |[2025-05-25 23:21:19] Recibido: Rackea2_98 |
|[2025-05-25 23:21:17] Enviado: Rackea2_99 |[2025-05-25 23:21:20] Recibido: Rackea2_99 |
|[2025-05-25 23:21:18] Enviado: Rackea2_100|[2025-05-25 23:21:21] Recibido: Rackea2_100|

A partir de los _logs_ obtenidos, se calcularon las siguientes métricas de rendimiento para la conexión **UDP**: 

* **Latencia promedio:** 3.000 s
* **Latencia mínima:** 3.000 s
* **Latencia máxima:** 3.000 s
* **Jitter:** 0.000 s

Estos resultados indican que la **latencia** se mantiene _constante_ a lo largo de toda la prueba, sin variaciones significativas en los tiempos de transmisión. La estabilidad del **jitter**, con valor de _0.000 s_, demuestra que los paquetes llegaron con una periodicidad uniforme, lo que sugiere una conexión sin interferencias. 

### Diferencias clave entre TCP y UDP observadas en Wireshark
**TCP** es un protocolo **orientado a la conexión**, lo que significa que antes de transferir datos realiza un proceso de _handshake_ (intercambio inicial de paquetes `SYN`, `SYN-ACK` y `ACK`) para establecer la conexión entre cliente y servidor. **UDP**, en cambio, **no es orientado a conexión**: los paquetes se envían directamente sin este paso previo.
En las capturas de **Wireshark**, esto se evidencia claramente: los paquetes **TCP** muestran el _handshake inicial_, y luego se observa cómo cada paquete con datos útiles es seguido de un `ACK` de confirmación. En cambio, los paquetes **UDP** no tienen ningún tipo de intercambio de control adicional.
**TCP** garantiza el orden de llegada y realiza reenvíos automáticos en caso de pérdida, mientras que **UDP** no garantiza el orden ni realiza reintentos: si un paquete se pierde o llega fuera de orden, simplemente no se recupera.
El _payload_ (contenido útil) en **TCP** se encuentra dentro de segmentos identificados con flags como [`PSH, ACK`], y va acompañado de control de flujo y número de secuencia. En **UDP**, el contenido se entrega como un bloque plano en la sección `Data`, sin fragmentación ni metadatos adicionales.
Finalmente, el _overhead_ en **TCP es mayor**: incluye cabeceras más pesadas, control de flujo, confirmaciones, y mecanismos de gestión de conexión. **UDP**, en cambio, **tiene una cabecera mínima**, lo que lo hace más liviano y rápido, aunque a costa de fiabilidad.

|          MÉTRICAS           |     TCP       |     UDP       |
|-----------------------------|---------------|---------------|
|Latencia Promedio            |     2.76 seg  |     3 seg     |
|Latencia Máxima              |     2 seg     |     3 seg     |
|Latencia Mínima              |     3 seg     |     3 seg     |
|Jitter                       |     0.01 seg  |     0 seg     |

La **encriptación** es una técnica que permite proteger la información mediante el uso de claves que transforman los datos en un formato ilegible para quienes no están autorizados a acceder a ellos. Existen dos grandes tipos de encriptación: 

* **Encriptado simétrico:** se utiliza una _única clave secreta_ tanto para cifrar como para descifrar el mensaje. Esto implica que ambas partes deben conocer y mantener en secreto la misma clave, lo cual presenta un problema en cuanto a la seguridad del intercambio de dicha clave. Sin embargo, este tipo de encriptación es mucho más rápido y eficiente, por lo que se emplea comúnmente para cifrar grandes volúmenes de datos o para proteger información en tiempo real, como en discos o conexiones privadas.
* **Encriptado asimétrico:** utiliza un par de claves distintas: una _clave pública_, que puede ser compartida libremente, y una _clave privada_, que debe mantenerse secreta. Un mensaje cifrado con una clave pública sólo puede ser descifrado con la clave privada correspondiente, y viceversa. Esto ofrece una mayor seguridad para la transmisión de datos, ya que no es necesario compartir la clave privada. Sin embargo, es un proceso más lento y con mayor carga computacional, por lo que no suele utilizarse para cifrar grandes cantidades de información, sino para intercambiar claves simétricas de manera segura o para firmar digitalmente documentos.

_En resumen_, la encriptación simétrica es más rápida pero menos segura en cuanto al intercambio de claves, mientras que la encriptación asimétrica es más segura pero más lenta. En muchos sistemas modernos se utilizan ambas combinadas para aprovechar las ventajas de cada una.


