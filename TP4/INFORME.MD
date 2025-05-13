# Trabajo Práctico N°4: 
# Ruteo externo dinámico y sistemas autónomos 
**Nombres**  
_Jorge A. Arbach_
_Bianca A. Fraga_
_Sol A. Nou_
_Felipe Pillichody_

**Rackea2**

**Universidad Nacional de Córdoba**  
**Redes de Computadoras**
**Profesores**: Santiago Henn   
**Fecha**: Jueves 24/04/2025

---

### Información de los autores
 
- **Información de contacto**: _jorge.arbach@mi.unc.edu.ar_, _bianca.fraga@mi.unc.edu.ar_, _felipe.pillichody@mi.unc.edu.ar_, _sol.nou@mi.unc.edu.ar_
---




# Parte I - Integración de conceptos, actividades online e investigación


## 1. Sobre AS

Un Autonomous System (AS) es una red o grupo de redes muy grande con una única política de enrutamiento. Lo que esté dentro de un AS comparte criterios unificados sobre cómo enrutar el tráfico hacia otros AS. Puede contener muchas subredes LAN, WAN, o redes privadas y públicas.

La mayoría de los AS se conectan a otros AS, pero si un AS se conecta solo a otro AS y comparte la misma política de enrutamiento, puede considerarse una subred del primer AS.

Cada AS esta bajo una administración única que es responsable de las políticas de ruteo involucradas. Lo normal es que cada una sea gestionada por un proveedor de acceso a Internet (ISP), una gran empresa tecnológica, una universidad o una agencia gubernamental.



Desde una perspectiva más general, podemos verlo como que Internet es una red de redes, y los sistemas autónomos son las grandes redes que componen Internet. Por este motivo, cada ordenador o dispositivo que se conecta a Internet está conectado a un AS. 


Podemos pensarlo con la siguiente analogía: un AS como la oficina de correos de una ciudad. El correo va de una oficina de correos a otra hasta que llega a la ciudad correcta, y la oficina de correos de esa ciudad entregará el correo en esa ciudad. Del mismo modo, los paquetes de datos recorren Internet saltando de AS a AS hasta que llegan al AS que contiene su dirección de Protocolo de Internet (IP) de destino. Los enrutadores dentro de ese AS envían el paquete a la dirección IP.
Cada AS controla un conjunto específico de direcciones IP, al igual que la oficina de correos de cada ciudad es responsable de entregar el correo a todas las direcciones de la ciudad. El rango de direcciones IP que controla un determinado AS se denomina su espacio de direcciones IP.

Como vemos, es muy similar a lo que sucede con los paquetes que se envían entre redes, pero a una escala mucho más grande. Esto es porque existe similitud entre el enrutamiento intradominio (OSPF, RIP) e inter-AS (BPG).


Cada AS tiene un identificador único conocido como ASN (Autonomous System Number). Es usado principalmente por el protocolo BGP para identificar a cada AS y permitir el intercambio de rutas entre ellos.
Existen dos tipos de ASN:


-  ASN de 16 bits: van del 1 al 65.535 (algunos están reservados).
- ASN de 32 bits (también llamado ASN extendido): van del 65.536 al 4.294.967.295.


A veces se expresan en formato decimal o en formato dotted. Los ASN privados (como los rangos de IP privadas) también existen: por ejemplo, del 64.512 al 65.534 para 16 bits.
Veamos algunos AS conocidos:

1. Google:


- ASN: 15169
- Nombre: GOOGLE
- Descripción: Utilizado por Google para sus servicios globales, incluyendo Google Search, Gmail, YouTube, etc.


2. Apple Inc.


- ASN: 714
- Nombre: APPLE-ENGINEERING
- Descripción: ASN histórico de Apple, usado para servicios de ingeniería y red de distribución.


3. Universidad de Stanford


- ASN: 32
- Nombre: STANFORD
- Descripción: Uno de los ASN más antiguos. Stanford opera su propia red académica con salida directa a Internet.


