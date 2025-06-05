
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

**Script del [servidor](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/server.py):** Responsable de recibir los paquetes enviados por el cliente y procesar la información contenida.  

**Script del [cliente](https://github.com/Biaan15/Rackea2/blob/main/TP5/TCP/client.py):** Encargado de generar y enviar los paquetes TCP con la información identificatoria correspondiente.


Para validar el correcto funcionamiento de estos scripts, se llevó a cabo una prueba entre dos computadoras pertenecientes a una misma red de área local (LAN): 

**Cliente:** Laptop con sistema operativo Linux, dirección IP `192.168.1.33`.
**Servidor:** Computadora de escritorio con sistema operativo Windows, dirección IP `192.168.1.24`. 

El _script del cliente_ fue configurado para enviar un total de **10 paquetes** con un intervalo de **1 segundo** entre cada transmisión. Se realizó la captura del tráfico de red para verificar que los paquetes fueran transmitidos correctamente. 

Los resultados fueron los siguientes:

![Figura 1](imagen/Figura1.png)





![Figura 2](imagen/Figura2.png)

A través de estas dos imágenes, podemos observar que el sistema cumple con el objetivo de enviar y recibir paquetes **TCP** de manera secuencial y con un intervalo de tiempo definido. La ejecución del _script del cliente_ [Figura 1] confirma el envío exitoso de los paquetes con la información identificatoria requerida, mientras que la [Figura 2] muestra la correcta recepción y procesamiento de los datos. 

Desde el _servidor_, se usó **Wireshark** para capturar el tráfico TCP entre las dos computadoras.Una vez finalizada la transmisión de datos, se aplicó el filtro `tcp.port == 12345`, lo que permitió visualizar únicamente los paquetes TCP asociados a dicho puerto, establecido como el puerto de escucha del servidor. 

![Figura 3](imagen/Figura3.png)
En este tráfico capturado, se observa de manera efectiva que la comunicación establecida se produce entre la dirección IP `192.168.1.24` **(cliente)** y la dirección `192.168.1.33` **(servidor)**. Durante la transmisión, el cliente envía paquetes desde un puerto aleatorio (`52498`) hacia el puerto `12345` del servidor. Esto es completamente normal en conexiones TCP, ya que los clientes eligen un puerto aleatorio para establecer una comunicación.  
Al principio de la captura, se puede identificar el **three-way Handshake**, un mecanismo fundamental para la inicialización de una sesión TCP. Se observa la siguiente secuencia clásica de intercambio de paquetes: 
**SYN:** el cliente inicia la conexión enviando un paquete con la bandera `SYN`. 
**SYN-ACK:** el servidor responde con `SYN, ACK`, confirmando la recepción del mensaje y proponiendo el establecimiento de la comunicación.
**ACK:** el cliente envía una confirmación con `ACK`, completando la negociación y estableciendo exitosamente el canal de comunicación TCP. 
Esto indica que el canal TCP está correctamente establecido. Además, se identifican 10 paquetes con las flags  `PSH, ACK`, lo cual es el comportamiento esperado: 
`PSH (Push)`: indica al receptor que debe procesar los datos de inmediato en lugar de almacenarlos temporalmente en el búfer. 


`ACK (Acknowledgement)`: confirma la recepción de datos enviados previamente.


Estos paquetes contienen la **carga útil correspondiente** a los mensajes enviados, como _Rackea2_1, Rackea2_2, etc_. Su correcta transmisión y recepción confirma la funcionalidad del sistema implementado.
En la captura de tráfico, al analizar el paquete número **9440**, se observa que corresponde al **séptimo paquete** transmitido, lo cual se puede verificar revisando su carga útil a través del _hex dump_. De esta manera, se evidencia la secuencia de bytes que representa los datos enviados, confirmando la correcta identificación del mensaje dentro del flujo de comunicación.




![Figura 4](imagen/Figura4.png)
Hacia el final de la captura, se registra un intercambio de **FIN, ACK** por parte del cliente, seguido de una respuesta **ACK** del servidor. Esto indica que el cliente está cerrando correctamente la conexión después de enviar los **10 paquetes**.


Ahora, se sumará una _feature_ en ambos scripts para la **generación de logs**, lo que permitirá registrar detalladamente cada etapa del envío y recepción de los paquetes TCP. Además, se incrementará la cantidad de paquetes transmitidos a **100 paquetes** para poder calcular, en base a los logs y un script adicional, la **latencia promedio, máxima, mínima** y el **jitter** de la conexión. Cabe recordar que la **frecuencia de envío** es de **1 segundo** entre cada paquete, manteniendo el mismo intervalo utilizado en las pruebas anteriores. 