Para entender cómo nuestra conexión a Internet se enruta a través de la red global, es importante identificar el Sistema Autónomo (AS) al que estamos conectados. En la página web [Hurricane Electric BGP Toolkit](https://bgp.he.net/) podemos ver la leyenda _Your ISP is xxxx_. 
Por ejemplo, al entrar desde la computadora de un integrante del equipo, conectado a la red wifi de su casa, figura _Your ISP is AS7303 (Telecom Argentina S.A.)_ lo que nos indica que el AS al que está conectados es:
**AS7303 – Telecom Argentina S.A.**
![Figura 1](imagen/Figura1Parte1.png)
Veamos algunas características de este AS:
**Identidad y Alcance:**
- Organización: Telecom Argentina
- También conocida como: FiberCorp, Cablevisión
- ASN (Autonomous System Number): 7303
- Tipo de organización: ISP (Internet Service Provider) con servicios de cable y DSL
- Cobertura geográfica: Regional, principalmente Argentina y Paraguay


Telecom Argentina es uno de los mayores proveedores de conectividad de la región, ofreciendo servicios residenciales, móviles y empresariales.

**Información de Enrutamiento y Prefijos**
El AS7303 de Telecom Argentina administra un importante volumen de direcciones IP públicas y redes anunciadas mediante BGP. Para entenderlo mejor, es clave distinguir entre:

-   Prefijos originados: son los bloques de direcciones IP que Telecom posee y administra directamente. En este caso, origina:  
-   730 prefijos IPv4, que suman un total de 8.429.312 direcciones IP públicas  
-   119 prefijos IPv6, aunque el despliegue de IPv6 es aún limitado públicamente       
-   Prefijos anunciados: representan todas las redes que Telecom anuncia a través de BGP, tanto propias como de clientes o socios de red. En total, anuncia:  
-   2.535 prefijos IPv4  
-   285 prefijos IPv6


El número de prefijos anunciados es mayor al de originados porque incluye redes de terceros que Telecom ayuda a enrutar (por ejemplo, empresas clientes o acuerdos de peering).

**Conectividad y Peering*
- Cantidad de peers (conexiones con otros AS): Más de 240  
- Principales proveedores de tránsito (upstreams):  
	- AS3356 – Lumen (Level 3)  
	- AS6762 – Telecom Italia Sparkle (Seabone)  
	- AS3257 – GTT Communications


Estos upstreams permiten que Telecom se conecte al resto del mundo a través de redes troncales de alto nivel, asegurando redundancia y baja latencia.
**Tráfico y Capacidad**
- Niveles de tráfico estimados: 10 a 20 terabits por segundo
- Ratio de tráfico: Mayormente inbound, lo que es típico de un ISP con muchos clientes residenciales (los usuarios descargan más de lo que suben).



## 2. Sobre BGP
BGP (Border Gateway Protocol) es el protocolo de enrutamiento utilizado para intercambiar información de rutas entre Sistemas Autónomos (AS) en Internet. Por eso se lo considera el protocolo base de la arquitectura de Internet global.
Cuando una organización necesita conectarse al mundo exterior, es decir, enrutar paquetes más allá de sus redes internas, debe formar parte de un Sistema Autónomo y utilizar BGP para anunciar sus rutas IP a otros AS.
A diferencia de protocolos internos como OSPF o RIP, que están diseñados para enrutar dentro de una misma red (intradominio), BGP se utiliza para el enrutamiento entre dominios administrativos distintos (inter-AS).
BGP es un protocolo de tipo vector de ruta. Es importante no confundirlo con un protocolo de vector de distancia, como RIP. En los protocolos de vector de distancia, las decisiones se basan en una métrica simple como el número de saltos. En cambio, BGP no calcula distancias: toma decisiones en función del camino completo que los paquetes deben recorrer a través de los AS (AS-PATH), además de otros atributos.
Esta lógica convierte a BGP en un protocolo altamente personalizable, ya que permite aplicar políticas de enrutamiento específicas según necesidades técnicas, comerciales o de seguridad. De esta forma, las organizaciones pueden decidir qué rutas aceptar, preferir o rechazar con gran precisión.

### Funcionamiento del Protocolo BGP
El funcionamiento de BGP se puede resumir en tres etapas principales: establecimiento de la sesión, mantenimiento de la conexión y anuncio de rutas.
1. Adquisición de vecino (Neighbor Acquisition)
BGP establece conexiones entre routers que han sido configurados explícitamente como vecinos (peers). Para ello:
- Se utiliza el protocolo TCP sobre el puerto 179.
- Ambos routers intercambian mensajes BGP del tipo OPEN, en los que se negocian parámetros como:
	- Número de Sistema Autónomo (ASN)
- Versión del protocolo
	- Tiempo de hold (tiempo máximo sin mensajes antes de considerar caída la sesión)


Este proceso es similar al intercambio inicial de mensajes HELLO en OSPF, aunque más orientado a control de sesión que a descubrimiento automático.
2. Detección de vecino alcanzable (Keepalive)
Una vez establecida la conexión BGP:
- Los routers se envían periódicamente mensajes KEEPALIVE para indicar que la sesión sigue activa.


- Si un router no recibe KEEPALIVEs en el tiempo acordado (Hold Time), la sesión BGP se considera caída, y todas las rutas aprendidas de ese vecino se eliminan de la tabla de enrutamiento.


3. Intercambio de rutas (Path Advertisement) 
Con la sesión activa, los routers comienzan a intercambiar información de enrutamiento a través de mensajes UPDATE. Estos mensajes pueden:
- Anunciar nuevas rutas (prefijos IP)
- Retirar rutas previamente anunciadas


Cada ruta anunciada viene acompañada de atributos que ayudan a determinar la mejor ruta. Algunos atributos clave:
- AS_PATH: lista de AS atravesados para alcanzar la red (evita loops)
- NEXT_HOP: dirección IP del siguiente salto
- LOCAL_PREF, MED, COMMUNITY, entre otros


Veamos un ejemplo del proceso completo. Supongamos que el Router A (AS64501) y el Router B (AS64502) quieren intercambiar rutas usando BGP:
Adquisición de vecino:
Ambos routers están configurados como vecinos y establecen una conexión TCP por el puerto 179. Se envían mensajes OPEN con sus datos (ASN, tiempos, identificador). Si todo coincide, la sesión queda establecida.


Detección de vecino alcanzable:
Una vez conectados, se envían periódicamente mensajes KEEPALIVE. Si uno deja de responder dentro del tiempo acordado, la sesión se considera caída.


Anuncio de rutas:
Router A anuncia la red 203.0.113.0/24 mediante un mensaje UPDATE, incluyendo atributos como AS_PATH = [64501] y NEXT_HOP = 192.0.2.1. Router B aprende la ruta y la puede reenviar o instalar en su tabla.


**Tipos de mensajes BGP**

Todos los mensajes BGP están encapsulados en TCP, lo que garantiza la confiabilidad del transporte. Existen cuatro tipos principales de mensajes:
- *OPEN*: Inicia la sesión entre vecinos, se negocia versión, ASN, etc. Similar a un 	HELLO packet en OSPF.
- *KEEPALIVE*: Confirma que la conexión sigue viva (heartbeat)
- *UPDATE*: Anuncia nuevas rutas o retira rutas inválidas
- *NOTIFICATION*: Indica errores y finaliza la conexión

**Formato general de un paquete BGP (simplificado):**
| Campo   | Tamaño     | Descripción                                              |
|---------|------------|----------------------------------------------------------|
| Marker  | 16 bytes   | Para autenticación o detección de errores               |
| Length  | 2 bytes    | Longitud total del mensaje                               |
| Type    | 1 byte     | OPEN (1), UPDATE (2), NOTIFICATION (3), KEEPALIVE (4)    |
| Datos   | variable   | Depende del tipo de mensaje                              |


![Figura 2](imagen/Figura2Parte1.png)


BGP puede funcionar en dos contextos distintos: 

- *eBGP*: conecta distintos AS y permite salir a Internet.

- *iBGP*: distribuye esa información dentro del mismo AS, para que todos los routers sepan cómo enrutar el tráfico.
 
Si bien iBGP opera dentro de un AS, no se considera un protocolo de enrutamiento intradominio como OSPF o RIP, ya que estos están diseñados para calcular rutas internas automáticamente usando métricas como el costo, mientras que iBGP simplemente distribuye rutas externas aprendidas por eBGP, sin hacer descubrimiento de rutas ni cálculos internos complejos. Por lo que eBGP e iBGP usen el mismo protocolo, su comportamiento cambia bastante según el caso.

Supongamos que Telecom (AS7303) quiere intercambiar rutas con Google (AS15169). Para eso usan eBGP (External BGP). Se usa cuando los routers están en redes administradas por distintas organizaciones. Cada router anuncia sus rutas públicas al otro, permitiendo que el tráfico fluya entre Internet y las redes internas.


Cuando Router A (Telecom) recibe una ruta de Router B (Google), modifica el atributo NEXT_HOP, indicando su propia IP como el nuevo punto de entrada.


Ahora supongamos que dentro de Telecom, varios routers distribuyen internamente las rutas aprendidas por eBGP. Ese intercambio se hace usando iBGP (Internal BGP). Es decir, no se anuncian nuevas rutas, sino que se propagan internamente las rutas aprendidas desde eBGP.


El NEXT_HOP no se modifica, lo que significa que los routers deben tener rutas internas para alcanzar el próximo salto.



El iBGP es clave para los AS de tránsito. Un AS de tránsito es aquel que permite que el tráfico pase a través de él entre dos AS diferentes, sin ser ni el origen ni el destino final del tráfico. 


Veamos el caso de la topología de la consigna:

![Figura 3](imagen/Figura3Parte1.png)


El tráfico puede ir desde AS1 (R1) hacia AS3 (R4) pasando por AS2. AS2 no origina ni termina ese tráfico, solo lo transporta de un AS a otro. Por lo tanto, AS2 es de tránsito, mientras que AS1 y AS3 son redes de borde: solo intercambian tráfico con sus vecinos, pero no transportan tráfico de terceros.

---

Volvamos a nuestra conexión actual, recordemos que estamos usando el AS7303. Sabemos que tiene conexiones BGP con 244 Sistemas Autónomos distintos (244 peers), es decir, 244 relaciones eBGP activas

Si buscamos esta ASN en [BGPView](https://bgpview.io/) podemos ver, entre otros datos,  el siguiente gráfico:


![Figura 4](imagen/Figura4Parte1.png)

En este grafo vemos representadas algunas de las relaciones que AS7303 mantiene con otros AS. En particular, se muestran 4 conexiones eBGP visibles (con AS3257, AS3356, AS6762 y AS6453).
Esto no significa que tenga solo 4 vecinos eBGP, sino que el gráfico está simplificado y muestra las relaciones principales observadas en el enrutamiento global, como algunos de sus proveedores de tránsito (upstreams) y peers más significativos.

**Aclaración** : Las relaciones iBGP no aparecen en sitios públicos porque son internas y no se observan desde el exterior.

Cuando dos Sistemas Autónomos establecen relaciones BGP, no todas las conexiones son iguales. Se pueden clasificar según el tipo de servicio que se prestan entre sí:
- *Upstream*: Es un proveedor de tránsito. Permite al AS que lo contrata alcanzar el resto de Internet. Por ejemplo, si AS7303 se conecta con AS3356 (Lumen) para tener salida global, entonces AS3356 es un upstream de AS7303.


- *Downstream*: Es el cliente del AS. Si una empresa o red más pequeña contrata a AS7303 para conectarse a Internet, entonces esa red es un downstream de AS7303.


- *Peer*: Es una relación entre pares (generalmente gratuita) que permite intercambiar rutas de clientes, pero no brinda tránsito completo. Este tipo de acuerdo es común entre ISPs de tamaño similar o dentro de puntos de intercambio como CABASE.

Estas relaciones influyen en qué rutas se aceptan, prefieren o filtran. Además, ayudan a determinar si un AS es de borde (solo intercambia tráfico propio y de clientes) o de tránsito (permite que el tráfico pase entre terceros).

Ahora veamos qué sucede si cambiamos de red. Recordemos que descubrimos originalmente la AS que estamos utilizando para acceder a Internet con https://bgp.he.net/ . Desde la red del hogar de uno de los integrantes obtenemos:

![Figura 5](imagen/Figura5Parte1.png)

Si probamos conectados a la red de la facultad obtenemos:

![Figura 6](imagen/Figura5-1Parte1.png)

También probando, por ejemplo, desde la red del lugar de trabajo de uno de los integrantes del grupo obtenemos:

![Figura 7](imagen/Figura6Parte1.png)
![Figura 7-1](imagen/Figura6-1Parte1.png)

Si queremos comparar esta ultima con la AS7303 de Telecom, podemos ver una gran diferencia en la cantidad de peers, teniendo AS262150  conexiones BGP con únicamente 13 Sistemas Autónomos, frente a los 244 de Telecom, demostrando la diferencia en el tamaño de la red. 

Además, la pagina https://bgpview.io/ nos da otro parametro para comparar, _Traffic Estimation_, diferenciado entre 10-20Tbps que tiene AS7303 y 50-100Gbps de AS262150,  lo que nos da una idea del tamaño de tráfico manejado por cada AS, evidenciando la diferencia de escala de ambos proveedores.

Como última prueba para comparar ambos ASN, vamos a observar el recorrido de los paquetes hacia un destino común, como el DNS de Google 8.8.8.8. De esta forma vemos el camino de red que usa cada ASN para llegar a Internet, permitiendo ver los proveedores de tránsitos, los saltos y la eficiencia de cada enrutamiento. 
Desde la conexión a la red AS7303 de Telecom Argentina, observamos esta salida:

![Figura 7](imagen/Figura7Parte1.png)

Por el otro lado, desde la red AS262150 de Empresa Provincial de Energia de Cordoba, obtenemos:

![Figura 8](imagen/Figura8Parte1.png)

Los tracert realizados al servidor público 8.8.8.8 desde dos sistemas autónomos distintos permiten observar diferencias en el enrutamiento y la conectividad de cada red. En el caso de AS7303 (Telecom Argentina), la traza presenta múltiples saltos intermedios que no responden, posiblemente por filtros ICMP, antes de llegar a direcciones IP asociadas a Google (por ejemplo, 72.14.194.198), siendo una ruta más compleja y requiriendo 10 saltos. 

Por el otro lado, la traza desde AS262150 (EPEC) muestra un camino más directo y completamente visible, con solo siete saltos hasta el destino, pasando por direcciones IP internas, luego por la IP 200.14.75.202 perteneciente a (CABASE Camara Arg de Base de Datos y Serv en Linea) y rápidamente llegando a la red de Google. Este segundo trace cuenta con un camino más limpio y controlado hacia Internet.

---

Por último, vamos con un caso práctico que permite ver la importancia del protocolo BGP:

El 4 de octubre de 2021, Facebook, junto con sus servicios asociados como WhatsApp, Instagram, Messenger y Oculus, experimentó una interrupción global que duró más de seis horas. Este incidente afectó a aproximadamente tres mil millones de usuarios en todo el mundo y fue causado por una serie de errores en la configuración del protocolo de enrutamiento BGP (Border Gateway Protocol) en la red troncal de la empresa.

Durante una operación de mantenimiento rutinaria, se ejecutó un comando que desconectó accidentalmente los centros de datos de Facebook de su red troncal. Como resultado, los routers de la empresa dejaron de anunciar sus rutas BGP, lo que hizo que los servidores de nombres de dominio (DNS) de Facebook fueran inaccesibles desde Internet. 

Esto provocó que los navegadores y aplicaciones no pudieran resolver los nombres de dominio de Facebook, haciendo que sus servicios parecieran haber desaparecido del mapa de Internet .
Consecuencias del apagón:

- Interrupción global de servicios: Facebook, Instagram, WhatsApp y otros servicios asociados estuvieron inaccesibles para usuarios de todo el mundo durante más de seis horas .
- Impacto en la comunicación interna: Los empleados de Facebook no pudieron utilizar herramientas internas, acceder a correos electrónicos ni ingresar a las oficinas, ya que los sistemas de autenticación también dependían de la red afectada
- Pérdidas económicas: Se estima que la interrupción causó pérdidas de al menos 60 millones de dólares en ingresos publicitarios y una caída del 5% en el valor de las acciones de la empresa. 
- Afectación a terceros: Servicios que dependen de la autenticación a través de Facebook también se vieron afectados, impidiendo que los usuarios accedieran a diversas plataformas y aplicaciones.

Este incidente destacó la fragilidad de la infraestructura de Internet y la importancia de una configuración adecuada de los protocolos de enrutamiento. También subrayó la necesidad de contar con mecanismos de recuperación efectivos y redundancias que permitan mitigar el impacto de errores humanos en sistemas críticos.

# Parte II - Simulaciones y análisis

Para iniciar el desarrollo de esta segunda parte del proyecto, utilizó una implementación otorgada por el profesor, de una topología de red para dos **Sistemas Autónomos (AS100 - AS200)** en un entorno virtual, utilizando el software _Packet Tracer_ como herramienta principal:

![Figura 1](imagen/Figura1Parte2.png)

Para evaluar el estado de **BGP** en la red, es necesario ejecutar una serie de comandos que nos permitirán analizar su configuración y funcionamiento, tal como se muestra a continuación:

* `show ip bgp summary`: este comando muestra el estado de las sesiones BGP con los vecinos, permitiendo verificar si la comunicación está establecida correctamente. 
* `show running-config | section router bgp`: extrae de toda la configuración del router, la referida a BGP del router, indicando los vecinos definidos, el número de AS y otros parámetros clave.
* `show ip protocols`: revela los protocolos de enrutamiento activos en el dispositivo, incluyendo información sobre el funcionamiento de BGP.
* `show ip bgp`: presenta la tabla de enrutamiento BGP, con detalles sobre las rutas anunciadas y aprendidas, su AS_PATH y otros tipos de atributos. 
* `show ip route bgp`: muestra la tabla de enrutamiento, permitiendo ver cómo BGP se integra con el resto de los protocolos de enrutamiento.

La **evidencia de que BGP** está funcionando correctamente suele encontrarse cuando ejecutamos el comando `show ip bgp summary` en la terminal del CLI de cada router, verificando el estado de las sesiones BGP y el intercambio de rutas con los vecinos.

![Figura 2](imagen/Figura2Parte2.png)

La imagen confirma que BGP está funcionando correctamente, ya que la sesión con el vecino pudo ser establecida y está intercambiando rutas activamente. Además, el protocolo operó de manera continua sin interrupciones.

En Packet Tracer, los estados de BGP se representan mediante números en lugar de nombres convencionales. Se observa que el `Router0` mantiene una sesión BGP con el vecino `10.0.0.2`, cuyo estado en la columna State es **4**. Esto significa que el router ha enviado un mensaje de apertura (`OpenSent`), indicando que el proceso de negociación BGP está avanzando, aunque aún no se ha alcanzado el estado **Established (6)**.

Con respecto a las **tablas de ruteo**, vamos a tener dos tipos de tablas:

* **Tabla de enrutamiento**: se obtiene ejecutando el comando `show ip route bgp`. Esta tabla muestra todas las rutas que el router conoce y cómo debe enviar los paquetes hacia sus destinos. Indica qué redes son alcanzables, y específicamente con este comando filtra las que fueron aprendidas del protocolo **BGP**. A diferencia de la _tabla de enrutamiento general_ (obtenida con `show ip route`), que incluye rutas de diferentes protocolos, mostrando cómo fueron aprendidas (si directamente conectadas, por protocolos dinámicos como BGP, OSPF,etc. o configuradas manualmente) y a través de qué interfaz deben ser enviadas.

![Figura 3](imagen/Figura3Parte2.png)

Decidimos ejecutar `show ip route bgp` porque nos interesa evaluar únicamente las rutas propagadas por BGP, sin interferencias de otros protocolos. 

A través de la imagen, se observa que la ruta fue aprendida mediante BGP (se encuentra marcado con la letra **“B”**). Esta se alcanza a través del **Next-Hop 10.0.0.2**, lo que significa que el router enviará los paquetes a esa dirección para alcanzar la red de destino `192.168.2.0/24`. La métrica **[20/0]** indica la distancia administrativa y otros parámetros internos utilizados por el protocolo. Por último, el tiempo **00:00:00** muestra que la ruta fue instalada recientemente en la tabla de enrutamiento. 

* **Tabla de BGP**: se obtiene ejecutando el comando `show ip bgp`, que muestra exclusivamente las rutas aprendidas por BGP. En esta tabla, el router registra las redes que recibió mediante anuncios de sus vecinos BGP, junto con otros datos como el **Next-Hop, AS_PATH** y las métricas utilizadas para la selección de la mejor ruta. 

![Figura 4](imagen/Figura4Parte2.png)

El contenido de la tabla confirma que BGP está funcionando correctamente, ya que el router recibe anuncios de rutas de su vecino y procesa la información correctamente. La presencia de la red `192.168.2.0/24` en la tabla evidencia que el intercambio de rutas BGP está funcionando y que la conectividad entre los dispositivos de la red se está gestionando según lo esperado.


Con esto la topología queda planteada y se verificó que los diferentes **Sistemas Autónomos** están interconectados a través de BGP para el intercambio de rutas y la propagación de la conectividad entre redes externas. Recordamos que cada _AS_ tiene sus propios dispositivos y segmentos de red, por lo que es fundamental verificar si los hosts dentro de cada sistema pueden comunicarse correctamente. 

Para esto, se realizaron pruebas de conectividad de la siguiente manera:

* **Prueba de conectividad desde AS100 hacia AS200:** se seleccionó la _PC0_ del AS100 y, a través de la consola, se ejecutó el comando `ping 192.168.2.2`. Este `ping` corresponde a la dirección IP de _PC2_, ubicada en el AS200. La prueba muestra una respuesta exitosa, lo que confirma que existe conectividad entre ambos sistemas autónomos y que el enrutamiento funciona correctamente. Esto indica que BGP ha propagado las rutas adecuadamente, permitiendo que el tráfico viaje entre AS100 y AS200 sin inconvenientes.

![Figura 5](imagen/Figura5Parte2.png)

* **Prueba de conectividad desde AS200 hacia AS100:** se seleccionó la _PC3_ del AS200 y, a través de la consola, se ejecutó el comando `ping 192.168.1.3`. Este `ping` corresponde a la dirección IP de _PC1_, ubicada en el AS100. La prueba muestra respuesta exitosa, lo que confirma que la comunicación entre AS200 y AS100 es funcional y que el enrutamiento está correctamente configurado. Esto refuerza la misma conclusión obtenida en la prueba anterior.

![Figura 6](imagen/Figura6Parte2.png)

### Comportamiento dinámico del protocolo BGP ante cambios y fallos en la red.

En una red basada en BGP, es fundamental analizar cómo el tráfico responde a cambios en la topología. Para ello, se simulará tráfico entre dispositivos, se apagará y encenderá un router, y se observará el impacto en la conectividad. 

En primer lugar, como ya comprobamos anteriormente, verificamos si hay una conectividad inicial entre los dispositivos (desde _PC0_ hacia _PC2_). Luego de esto, habilitaremos el **Modo Simulación** del programa para observar el movimiento de datos entre dichos hosts, configurando los filtros de evento para mostrar `ICMP` y `BGP`:

![Figura 7](imagen/Figura7Parte2.png)
![Figura 8](imagen/Figura8Parte2.png)

En esta captura, podemos observar la transmisión de paquetes `ICMP` y `BGP` donde:

* **Flujo `ICMP` entre dispositivos:** los paquetes `ICMP` se están moviendo entre los dispositivos _PC2 → Switch1 → Router1 → Router0 → Switch0 → PC0_ y así sucesivamente, lo que indica que el tráfico `ping` está siendo encaminado correctamente a través de dicha topología.

* **Mensajes BGP entre routers:** se observa tráfico BGP entre `Router1` y `Router0`, lo que confirma que ambos routers están intercambiando información de enrutamiento. 

Si mientras se encuentra funcionando la simulación, apagamos y encendemos un router (en este caso _Router1_), ocurre lo siguiente:

![Figura 9](imagen/Figura9Parte2.png)

Cuando el _Router1_ se apaga, hay un intervalo sin eventos de tráfico relacionados con él, lo que confirma que la comunicación quedó interrumpida. Esto significa que las rutas aprendidas por BGP desaparecen, causando la pérdida de conectividad entre los _AS100_ y _AS200_. 

Los paquetes `ping` enviados desde _PC0_ hacia _PC2_ dejan de recibir respuesta y aparece el mensaje `Reply from 192.168.1.1: Destination host unreachable`. Este mensaje nos indica que _Router0_ ya no tiene una ruta válida para alcanzar _PC2_, debido a la caída del _Router1_. Esto implica que los paquetes ICMP se quedan sin camino hacia su destino. 

Cuando _Router1_ vuelve a encenderse, BGP restablece la sesión con _Router0_, permitiendo que las rutas sean anunciadas nuevamente. Por lo que reaparecen los paquetes BGP y la comunicación se normaliza. Al verificar la conectividad con `ping`, las respuestas vuelven a ser exitosas, demostrando que la red recuperó su funcionalidad.

Este comportamiento valida que **BGP** es un protocolo dinámico, capaz de adaptarse automáticamente a fallos y restaurar la comunicación en poco tiempo. La prueba evidencia cómo el tráfico se comporta ante cambios en la topología y permite confirmar que las rutas de BGP se propagan correctamente tras la recuperación del router. 

### Configuraciones para IPv6

El objetivo de esta configuración es implementar IPv6 en la infraestructura de red y verificar la conectividad entre los sistemas autónomos **AS100** y **AS200**. A continuación se describirán algunos de los pasos necesarios para asignar direcciones IPv6 a los routers, configurar BGP para el intercambio de rutas IPv6 y realizar pruebas de conectividad para observar qué comportamiento se obtiene.

Antes de configurar las direcciones IPv6, es necesario activar IPv6 en **ambos routers**. Para esto, se ejecuta el comando `ipv6 unicast-routing`. Este comando habilita IPv6, permitiendo que las interfaces trabajen con este tipo de dirección. Luego, para comprobar que IPv6 está activado, se ejecuta el comando `show running-config | include ipv6 unicast-routing`: 

![Figura 10](imagen/Figura10Parte2.png)

A partir de esto, se asignan las direcciones IPv6 globales a cada interfaz de los routers para permitir la comunicación:

**Configuración en Router0 (AS100):**

![Figura 11](imagen/Figura11Parte2.png)

**Configuración en Router1 (AS200):**

![Figura 12](imagen/Figura12Parte2.png)

Donde:

* `interface FastEthernet 0/0`: indica que se está configurando la interfaz que conecta a un router con el otro router.
* `interface FastEthernet 0/1`: indica que se está configurando la interfaz que conecta a cada router con su respectivo switch.
* `ipv6 address 2001:DB8::x00/64`: se asigna la dirección IPv6 única a la interfaz de la red. Se usa `/64`, que es la longitud de prefijo estándar en redes IPv6.
* `ipv6 route 2001:0DB8:x00::/64 2001:0DB8:10::x`: configura una ruta estática IPv6, indicando que para llegar a la red `2001:0DB8:x00::/64`, el router debe enviar los paquetes a la dirección IPv6 (`2001:0DB8:10::x`), correspondiente al otro router
* `show ipv6 interface brief`: este comando verificará todas las interfaces y sus direcciones IPv6.

A su vez, configuramos todas las direcciones IPv6 estáticas de cada uno de los hosts, teniendo en cuenta las direcciones IPv6 del Sistemas Autónomo que pertenecen, configurados en los routers:

![Figura 13](imagen/Figura13Parte2.png)
![Figura 14](imagen/Figura14Parte32.png)
![Figura 15](imagen/Figura15Parte2.png)
![Figura 16](imagen/Figura16Parte2.png)

**Prueba de conectividad:**

![Figura 17](imagen/Figura17Parte2.png)

De esta forma, el diseño de la red final lo presentamos en la siguiente tabla:

| EQUIPO |  INTERFAZ     | IP DE RED     |  IPv4      | MÁSCARA     |  IPv6  | Comments |
|------- |-------------  |---------------|------------|-------------|--------|----------|
| R0     |FastEthernet0/0| 10.0.0.0          | 10.0.0.1   |255.255.255.0|2001:0DB8:10::1/64     |Enlace con router 1          |
| R0     |FastEthernet0/1|192.168.1.0    | 192.168.1.1|255.255.255.0|2001:0DB8:100::1/64    |Red Interna AS100 (hosts y switch0)          |
| R1     |FastEthernet0/0| 10.0.0.0              | 10.0.0.2   |255.255.255.0|2001:0DB8:10::2/64     |Enlace con router 1          |
| R1     |FastEthernet0/1|192.168.2.0    | 192.168.2.1|255.255.255.0|2001:0DB8:200::1/64    |Red Interna AS200 (hosts y switch1)          |
| PC0    |FastEthernet0  |192.168.1.0    | 192.168.1.2|255.255.255.0|2001:0DB8:100::2/64    |   Host en AS100       |
| PC1    |FastEthernet0  |192.168.1.0    | 192.168.1.3|255.255.255.0|2001:0DB8:100::3/64    |Host en AS100          |
| PC2    |FastEthernet0  |192.168.2.0    | 192.168.2.2|255.255.255.0|2001:0DB8:200::2/64    |Host en AS200          |
| PC3    |FastEthernet0  |192.168.2.0    | 192.168.2.3|255.255.255.0|2001:0DB8:200::3/64    |Host en AS200          |
| SW0    |   VLAN1       |    N/A        |    N/A     |   N/A       |  N/A   |Conmutador L2 en AS100          |
| SW1    |   VLAN1       |    N/A        |    N/A     |   N/A       |  N/A   |Conmutador L2 en AS200          |

### Ampliacion del sistema autónomo

Ahora se tiene como objetivo ampliar el sistema autónomo AS100 añadiendo un nuevo router (Router2), un switch y un nuevo host (h4) conectado a ese switch, garantizando su integración al dominio de enrutamiento.

Por ese motivo vamos a adoptar la siguiente topología:
Router0 conectado a Router2 mediante un enlace punto a punto.
Router2 conectado a un switch, el cual está vinculado al host h4.

Como ya sabemos, debemos asignar direcciones IP a los componentes nuevos que integran AS100 y eso es lo que se hace a continuación.

Para el enlace Router0 ⇄ Router2: la red será `10.0.1.0/30`. En este caso se decidió utilizar una subred /30 para el enlace punto a punto, ya que solo requiere dos hosts (Router0 y Router2). Entonces:
`Router0: 10.0.1.1`
`Router2: 10.0.1.2`

Por otro lado para la red LAN del Router2 hacia h4 se decidió utilizar la red **192.168.4.0/24**:
`Router2: 192.168.4.1`
`h4: 192.168.4.10` (puerta de enlace: `192.168.4.1`)

Una vez establecido esto, pasamos a configurar cada uno de los elementos nuevos. En primer lugar configuramos el **h4** con las direcciones mencionadas anteriormente.

![Figura 18](imagen/Figura18Parte2.png)

Luego configuramos los _routers 2, 0 y 1_:

![Figura 19](imagen/Figura19Parte2.png)
![Figura 20](imagen/Figura20Parte2.png)
![Figura 21](imagen/Figura21Parte2.png)

A partir de la configuración de cada interfaz con su dirección ip correspondiente, recordamos ejecutar el comando `no shutdown`, para habilitar dicha interfaz.

Cabe destacar que en la configuración de estos routers, usamos el comando `ip route` e `ipv6 route` para establecer rutas estáticas para comprobar la conexión de la red. Sin embargo, estas rutas serán eliminadas, más adelante, para poder experimentar el comportamiento de OSPF y BGP.

Ya realizadas las configuraciones, comprobamos desde **h4** la conexión con los otros hosts:

![Figura 22](imagen/Figura22Parte2.png)

**Incorporación de protocolo OSPF**

Una vez incorporado este nuevo router y host en AS100,vamos a sustituir las rutas estáticas en AS100 por OSPF como mencionamos anteriormente. Este protocolo de enrutamiento interior nos va a permitir el descubrimiento dinámico de rutas y escalabilidad a diferencia de las rutas estáticas.

Para realizar dicha tarea debemos anunciar ambas redes internas del AS100 en el área 0, que es la principal área backbone de OSPF. Lo mismo con el enlace punto a punto, para garantizar la conectividad entre routers. Procedemos a configurar ambos routers, tanto en IPv4 como en IPv6:

![Figura 23](imagen/Figura23Parte2.png)
![Figura 24](imagen/Figura24Parte2.png)

Como podemos observar, primero iniciamos el proceso OSPF número 1 con el comando `router ospf 1`. Luego con el comando `network [IP] [máscara] area [área]`, incluimos la red correspondiente en el área 0 de OSPF. La máscara `0.0.0.3` corresponde a `/30` y `0.0.0.255` a `/24`, tal como lo configuramos anteriormente.

En **OSPFv3 (IPv6)**, la asignación del área se hace directamente en la interfaz con `ipv6 ospf [ID] area [área]`, como se observa en las imagenes.

Una vez configurado OSPF en AS100, validamos la conexión de las rutas, con el comando `show ip route` y `show ipv6 route`

![Figura 25](imagen/Figura25Parte2.png)
![Figura 26](imagen/Figura26Parte2.png)

Las rutas **OSPF** son aquellas que están identificadas con la letra **“O”**, tal como se aprecia en las imagenes.  

En el _Router2_ podemos encontrar:
La ruta de la red interna perteneciente al _router0_, tanto en IPv4 (`192.168.1.0/24`) como en IPv6 (`2001:DB8:100::/64`)
Por otro lado, en el _router0_ se ve:
La ruta de la red interna perteneciente al router2, tanto en IPv4 (`192.168.4.0/24`) como en IPv6 (`2001:DB8:104::/64`)

**Redistribuir OSPF en BGP.**

Como ya tenemos la configuración OSPF en AS100 ahora podemos redistribuirla en BGP.

Primero nos vamos a asegurar de eliminar todas las rutas estáticas que hayamos configurado anteriormente, para cumplir con el objetivo propuesto. Luego continuaremos con la redistribución de OSPF en BGP, para permitir que estos manejen el enrutamiento de forma dinámica. 

Configuramos el _router0_ y el _router1_:

![Figura 27](imagen/Figura27Parte2.png)
![Figura 28](imagen/Figura28Parte2.png)

En dichas imágenes, podemos observar el uso de ciertos comandos:

`router bgp [AS]`: iniciamos el proceso BGP para el sistema autónomo indicado.
`neighbor [IP] remote-as [AS]`: establecemos una sesión eBGP con el router indicado.
`redistribute ospf 1`: en el router0 permitimos que las rutas OSPF aprendidas sean exportadas al dominio BGP.
`network …`: en el router1 anunciamos explícitamente una red local a BGP (solo en Router1)

Cabe mencionar que se necesitó lanzar el comando `clear ip bgp *` para que en las tablas de ruteo que se ven a continuación, aparezcan las rutas BGP redistribuidas:

![Figura 29](imagen/Figura29Parte2.png)

![Figura 30](imagen/Figura30Parte2.png)

Las rutas BGP aparecen en las tablas identificadas con la letra **“B”**. Por lo que, analizando dichas tablas, podemos decir que:

El _Router1_ aprendió mediante BGP las rutas `192.168.1.0/24` y `192.168.4.0/24` (ambas del AS100).
El _Router0_ aprendió la red `192.168.2.0/24` perteneciente a AS200, desde Router1, gracias a BGP.

Finalmente, como ambos sistemas autónomos se conocen gracias a BGP, podemos comprobar la conexión entre los mismos, realizando pings desde el **host número 4**:

![Figura 31](imagen/Figura31Parte2.png)

Tal como se ve en la imágen, todos los pings resultan exitosos, asegurando la conexión de AS100 y AS200. De esta manera, podemos concluir que gracias a la redistribución de OSPF en BGP, el router1, perteneciente al sistema autónomo AS200, tiene acceso completo a las redes internas del AS100. La integración entre ambos sistemas autónomos es funcional y permite comunicación entre los hosts (como h2 en AS200 y h4 en AS100), validando así el correcto funcionamiento del enrutamiento dinámico entre ambos AS, mediante los protocolos mencionados.

## Referencias
- [1] https://www.youtube.com/watch?v=CT4xaXLcnpM&ab_channel=Udacity
- [2] https://www.peeringdb.com/asn/7303
- [3] https://bgp.he.net/AS7303
- [4] https://bgp.tools/as/7303
- [5] https://www.cloudflare.com/es-es/learning/network-layer/what-is-an-autonomous-system/	
- [6] https://www.geeksforgeeks.org/difference-between-distance-vector-routing-and-link-state-routing/
- [7] https://avrohomg.medium.com/the-facebook-outage-of-2021-6231bf99ff57

- [8] https://es.wikipedia.org/wiki/Apag%C3%B3n_de_Facebook_de_2021
- [9] https://blog.cloudflare.com/october-2021-facebook-outage
- [10] https://engineering.fb.com/2021/10/04/networking-traffic/outage/

