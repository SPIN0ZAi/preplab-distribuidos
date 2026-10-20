# scripts/generators/lab1_part1.py
# -*- coding: utf-8 -*-
"""
Lab 1 Questions 1 to 70:
- lab1-001 to lab1-010: Teacher's 10 original Campus Virtual questions verbatim.
- lab1-011 to lab1-040: Contenedores vs Máquinas Virtuales (kernel sharing, namespaces, cgroups, hypervisors, overhead).
- lab1-041 to lab1-070: Arquitectura Docker Engine (dockerd, REST API, containerd, runc, OCI, Docker Hub, union fs).
"""

def get_questions():
    questions = []

    # =========================================================================
    # TEACHER'S 10 ORIGINAL QUESTIONS (lab1-001 to lab1-010)
    # =========================================================================
    questions.append({
        "id": "lab1-001",
        "lab": 1,
        "topic": "Dockerfile e Imágenes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué archivo se usa para construir imágenes personalizadas en Docker?",
        "options": [
            {"id": "a", "text": "docker-config"},
            {"id": "b", "text": "Dockerfile"},
            {"id": "c", "text": "DockerCompose"},
            {"id": "d", "text": "DockeFile.txt"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "El archivo estándar reconocido por el motor de Docker para definir los pasos de construcción de una imagen es 'Dockerfile' (sin extensión).",
            "wrong": {
                "a": "'docker-config' no es el nombre estándar del archivo de construcción en Docker.",
                "c": "'DockerCompose' es para orquestación de múltiples contenedores (docker-compose.yml), no para compilar una sola imagen.",
                "d": "'DockeFile.txt' contiene una errata tipográfica y una extensión .txt no recomendada en Docker."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 1"
    })

    questions.append({
        "id": "lab1-002",
        "lab": 1,
        "topic": "Redes y Mapeo de Puertos",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué hace el parámetro \"-p\" en el comando \"docker run\"?",
        "options": [
            {"id": "a", "text": "Mapea puertos del host al contenedor"},
            {"id": "b", "text": "Asigna un nombre al contenedor"},
            {"id": "c", "text": "Indica el proceso en el host"},
            {"id": "d", "text": "Asigna el puerto por defecto que usa el contenedor"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "El parámetro '-p' publica un puerto enlazándolo entre la máquina anfitriona (host) y el contenedor (-p puertoHost:puertoContenedor).",
            "wrong": {
                "b": "Asignar un nombre al contenedor se hace con el parámetro '--name'.",
                "c": "No interactúa con el identificador de proceso (PID) del host; se encarga del redireccionamiento de red.",
                "d": "El puerto por defecto que escucha la aplicación se define en el Dockerfile mediante la directiva EXPOSE."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 2"
    })

    questions.append({
        "id": "lab1-003",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué comando de Docker se usa para ver los contenedores activos?",
        "options": [
            {"id": "a", "text": "docker info"},
            {"id": "b", "text": "docker ls"},
            {"id": "c", "text": "docker ps -a"},
            {"id": "d", "text": "docker ps"}
        ],
        "correct": ["d"],
        "explanation": {
            "correct": "'docker ps' lista exclusivamente los contenedores que se encuentran en ejecución (activos).",
            "wrong": {
                "a": "'docker info' muestra información general del sistema y del demonio Docker Engine.",
                "b": "'docker ls' no existe como comando global en Docker.",
                "c": "'docker ps -a' muestra todos los contenedores existentes, incluyendo los detenidos."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 3"
    })

    questions.append({
        "id": "lab1-004",
        "lab": 1,
        "topic": "Ciclo de Vida de Contenedores",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Con qué comando se eliminan contenedores detenidos?",
        "options": [
            {"id": "a", "text": "docker remove"},
            {"id": "b", "text": "docker rm"},
            {"id": "c", "text": "docker stop"},
            {"id": "d", "text": "docker kill"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "'docker rm <id-contenedor>' elimina contenedores que ya no están en ejecución.",
            "wrong": {
                "a": "'docker remove' no es la sintaxis admitida por el CLI de Docker.",
                "c": "'docker stop' detiene la ejecución del contenedor de forma limpia, pero no lo borra del almacenamiento.",
                "d": "'docker kill' interrumpe forzosamente el contenedor enviando SIGKILL, pero no borra su registro en disco."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 4"
    })

    questions.append({
        "id": "lab1-005",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Para qué sirve el comando docker logs?",
        "options": [
            {"id": "a", "text": "Eliminar los logs"},
            {"id": "b", "text": "Crear logs"},
            {"id": "c", "text": "Mandar logs al host"},
            {"id": "d", "text": "Consultar logs de un contenedor en concreto"}
        ],
        "correct": ["d"],
        "explanation": {
            "correct": "'docker logs' recopila e imprime las salidas estándar (stdout y stderr) generadas por el proceso principal de un contenedor.",
            "wrong": {
                "a": "No borra archivos de log existentes en el demonio.",
                "b": "No genera entradas de log ficticias; muestra la salida emitida por la aplicación.",
                "c": "No transporta logs a servidores de logging remotos del host de manera directa."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 5"
    })

    questions.append({
        "id": "lab1-006",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "easy",
        "type": "truefalse",
        "question": "En un sistema informático, se pueden ejecutar más máquinas virtuales que contenedores.",
        "options": [
            {"id": "a", "text": "Verdadero"},
            {"id": "b", "text": "Falso"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "Es Falso. Los contenedores comparten el kernel del host y no necesitan una capa completa de SO invitado ni virtualización de hardware, lo que permite ejecutar una densidad mucho mayor de contenedores que de máquinas virtuales.",
            "wrong": {
                "a": "Es incorrecto. Las máquinas virtuales requieren duplicar el kernel, la memoria dedicada y los servicios del sistema operativo, consumiendo muchísimos más recursos."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 6"
    })

    questions.append({
        "id": "lab1-007",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Para qué sirve el comando \"docker run\"?",
        "options": [
            {"id": "a", "text": "Borrar un volumen"},
            {"id": "b", "text": "Crear una imagen en Docker"},
            {"id": "c", "text": "Crear una red nueva"},
            {"id": "d", "text": "Crear y ejecutar un contenedor"}
        ],
        "correct": ["d"],
        "explanation": {
            "correct": "'docker run' instancia una nueva capa de lectura/escritura a partir de la imagen especificada y arranca su proceso.",
            "wrong": {
                "a": "Para borrar volúmenes se utiliza 'docker volume rm'.",
                "b": "Para construir imágenes se emplea 'docker build'.",
                "c": "Para crear redes se ejecuta 'docker network create'."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 7"
    })

    questions.append({
        "id": "lab1-008",
        "lab": 1,
        "topic": "Redes y Mapeo de Puertos",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué comando de Docker muestra todas las redes existentes?",
        "options": [
            {"id": "a", "text": "docker ls net"},
            {"id": "b", "text": "dotnet network ls"},
            {"id": "c", "text": "docker network ls"},
            {"id": "d", "text": "docker networks"}
        ],
        "correct": ["c"],
        "explanation": {
            "correct": "'docker network ls' enumera todas las redes configuradas en el demonio de Docker.",
            "wrong": {
                "a": "'docker ls net' es una combinación sintáctica no admitida en Docker CLI.",
                "b": "'dotnet network ls' pertenece a .NET y no tiene herramientas de administración de red.",
                "d": "'docker networks' no es un comando reconocido."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 8"
    })

    questions.append({
        "id": "lab1-009",
        "lab": 1,
        "topic": "Gestión de Imágenes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Cómo se eliminan imágenes en Docker?",
        "options": [
            {"id": "a", "text": "docker image delete"},
            {"id": "b", "text": "docker image rm"},
            {"id": "c", "text": "docker image clear"},
            {"id": "d", "text": "docker remove image"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "'docker image rm' (o 'docker rmi') borra una o varias imágenes locales.",
            "wrong": {
                "a": "'docker image delete' no existe como subcomando en Docker.",
                "c": "'docker image clear' no es un comando de Docker.",
                "d": "'docker remove image' no coincide con la gramática objeto-verbo de Docker CLI."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 9"
    })

    questions.append({
        "id": "lab1-010",
        "lab": 1,
        "topic": "Gestión de Imágenes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Para qué sirve el comando \"docker images\"?",
        "options": [
            {"id": "a", "text": "Listar los contenedores en ejecución"},
            {"id": "b", "text": "Listar las imágenes locales"},
            {"id": "c", "text": "Crear una imagen"},
            {"id": "d", "text": "Borrar imágenes"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "'docker images' muestra todas las imágenes descargadas o compiladas que residen localmente en el host.",
            "wrong": {
                "a": "Listar contenedores en ejecución es la función de 'docker ps'.",
                "c": "Crear imágenes a partir de un Dockerfile se hace con 'docker build'.",
                "d": "Borrar imágenes se hace con 'docker image rm'."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 10"
    })

    # =========================================================================
    # CONTENEDORES VS MÁQUINAS VIRTUALES (lab1-011 to lab1-040)
    # =========================================================================
    vm_vs_c = [
        ("lab1-011", "¿Cuál es la diferencia arquitectónica principal entre un contenedor y una máquina virtual tradicional?",
         [("a", "Los contenedores comparten el kernel del sistema operativo anfitrión, mientras que las máquinas virtuales ejecutan su propio sistema operativo invitado completo sobre un hipervisor."),
          ("b", "Los contenedores virtualizan las instrucciones del hardware físico mediante un hipervisor Tipo 1."),
          ("c", "Las máquinas virtuales no requieren memoria RAM dedicada y comparten el kernel del host."),
          ("d", "Los contenedores siempre emulan una CPU x86 completa para cada proceso.")],
         ["a"], "medium", "single",
         "Los contenedores operan a nivel de sistema operativo compartiendo el kernel subyacente, lo que elimina el hipervisor y el SO invitado redundante.",
         {"b": "La virtualización de hardware mediante hipervisor corresponde a las máquinas virtuales, no a los contenedores.",
          "c": "Las máquinas virtuales sí requieren memoria asignada y un kernel propio independiente.",
          "d": "Los contenedores ejecutan binarios directamente en la CPU del host sin emulación de hardware."}),

        ("lab1-012", "¿Qué primitiva del kernel de Linux es responsable de aislar los recursos visibles para un contenedor (como procesos, red y sistemas de archivos)?",
         [("a", "Control Groups (cgroups)"),
          ("b", "Linux Namespaces"),
          ("c", "Hypervisor KVM"),
          ("d", "AppArmor Profiles")],
         ["b"], "medium", "single",
         "Los Namespaces proporcionan aislamiento al particionar los recursos globales del kernel (PID, NET, IPC, MNT, UTS, USER) para que cada contenedor vea su propia vista independiente.",
         {"a": "cgroups limita y mide el uso de recursos (CPU, memoria, I/O), pero no aísla la visibilidad.",
          "c": "KVM es un módulo de hipervisor para virtualización completa mediante máquinas virtuales.",
          "d": "AppArmor restringe las capacidades de seguridad de los programas pero no genera el aislamiento de recursos."}),

        ("lab1-013", "¿Qué primitiva del kernel de Linux se utiliza para limitar y monitorizar el consumo de recursos como CPU y memoria de un contenedor?",
         [("a", "Control Groups (cgroups)"),
          ("b", "Namespaces UTS"),
          ("c", "Systemd Services"),
          ("d", "Chroot Jails")],
         ["a"], "medium", "single",
         "cgroups (Control Groups) permite regular la cantidad de recursos hardware (tiempo de CPU, límites de memoria RAM, ancho de banda de red y I/O de disco) que puede consumir un grupo de procesos.",
         {"b": "UTS Namespace aísla el hostname y el nombre de dominio.",
          "c": "Systemd es el sistema de inicio y gestor de servicios de Linux, no la primitiva de limitación de recursos.",
          "d": "Chroot solo cambia la raíz del árbol de directorios para un proceso."}),

        ("lab1-014", "¿Por qué el tiempo de arranque de un contenedor es típicamente de milisegundos a pocos segundos en comparación con los minutos de una máquina virtual?",
         [("a", "Porque el contenedor no necesita inicializar hardware virtualizado ni arrancar un kernel de sistema operativo desde cero; solo lanza un proceso."),
          ("b", "Porque los contenedores se almacenan siempre en la memoria caché L3 de la CPU del servidor."),
          ("c", "Porque las máquinas virtuales no utilizan compilación Just-In-Time."),
          ("d", "Porque Docker precarga todas las imágenes en la memoria RAM antes de arrancar.")],
         ["a"], "easy", "single",
         "Al arrancar un contenedor, el kernel del host ya está en ejecución; simplemente se crea un nuevo conjunto de namespaces y cgroups y se ejecuta el proceso binario directamente.",
         {"b": "Los contenedores no se almacenan permanentemente en la caché L3 del procesador.",
          "c": "El tipo de compilador de la aplicación no define la sobrecarga de arranque del hipervisor.",
          "d": "Docker no precarga todas las imágenes en RAM de forma arbitraria."}),

        ("lab1-015", "¿Qué namespace de Linux permite a un contenedor tener su propia tabla de enrutamiento, interfaces virtuales y direcciones IP independientes?",
         [("a", "PID Namespace"),
          ("b", "NET Namespace"),
          ("c", "MNT Namespace"),
          ("d", "IPC Namespace")],
         ["b"], "medium", "single",
         "El Network (NET) Namespace aísla la pila de red, incluyendo interfaces de red (como eth0), tablas de rutas, reglas de cortafuegos y números de puerto.",
         {"a": "PID Namespace aísla el árbol de identificadores de procesos.",
          "c": "MNT Namespace aísla los puntos de montaje del sistema de archivos.",
          "d": "IPC Namespace aísla la comunicación entre procesos (semáforos y colas de mensajes POSIX/SysV)."}),

        ("lab1-016", "¿Qué namespace de Linux permite que el proceso principal dentro de un contenedor tenga el identificador PID 1 a pesar de tener otro PID en el host?",
         [("a", "PID Namespace"),
          ("b", "USER Namespace"),
          ("c", "UTS Namespace"),
          ("d", "CGROUP Namespace")],
         ["a"], "medium", "single",
         "El Process ID (PID) Namespace reasigna los identificadores de procesos de forma que el proceso raíz del contenedor se ejecute como PID 1 en su propio espacio.",
         {"b": "USER Namespace mapea UID y GID de usuarios entre el contenedor y el host.",
          "c": "UTS Namespace aísla el nombre de host (hostname).",
          "d": "CGROUP Namespace virtualiza la vista del directorio /proc/$PID/cgroup."}),

        ("lab1-017", "¿Cuál de las siguientes afirmaciones sobre la sobrecarga (overhead) de los contenedores frente a las máquinas virtuales es correcta?",
         [("a", "Los contenedores presentan un overhead prácticamente nulo de CPU y memoria porque ejecutan instrucciones nativamente en el kernel del host."),
          ("b", "Los contenedores consumen el doble de memoria RAM porque deben virtualizar cada llamada al sistema."),
          ("c", "Las máquinas virtuales siempre son más ligeras en almacenamiento porque comprimen automáticamente el disco duro."),
          ("d", "El hipervisor no añade ninguna penalización de rendimiento respecto al hardware real.")],
         ["a"], "medium", "single",
         "Dado que no hay capa de traducción de hardware ni hipervisor interceptando llamadas de CPU, los contenedores ejecutan código a velocidad casi nativa.",
         {"b": "Los contenedores no duplican llamadas al sistema ni las virtualizan; las ejecutan sobre el kernel del host.",
          "c": "Las imágenes de máquinas virtuales ocupan gigabytes por contener el sistema operativo completo, mientras los contenedores comparten capas.",
          "d": "Cualquier hipervisor introduce sobrecarga en la emulación de CPU, interrupciones y traducción de memoria MMU."}),

        ("lab1-018", "¿Qué sucede si el kernel del sistema operativo anfitrión experimenta un kernel panic?",
         [("a", "Todos los contenedores en ejecución en ese host se detendrán de inmediato porque comparten dicho kernel."),
          ("b", "Solo los contenedores que usan la red bridge se detendrán, los demás continuarán."),
          ("c", "Docker reiniciará automáticamente un kernel secundario independiente para cada contenedor."),
          ("d", "Los contenedores continuarán funcionando normalmente gracias al hipervisor containerd.")],
         ["a"], "hard", "single",
         "Debido a que todos los contenedores comparten el mismo kernel del anfitrión, un fallo crítico del kernel inhabilita la máquina y a todos sus contenedores.",
         {"b": "El subsistema de red no protege al sistema operativo frente a un kernel panic.",
          "c": "Docker no contiene kernels adicionales de respaldo dentro de sus capas.",
          "d": "containerd es un demonio de gestión de procesos OCI en espacio de usuario, no un hipervisor con kernel propio."}),

        ("lab1-019", "Un contenedor Linux puede ejecutarse directamente sin ninguna capa de emulación ni máquina virtual sobre un kernel de Windows nativo.",
         [("a", "Verdadero"),
          ("b", "Falso")],
         ["b"], "medium", "truefalse",
         "Es Falso. Los contenedores Linux requieren las llamadas al sistema del kernel de Linux. En Windows, Docker Desktop utiliza WSL2 (Windows Subsystem for Linux) o una VM Hyper-V para proporcionar dicho kernel.",
         {"a": "Es incorrecto porque Windows posee una arquitectura de kernel distinta (NT) incompatible con binarios ELF y llamadas al sistema Linux."}),

        ("lab1-020", "¿Cuál es la principal ventaja de utilizar contenedores en entornos de integración y despliegue continuo (CI/CD)?",
         [("a", "Garantizan la reproducibilidad e inmutabilidad del entorno, eliminando el problema de 'en mi máquina funciona'."),
          ("b", "Permiten compilar código C# sin necesidad de tener el SDK de .NET instalado en ningún lugar."),
          ("c", "Multiplican por diez la velocidad de la tarjeta de red física del servidor."),
          ("d", "Eliminan la necesidad de escribir pruebas unitarias de software.")],
         ["a"], "easy", "single",
         "Empaquetar la aplicación con todas sus dependencias exactas, bibliotecas y configuraciones garantiza que se ejecute de forma idéntica en desarrollo, staging y producción.",
         {"b": "El SDK de .NET sigue siendo necesario para compilar, aunque se incluye dentro de la imagen de compilación.",
          "c": "Los contenedores no modifican las especificaciones físicas del hardware de red.",
          "d": "Las pruebas unitarias y de integración siguen siendo indispensables para la calidad del software."}),

        ("lab1-021", "¿Qué diferencias existen entre un hipervisor de Tipo 1 (Bare Metal) y un hipervisor de Tipo 2 (Hosted)?",
         [("a", "El Tipo 1 se ejecuta directamente sobre el hardware físico sin SO intermedio, mientras que el Tipo 2 se ejecuta como una aplicación sobre un sistema operativo anfitrión."),
          ("b", "El Tipo 1 solo admite contenedores Docker y el Tipo 2 solo admite Kubernetes."),
          ("c", "El Tipo 1 requiere emular siempre arquitectura ARM sobre x86."),
          ("d", "El Tipo 2 ofrece mayor rendimiento que el Tipo 1 debido al uso de llamadas directas al BIOS.")],
         ["a"], "hard", "single",
         "Los hipervisores Tipo 1 (como VMware ESXi, Proxmox o Xen) se ejecutan directamente sobre el silicio para máximo rendimiento, mientras que los Tipo 2 (como VirtualBox o VMware Workstation) corren sobre un SO convencional.",
         {"b": "Los hipervisores gestionan máquinas virtuales completas, no son tecnologías de orquestación de contenedores.",
          "c": "La arquitectura física de la CPU determina la ejecución; no se limita a emulación ARM.",
          "d": "El Tipo 2 sufre mayor latencia porque todas las operaciones pasan por el SO anfitrión."}),

        ("lab1-022", "¿Qué componente de Linux proporciona el aislamiento de sistemas de archivos de forma que cada contenedor tenga su propio árbol de directorios raíz '/'?",
         [("a", "Mount (MNT) Namespace junto con chroot / pivot_root"),
          ("b", "IPC Namespace"),
          ("c", "Memory cgroup controller"),
          ("d", "Netfilter iptables")],
         ["a"], "hard", "single",
         "El MNT Namespace combinado con pivot_root altera la raíz visible del sistema de archivos, aislando completamente las rutas de disco del contenedor respecto al host.",
         {"b": "IPC Namespace controla colas de mensajes y memoria compartida.",
          "c": "Memory cgroup gestiona cuotas de memoria RAM.",
          "d": "Netfilter / iptables gestiona el cortafuegos y la redirección de paquetes de red."}),

        ("lab1-023", "¿Qué sucede cuando un proceso en un contenedor excede el límite de memoria RAM configurado mediante cgroups?",
         [("a", "El Out-Of-Memory (OOM) Killer del kernel termina forzosamente el proceso principal del contenedor (código de salida 137)."),
          ("b", "Docker expande automáticamente la memoria física del host usando compresión zRAM."),
          ("c", "El contenedor se pausa indefinidamente sin consumir CPU hasta que el usuario ejecute docker unpause."),
          ("d", "El kernel descarta los archivos del contenedor y lo convierte en una imagen.")],
         ["a"], "hard", "single",
         "Cuando se agota el límite asignado al cgroup de memoria y el espacio swap configurado, el kernel activa el OOM Killer para proteger la estabilidad del sistema.",
         {"b": "Docker no puede crear memoria física de hardware que no exista en el host.",
          "c": "El contenedor no se pausa; el proceso es destruido con señal SIGKILL (128 + 9 = 137).",
          "d": "Los archivos no se eliminan mágicamente ni se transforman en imágenes."}),

        ("lab1-024", "¿Qué permite el User Namespace (userns) en Docker en relación con la seguridad de contenedores?",
         [("a", "Permite que el usuario 'root' (UID 0) dentro del contenedor sea mapeado a un usuario sin privilegios en el host."),
          ("b", "Permite que cualquier usuario de la red local acceda al contenedor sin contraseña."),
          ("c", "Obliga a que todos los contenedores compartan la misma cuenta de usuario de Active Directory."),
          ("d", "Desactiva los permisos de lectura y escritura en los discos SSD.")],
         ["a"], "hard", "single",
         "User Namespaces proporciona contención de privilegios: si un atacante escapa del contenedor, solo tendrá permisos de un usuario estándar no privilegiado en la máquina física.",
         {"b": "No tiene relación con la autenticación remota o contraseñas de red.",
          "c": "No interactúa de forma obligatoria con directorios LDAP o Active Directory.",
          "d": "No tiene nada que ver con el hardware de almacenamiento SSD."}),

        ("lab1-025", "En términos de densidad de cómputo en un servidor de 64 GB de RAM, ¿cuál de los siguientes enfoques permite ejecutar una mayor cantidad de instancias de microservicios?",
         [("a", "Contenedores Docker"),
          ("b", "Máquinas Virtuales KVM completas"),
          ("c", "Máquinas Virtuales VMware con Windows Server en cada una"),
          ("d", "Ambos enfoques permiten exactamente la misma cantidad de instancias")],
         ["a"], "easy", "single",
         "Dado que los contenedores no cargan sistemas operativos duplicados y comparten memoria de bibliotecas y kernel, pueden empaquetarse en órdenes de magnitud superiores (cientos de contenedores frente a decenas de VMs).",
         {"b": "Las máquinas virtuales KVM requieren asignar memoria fija dedicada y SO para cada instancia.",
          "c": "Windows Server como SO invitado en cada VM consume varios gigabytes solo para arrancar el sistema.",
          "d": "La diferencia de consumo de memoria entre ambos modelos es masiva."}),

        ("lab1-026", "¿Qué namespace de Linux se encarga de aislar los identificadores de comunicación entre procesos (IPC) como los segmentos de memoria compartida System V y colas de mensajes POSIX?",
         [("a", "IPC Namespace"),
          ("b", "UTS Namespace"),
          ("c", "MNT Namespace"),
          ("d", "NET Namespace")],
         ["a"], "medium", "single",
         "El IPC Namespace previene que los procesos dentro de un contenedor interactúen o corrompan la memoria compartida o colas de mensajes de procesos fuera de su entorno.",
         {"b": "UTS aísla el hostname del sistema.",
          "c": "MNT aísla los puntos de montaje del disco.",
          "d": "NET aísla las interfaces y sockets de red."}),

        ("lab1-027", "¿Qué namespace de Linux permite a un contenedor tener su propio nombre de máquina (hostname) independiente del nombre de la máquina anfitriona?",
         [("a", "UTS Namespace"),
          ("b", "PID Namespace"),
          ("c", "USER Namespace"),
          ("d", "NET Namespace")],
         ["a"], "medium", "single",
         "El UTS (UNIX Timesharing System) Namespace permite que cada contenedor defina su propio hostname y domain name sin alterar el host.",
         {"b": "PID aísla el árbol de procesos.",
          "c": "USER aísla los identificadores de usuario UID y grupo GID.",
          "d": "NET aísla las tablas de enrutamiento y puertos de red."}),

        ("lab1-028", "¿Cuáles de las siguientes opciones corresponden a tecnologías o primitivas fundamentales sobre las que se basa Docker en Linux? (Selecciona todas las correctas)",
         [("a", "Namespaces del Kernel"),
          ("b", "Control Groups (cgroups)"),
          ("c", "Sistemas de archivos UnionFS (como Overlay2)"),
          ("d", "Hipervisor ESXi")],
         ["a", "b", "c"], "hard", "multi",
         "Docker se apoya en Namespaces (para aislamiento), cgroups (para control y limitación de recursos) y UnionFS/Overlay2 (para capas de imágenes eficientes).",
         {"d": "ESXi es un hipervisor propietario tipo 1 de VMware para máquinas virtuales, no una tecnología del kernel Linux para contenedores."}),

        ("lab1-029", "Las imágenes de contenedor son plantillas inmutables de solo lectura a partir de las cuales se crean los contenedores.",
         [("a", "Verdadero"),
          ("b", "Falso")],
         ["a"], "easy", "truefalse",
         "Es Verdadero. Una imagen está compuesta por una serie de capas de solo lectura apiladas. Al instanciar un contenedor, Docker añade únicamente una capa delgada de lectura y escritura encima.",
         {"b": "Es incorrecto. Las capas de una imagen son estrictamente de solo lectura y nunca se modifican en tiempo de ejecución."}),

        ("lab1-030", "¿Qué ocurre cuando dos contenedores distintos se ejecutan a partir de la misma imagen base 'ubuntu:22.04' en el mismo servidor?",
         [("a", "Ambos contenedores comparten en memoria las capas de solo lectura de la imagen, teniendo cada uno su propia capa de lectura/escritura independiente."),
          ("b", "Docker duplica físicamente los 70 MB de la imagen en dos ubicaciones de disco diferentes para evitar conflictos."),
          ("c", "El segundo contenedor no puede arrancar hasta que el primero se detenga."),
          ("d", "Cualquier archivo creado en el primer contenedor se vuelve visible inmediatamente en el segundo.")],
         ["a"], "medium", "single",
         "El sistema de almacenamiento por capas reutiliza los bloques de solo lectura, minimizando drásticamente el espacio en disco y el uso de caché de memoria de la página del kernel.",
         {"b": "El motor de almacenamiento no duplica las capas; utiliza punteros y Copy-on-Write.",
          "c": "Se pueden ejecutar cientos de contenedores concurrentes a partir de una misma imagen.",
          "d": "Cada contenedor tiene su propia capa superior de lectura/escritura aislada; no comparten modificaciones a menos que se use un volumen compartido."}),

        ("lab1-031", "¿Cuál es el rol del mecanismo Copy-on-Write (CoW) en el almacenamiento de contenedores?",
         [("a", "Permite que un archivo perteneciente a una capa de solo lectura solo se copie a la capa escribible del contenedor en el momento en que se intenta modificar."),
          ("b", "Obliga a escribir todos los cambios directamente en la memoria NVRAM del servidor."),
          ("c", "Copia automáticamente todos los datos del contenedor en un repositorio de GitHub."),
          ("d", "Bloquea cualquier intento de escritura por parte de la aplicación dentro del contenedor.")],
         ["a"], "medium", "single",
         "Copy-on-Write garantiza que los archivos de la imagen subyacente permanezcan inalterados; la primera modificación copia el archivo hacia la capa superior de trabajo del contenedor específico.",
         {"b": "No interactúa con memorias NVRAM de hardware.",
          "c": "No tiene integración con servicios externos como GitHub.",
          "d": "No bloquea la escritura; la gestiona eficientemente redirigiéndola a la capa de trabajo."}),

        ("lab1-032", "¿Qué herramienta proporciona una especificación estándar abierta (OCI) para formatos de imágenes y tiempos de ejecución de contenedores?",
         [("a", "Open Container Initiative (OCI)"),
          ("b", "ISO 9001"),
          ("c", "W3C Consortium"),
          ("d", "IEEE Computer Society")],
         ["a"], "medium", "single",
         "La OCI (Open Container Initiative) es un proyecto de gobernanza abierta creado para diseñar estándares de la industria en torno a los formatos de contenedores e imagen (image-spec y runtime-spec).",
         {"b": "ISO 9001 es una norma de gestión de calidad.",
          "c": "W3C se enfoca en estándares de la World Wide Web (HTML, CSS).",
          "d": "IEEE elabora estándares de ingeniería eléctrica y redes como 802.11."}),

        ("lab1-033", "¿Qué diferencia fundamental existe entre parar un contenedor (`docker stop`) y destruirlo (`docker rm`)?",
         [("a", "`docker stop` detiene los procesos del contenedor preservando su estado y capa escribible en disco, mientras que `docker rm` elimina por completo el contenedor y su capa de escritura."),
          ("b", "`docker stop` elimina la imagen base y `docker rm` reinicia la máquina física."),
          ("c", "`docker stop` solo funciona en Windows y `docker rm` en Linux."),
          ("d", "No existe ninguna diferencia; ambos comandos son sinónimos.")],
         ["a"], "easy", "single",
         "Un contenedor detenido mantiene sus datos y configuraciones y puede reactivarse con `docker start`. Al ejecutar `docker rm`, se destruye su capa escribible asociada.",
         {"b": "Ninguno de los dos comandos borra la imagen base ni reinicia el servidor anfitrión.",
          "c": "Ambos comandos son estándar en cualquier sistema operativo soportado por Docker Engine.",
          "d": "Tienen efectos completamente distintos en el ciclo de vida del contenedor."}),

        ("lab1-034", "Si se borra un contenedor con `docker rm`, ¿se eliminan también las imágenes de Docker a partir de las cuales se construyó?",
         [("a", "Verdadero"),
          ("b", "Falso")],
         ["b"], "easy", "truefalse",
         "Es Falso. La imagen base permanece intacta en el almacenamiento local del host. Para eliminar una imagen debe usarse explícitamente `docker image rm` (o `docker rmi`).",
         {"a": "Es incorrecto. El ciclo de vida de los contenedores es independiente de la persistencia de las imágenes de solo lectura."}),

        ("lab1-035", "¿Por qué se dice que los contenedores promueven una arquitectura de microservicios eficiente?",
         [("a", "Porque su ligereza permite aislar cada servicio con sus propias dependencias y escalar horizontalmente instancias de forma granular."),
          ("b", "Porque un solo contenedor puede sustituir a todas las bases de datos relacionales del mundo."),
          ("c", "Porque obligan a programar exclusivamente en ensamblador."),
          ("d", "Porque reemplazan la necesidad de usar cables de red en los centros de datos.")],
         ["a"], "easy", "single",
         "Los microservicios se benefician de la baja sobrecarga y aislamiento de los contenedores para arrancar réplicas rápidamente en función de la demanda de tráfico.",
         {"b": "Los contenedores ejecutan servicios de bases de datos, no las reemplazan por arte de magia.",
          "c": "Se puede usar cualquier lenguaje de programación (.NET, Java, Python, Go, Node.js, etc.).",
          "d": "La infraestructura de red física sigue siendo indispensable."}),

        # =========================================================================
        # ARQUITECTURA DOCKER ENGINE (lab1-036 to lab1-070)
        # =========================================================================
        ("lab1-036", "¿Cuáles son los tres componentes principales de la arquitectura de Docker Engine?",
         [("a", "El cliente Docker CLI, la API REST del demonio y el demonio dockerd"),
          ("b", "El BIOS, el hipervisor KVM y la tarjeta gráfica"),
          ("c", "El compilador Roslyn, NuGet y el runtime de Blazor"),
          ("d", "Nginx, Apache HTTP Server y el protocolo gRPC")],
         ["a"], "medium", "single",
         "Docker Engine sigue una arquitectura cliente-servidor donde la CLI envía comandos a través de una API REST al demonio de fondo (dockerd).",
         {"b": "Estos son componentes de hardware y virtualización completa de sistemas.",
          "c": "Estos son componentes del ecosistema de desarrollo de Microsoft .NET.",
          "d": "Estos son servidores web y frameworks de transporte remoto."}),

        ("lab1-037", "¿A través de qué socket local se comunica por defecto el cliente de Docker CLI con el demonio dockerd en un sistema Linux?",
         [("a", "/var/run/docker.sock"),
          ("b", "/etc/docker/daemon.json"),
          ("c", "/dev/null"),
          ("d", "/opt/docker/socket.bin")],
         ["a"], "medium", "single",
         "La comunicación por defecto utiliza el socket de dominio UNIX ubicado en `/var/run/docker.sock` (o `/run/docker.sock`).",
         {"b": "`/etc/docker/daemon.json` es el archivo de configuración del demonio, no un socket de comunicación IPC.",
          "c": "`/dev/null` es el dispositivo de descarte de datos de UNIX.",
          "d": "`/opt/docker/socket.bin` no es la ruta estándar del socket."}),

        ("lab1-038", "¿Qué componente de bajo nivel es el encargado de interactuar directamente con el kernel de Linux para crear los namespaces y cgroups al arrancar un contenedor?",
         [("a", "runc"),
          ("b", "Docker Desktop UI"),
          ("c", "Docker Hub"),
          ("d", "Docker Compose")],
         ["a"], "hard", "single",
         "`runc` es la implementación de referencia de la OCI para el runtime de contenedores de bajo nivel que interactúa directamente con las APIs del kernel de Linux.",
         {"b": "Docker Desktop UI es una aplicación frontend gráfica para el usuario en Windows/macOS.",
          "c": "Docker Hub es un registro en la nube para alojar y compartir imágenes.",
          "d": "Docker Compose es una herramienta de orquestación de múltiples contenedores."}),

        ("lab1-039", "¿Qué función cumple 'containerd' en el ecosistema de Docker?",
         [("a", "Es un runtime de alto nivel que gestiona el ciclo de vida completo de los contenedores (transferencia de imágenes, ejecución mediante runc, almacenamiento y supervisión de red)."),
          ("b", "Es un navegador web integrado para visualizar aplicaciones frontend."),
          ("c", "Es un reemplazo de la memoria RAM del sistema operativo."),
          ("d", "Es el compilador de código fuente en C#.")],
         ["a"], "hard", "single",
         "`containerd` es un gestor de contenedores industrial diseñado para integrarse en sistemas como Docker y Kubernetes (a través de CRI).",
         {"b": "No contiene navegadores web ni interfaces visuales HTML.",
          "c": "No gestiona ni sustituye el hardware de memoria RAM.",
          "d": "No tiene funciones de compilación de código fuente .NET."}),

        ("lab1-040", "¿Qué proceso 'shim' (containerd-shim) se coloca entre containerd y runc para permitir que un contenedor siga corriendo aunque el demonio de Docker se reinicie?",
         [("a", "containerd-shim"),
          ("b", "hyperv-shim"),
          ("c", "systemd-shim"),
          ("d", "bash-wrapper")],
         ["a"], "hard", "single",
         "`containerd-shim` actúa como padre del proceso del contenedor, manteniendo abiertos los descriptores de archivo (stdin/stdout/stderr) y reportando el código de salida sin acoplarse permanentemente al demonio principal.",
         {"b": "hyperv-shim no forma parte de la arquitectura estándar OCI de containerd.",
          "c": "systemd-shim no gestiona el desacoplamiento de runc.",
          "d": "bash-wrapper no es el componente técnico de desacoplamiento de procesos en containerd."}),

        ("lab1-041", "¿Qué es un 'Docker Registry' (Registro de Docker)?",
         [("a", "Un servicio de almacenamiento y distribución de imágenes de Docker con soporte para etiquetado (tags) y control de versiones."),
          ("b", "El registro de claves de Windows (Regedit) donde se guardan las contraseñas de Docker."),
          ("c", "Una base de datos SQL donde se guardan los logs de cada contenedor."),
          ("d", "El archivo de configuración donde se definen las variables de entorno de .NET.")],
         ["a"], "easy", "single",
         "Un registro (como Docker Hub, GitHub Packages o Azure Container Registry) permite subir (`push`) y descargar (`pull`) imágenes de contenedores.",
         {"b": "No tiene ninguna relación con el registro de Windows (Windows Registry).",
          "c": "Los logs no se guardan en un Docker Registry.",
          "d": "Las variables de entorno de .NET residen en appsettings.json o en el entorno del proceso."}),

        ("lab1-042", "¿Cuál es el registro público predeterminado que utiliza Docker cuando se descarga una imagen sin especificar un prefijo de servidor?",
         [("a", "Docker Hub (docker.io)"),
          ("b", "Quay.io"),
          ("c", "Google Container Registry (gcr.io)"),
          ("d", "Microsoft Container Registry (mcr.microsoft.com)")],
         ["a"], "easy", "single",
         "Por defecto, referencias como `nginx:alpine` o `ubuntu:22.04` se resuelven automáticamente en Docker Hub (`registry-1.docker.io`).",
         {"b": "Quay.io es un registro gestionado por Red Hat que requiere prefijo explícito.",
          "c": "gcr.io es el registro de Google Cloud Platform.",
          "d": "mcr.microsoft.com aloja imágenes de Microsoft (como .NET y SQL Server) y requiere la ruta completa."}),

        ("lab1-043", "¿Cómo identifica Docker de forma criptográfica y unívoca cada capa de una imagen?",
         [("a", "Mediante un hash criptográfico SHA-256 basado en el contenido exacto de los archivos de la capa."),
          ("b", "Mediante la fecha y hora de compilación en formato UNIX timestamp."),
          ("c", "Mediante el número de puerto que expone el contenedor."),
          ("d", "Mediante el nombre de usuario de la cuenta de Windows.")],
         ["a"], "medium", "single",
         "Docker utiliza direccionamiento por contenido (content-addressable storage), calculando el digest sha256 del contenido comprimido de cada capa.",
         {"b": "La marca de tiempo no garantiza unicidad de contenido ni inmutabilidad criptográfica.",
          "c": "El puerto de red no tiene relación con el almacenamiento de archivos de la capa.",
          "d": "El nombre de usuario del anfitrión no influye en el identificador de capa."}),

        ("lab1-044", "¿Cuál es el controlador de almacenamiento (storage driver) predeterminado y recomendado actualmente en Docker para la mayoría de distribuciones Linux modernas?",
         [("a", "overlay2"),
          ("b", "aufs"),
          ("c", "vfs"),
          ("d", "devicemapper")],
         ["a"], "medium", "single",
         "`overlay2` es el controlador estándar altamente eficiente que aprovecha el soporte nativo de OverlayFS en el kernel de Linux para fusionar capas.",
         {"b": "aufs era un controlador histórico que ya no se utiliza ni se incluye en kernels modernos.",
          "c": "vfs no realiza Copy-on-Write y consume un espacio gigantesco al duplicar todo el árbol de directorios.",
          "d": "devicemapper está obsoleto en Docker moderno."}),

        ("lab1-045", "En la terminología de OverlayFS, ¿cómo se denominan respectivamente el directorio de las capas inferiores de la imagen y el directorio de cambios del contenedor?",
         [("a", "lowerdir (capas de solo lectura de la imagen) y upperdir (capa de lectura/escritura del contenedor)"),
          ("b", "readdir y writedir"),
          ("c", "cachedir y tempdir"),
          ("d", "hostdir y clientdir")],
         ["a"], "hard", "single",
         "OverlayFS fusiona uno o más `lowerdir` (las capas inmutables de la imagen) con un `upperdir` (la capa escribible del contenedor) presentándolos juntos en el `merged` dir.",
         {"b": "readdir y writedir son llamadas a funciones de biblioteca C, no términos de OverlayFS.",
          "c": "cachedir y tempdir son directorios convencionales de temporales.",
          "d": "hostdir y clientdir no son conceptos del sistema de archivos superpuesto."}),

        ("lab1-046", "¿Qué comando se utiliza para verificar la versión exacta del cliente de Docker, del demonio y del runtime subyacente?",
         [("a", "docker version"),
          ("b", "docker check"),
          ("c", "docker print"),
          ("d", "docker status")],
         ["a"], "easy", "single",
         "`docker version` imprime la versión detallada tanto del cliente como del servidor Docker Engine (incluyendo commit de git, versión de API y runc).",
         {"b": "'docker check' no es un comando existente en Docker CLI.",
          "c": "'docker print' no existe en Docker.",
          "d": "'docker status' no existe; para ver el estado se usa 'docker info' o 'docker stats'."}),

        ("lab1-047", "¿Qué comando permite inspeccionar la información global del sistema Docker, como la cantidad de contenedores totales, imágenes, controladores de red y memoria disponible?",
         [("a", "docker info"),
          ("b", "docker inspect --all"),
          ("c", "docker stats --system"),
          ("d", "docker system info-all")],
         ["a"], "easy", "single",
         "`docker info` despliega un resumen completo de la configuración y métricas globales del motor de Docker.",
         {"b": "'docker inspect' requiere especificar el nombre o ID de un objeto concreto.",
          "c": "'docker stats' monitoriza el uso de CPU y memoria de los contenedores en tiempo real.",
          "d": "'docker system info-all' no es una sintaxis válida de Docker."}),

        ("lab1-048", "¿Qué ocurre si el demonio `dockerd` se detiene o se bloquea mientras un usuario intenta ejecutar cualquier comando en la terminal?",
         [("a", "El comando fallará mostrando un error de conexión con el socket (por ejemplo: 'Cannot connect to the Docker daemon')."),
          ("b", "La terminal se formateará automáticamente."),
          ("c", "Docker ejecutará el contenedor usando PowerShell como servidor de emergencia."),
          ("d", "El comando se enviará a través de un SMS a los administradores.")],
         ["a"], "medium", "single",
         "El cliente de línea de comandos no puede ejecutar acciones por sí mismo; si el demonio no responde en el socket IPC, el comando aborta con error de conexión.",
         {"b": "La terminal no se formatea bajo ninguna circunstancia.",
          "c": "PowerShell es un intérprete de comandos, no un demonio OCI de reemplazo.",
          "d": "Docker no incluye pasarelas de mensajería SMS en su arquitectura básica."}),

        ("lab1-049", "Las etiquetas (tags) en Docker permiten diferenciar distintas versiones o variantes de una misma imagen (por ejemplo: `mcr.microsoft.com/dotnet/sdk:10.0` vs `sdk:8.0`).",
         [("a", "Verdadero"),
          ("b", "Falso")],
         ["a"], "easy", "truefalse",
         "Es Verdadero. La parte que sigue a los dos puntos (`:tag`) especifica la versión o variante de la imagen. Si no se especifica ninguna etiqueta, Docker asume por defecto `:latest`.",
         {"b": "Es incorrecto. Las etiquetas son precisamente el mecanismo estándar para versionar imágenes."}),

        ("lab1-050", "Si se ejecuta `docker run alpine` sin especificar una etiqueta, ¿qué etiqueta asume Docker automáticamente?",
         [("a", "latest"),
          ("b", "stable"),
          ("c", "default"),
          ("d", "main")],
         ["a"], "easy", "single",
         "La convención predeterminada de Docker en ausencia de etiqueta explícita es solicitar la etiqueta `latest`.",
         {"b": "'stable' es una etiqueta común en proyectos como Debian o Nginx, pero no es el valor por defecto de Docker.",
          "c": "'default' no es la etiqueta estándar en los registros de Docker.",
          "d": "'main' es el nombre habitual de la rama git principal, no el tag por defecto de Docker."}),

        ("lab1-051", "¿Por qué se desaconseja el uso de la etiqueta `:latest` en entornos de producción?",
         [("a", "Porque `:latest` es una etiqueta mutable que puede apuntar a versiones diferentes de la imagen con el tiempo, comprometiendo la reproducibilidad del despliegue."),
          ("b", "Porque Docker cobra una tarifa especial por el uso de la etiqueta latest."),
          ("c", "Porque las imágenes latest siempre se ejecutan en modo depuración (debug) consumiendo el triple de memoria."),
          ("d", "Porque los cortafuegos corporativos bloquean automáticamente la palabra latest.")],
         ["a"], "medium", "single",
         "Un nuevo `push` a un repositorio puede cambiar el contenido de `latest` sin aviso, provocando que dos servidores descarguen binarios distintos para la misma definición de despliegue.",
         {"b": "Docker Hub no cobra por nombres de etiquetas.",
          "c": "La etiqueta no altera la configuración de depuración interna del ejecutable.",
          "d": "Los cortafuegos no filtran el tráfico por el nombre de la etiqueta de la imagen."}),

        ("lab1-052", "¿Qué archivo se utiliza para configurar de forma persistente opciones del demonio Docker como la dirección de los registros inseguros o el directorio raíz de almacenamiento?",
         [("a", "/etc/docker/daemon.json"),
          ("b", "/etc/docker/docker.conf"),
          ("c", "~/.docker/config.json"),
          ("d", "/var/lib/docker/settings.xml")],
         ["a"], "medium", "single",
         "`/etc/docker/daemon.json` es el archivo de configuración centralizado en formato JSON para el demonio `dockerd` en Linux.",
         {"b": "'/etc/docker/docker.conf' no es el nombre estándar reconocido por dockerd.",
          "c": "'~/.docker/config.json' configura el cliente local de Docker (credenciales de login, plugins CLI), no el demonio.",
          "d": "Docker no utiliza archivos de configuración en formato XML."}),

        ("lab1-053", "¿Qué subdirectorio del sistema operativo almacena habitualmente por defecto todas las imágenes, capas de contenedores y volúmenes en Linux?",
         [("a", "/var/lib/docker"),
          ("b", "/etc/docker"),
          ("c", "/opt/docker/bin"),
          ("d", "/tmp/docker")],
         ["a"], "medium", "single",
         "La ubicación raíz estándar de almacenamiento del demonio de Docker es `/var/lib/docker` (donde residen las subcarpetas overlay2, volumes, containers, etc.).",
         {"b": "`/etc/docker` almacena archivos de configuración estáticos como daemon.json.",
          "c": "`/opt/docker/bin` no es el directorio de almacenamiento de datos del motor.",
          "d": "`/tmp` se borra en los reinicios del sistema, lo cual destruiría todas las imágenes y volúmenes."}),

        ("lab1-054", "¿Qué comando permite descargar una imagen desde un registro remoto sin ejecutar ningún contenedor?",
         [("a", "docker pull"),
          ("b", "docker fetch"),
          ("c", "docker clone"),
          ("d", "docker download")],
         ["a"], "easy", "single",
         "`docker pull <nombre-imagen>:<tag>` descarga las capas de la imagen desde el registro al almacenamiento local del host.",
         {"b": "'docker fetch' no es un comando de Docker CLI.",
          "c": "'docker clone' es propio de Git o hipervisores, no de Docker.",
          "d": "'docker download' no existe en Docker."}),

        ("lab1-055", "¿Qué comando permite enviar una imagen construida localmente hacia un registro remoto (como Docker Hub)?",
         [("a", "docker push"),
          ("b", "docker upload"),
          ("c", "docker send"),
          ("d", "docker commit")],
         ["a"], "easy", "single",
         "`docker push <nombre-imagen>:<tag>` sube las capas de la imagen hacia el repositorio especificado tras haberse autenticado.",
         {"b": "'docker upload' no existe en la sintaxis de Docker.",
          "c": "'docker send' no es un comando válido.",
          "d": "'docker commit' crea una imagen local a partir de los cambios en un contenedor, pero no la envía a un registro remoto."}),

        ("lab1-056", "¿Qué comando permite guardar una o más imágenes en un archivo comprimido .tar para moverlas a un entorno sin conexión a internet?",
         [("a", "docker save"),
          ("b", "docker export"),
          ("c", "docker zip"),
          ("d", "docker compress")],
         ["a"], "medium", "single",
         "`docker save -o archivo.tar imagen:tag` empaqueta la imagen completa con todas sus capas e historial en un archivo tar.",
         {"b": "'docker export' exporta el sistema de archivos plano de un contenedor, perdiendo las capas y metadatos de la imagen.",
          "c": "'docker zip' no existe en Docker.",
          "d": "'docker compress' no es un comando de Docker."}),

        ("lab1-057", "¿Qué comando permite restaurar una imagen a partir de un archivo .tar creado previamente con `docker save`?",
         [("a", "docker load"),
          ("b", "docker import"),
          ("c", "docker restore"),
          ("d", "docker unpack")],
         ["a"], "medium", "single",
         "`docker load -i archivo.tar` restaura la imagen con su historial de capas y etiquetas intactas.",
         {"b": "'docker import' se utiliza para importar un sistema de archivos plano creado con 'docker export', no con 'docker save'.",
          "c": "'docker restore' no es un comando de Docker CLI.",
          "d": "'docker unpack' no existe en la herramienta."}),

        ("lab1-058", "¿Cuál es la diferencia técnica entre `docker save` y `docker export`?",
         [("a", "`docker save` guarda una imagen con todas sus capas individuales e historial; `docker export` guarda el sistema de archivos plano de un contenedor sin capas intermedias ni metadatos."),
          ("b", "`docker save` solo comprime en ZIP y `docker export` solo en TAR."),
          ("c", "`docker save` elimina la imagen original del host tras guardarla."),
          ("d", "No hay diferencia; son comandos completamente idénticos.")],
         ["a"], "hard", "single",
         "`docker save` opera sobre imágenes preservando el árbol de capas y etiquetas. `docker export` aplana el estado del contenedor en un único tarball sin metadatos de Dockerfile (como ENTRYPOINT o ENV).",
         {"b": "Ambos formatos generan empaquetados tar estándar.",
          "c": "Ningún comando de exportación borra los datos de origen del disco.",
          "d": "La diferencia técnica en la estructura de capas resultante es sustancial."}),

        ("lab1-059", "¿Qué mecanismo utiliza Docker para verificar que una imagen descargada desde Docker Hub no ha sido alterada maliciosamente durante la transmisión?",
         [("a", "Docker Content Trust (DCT) y verificación de firmas criptográficas digitales con notario"),
          ("b", "Contraseñas por defecto en texto plano en el manifiesto"),
          ("c", "Comprobación del número de líneas del archivo README.md"),
          ("d", "Verificación mediante la dirección MAC del usuario")],
         ["a"], "hard", "single",
         "Docker Content Trust (DCT) utiliza claves públicas y privadas para firmar criptográficamente los manifiestos de las imágenes garantizando autenticidad e integridad.",
         {"b": "Las contraseñas en texto plano comprometen la seguridad en lugar de garantizar la integridad.",
          "c": "El archivo README no tiene validez criptográfica.",
          "d": "La dirección MAC no certifica la integridad del contenido transmitido."}),

        ("lab1-060", "¿Qué comando muestra el historial de creación y las capas que componen una imagen local?",
         [("a", "docker history"),
          ("b", "docker layers"),
          ("c", "docker tree"),
          ("d", "docker trace")],
         ["a"], "medium", "single",
         "`docker history <imagen>` enumera secuencialmente cada una de las capas que componen la imagen, el tamaño de cada una y la instrucción que la originó.",
         {"b": "'docker layers' no existe como subcomando en Docker.",
          "c": "'docker tree' no existe en Docker CLI.",
          "d": "'docker trace' no es un comando de Docker."}),

        ("lab1-061", "¿Cuál es la función del comando `docker tag`?",
         [("a", "Crea un nuevo alias o referencia a una imagen existente sin duplicar sus datos en disco."),
          ("b", "Borra las capas intermedias para reducir el tamaño de la imagen a la mitad."),
          ("c", "Añade una descripción de texto visible en Google Search."),
          ("d", "Cambia el puerto de escucha del contenedor en tiempo de ejecución.")],
         ["a"], "easy", "single",
         "`docker tag imagen_origen nuevo_nombre:nuevo_tag` asocia un nuevo nombre a la misma imagen identificada por su ID sha256.",
         {"b": "No altera el tamaño ni elimina capas.",
          "c": "No interactúa con motores de búsqueda en internet.",
          "d": "Los puertos se definen en el Dockerfile o en el comando `docker run`, no con tags."}),

        ("lab1-062", "¿Cómo se puede ejecutar un contenedor indicando que se elimine automáticamente cuando su proceso principal termine?",
         [("a", "docker run --rm"),
          ("b", "docker run --delete"),
          ("c", "docker run --cleanup"),
          ("d", "docker run --kill-after")],
         ["a"], "easy", "single",
         "El parámetro `--rm` indica a Docker Engine que limpie y destruya automáticamente la capa de contenedor cuando este finalice su ejecución.",
         {"b": "'--delete' no es un flag soportado por docker run.",
          "c": "'--cleanup' no existe en el comando docker run.",
          "d": "'--kill-after' no es una opción de docker run."}),

        ("lab1-063", "¿Qué combinación de parámetros en `docker run` permite interactuar con un shell dentro del contenedor manteniendo la entrada estándar abierta y asignando una pseudo-terminal (TTY)?",
         [("a", "-it (o -i -t)"),
          ("b", "-d"),
          ("c", "--detach --silent"),
          ("d", "-p -v")],
         ["a"], "easy", "single",
         "`-i` (interactive) mantiene STDIN abierto y `-t` (tty) asigna una pseudo-terminal para que el usuario pueda escribir comandos en la consola.",
         {"b": "`-d` ejecuta el contenedor en segundo plano (detached), sin terminal interactiva.",
          "c": "'--silent' no existe en docker run.",
          "d": "`-p` y `-v` configuran puertos y volúmenes, no la entrada interactiva de consola."}),

        ("lab1-064", "¿Qué hace el comando `docker run -d`?",
         [("a", "Ejecuta el contenedor en segundo plano (modo 'detached') imprimiendo el ID completo del contenedor en la consola."),
          ("b", "Ejecuta el contenedor en modo depuración (debugging) con puntos de interrupción activos."),
          ("c", "Borra el contenedor inmediatamente después de iniciarlo."),
          ("d", "Descarga la imagen sin arrancarla.")],
         ["a"], "easy", "single",
         "`-d` o `--detach` libera la terminal inmediatamente y permite que el proceso continúe ejecutándose como un proceso en segundo plano.",
         {"b": "No habilita modos de depuración interactiva de código.",
          "c": "Para eliminar tras terminar se usa `--rm`.",
          "d": "Para solo descargar sin arrancar se usa `docker pull`."}),

        ("lab1-065", "¿Qué comando permite adjuntar la terminal a un contenedor que ya se está ejecutando en segundo plano para ver su salida estándar en tiempo real?",
         [("a", "docker attach"),
          ("b", "docker connect"),
          ("c", "docker join"),
          ("d", "docker link")],
         ["a"], "medium", "single",
         "`docker attach <id-o-nombre>` conecta la terminal a la entrada/salida estándar del proceso principal de un contenedor en ejecución.",
         {"b": "'docker connect' no existe en Docker CLI; para redes se usa 'docker network connect'.",
          "c": "'docker join' no es un comando de gestión de contenedores.",
          "d": "'docker link' es una opción obsoleta de red de docker run."}),

        ("lab1-066", "¿Cuál es la diferencia entre `docker attach` y `docker exec`?",
         [("a", "`docker attach` se conecta al proceso principal existente (PID 1); `docker exec` inicia un nuevo proceso independiente dentro de los namespaces del contenedor en ejecución."),
          ("b", "`docker attach` solo sirve para ver logs y `docker exec` reinicia el servidor."),
          ("c", "`docker exec` solo funciona si el contenedor está detenido."),
          ("d", "No existe ninguna diferencia técnica entre ambos.")],
         ["a"], "hard", "single",
         "`docker exec` ejecuta un nuevo proceso separado (por ejemplo, `docker exec -it mi_app bash`) dentro del entorno existente del contenedor sin interrumpir el proceso principal.",
         {"b": "Para ver logs históricos se usa `docker logs`, no `docker attach`.",
          "c": "`docker exec` requiere obligatoriamente que el contenedor esté en estado 'running'.",
          "d": "Uno interactúa con el proceso ya existente mientras que el otro crea un proceso secundario."}),

        ("lab1-067", "¿Qué comando permite ejecutar una sesión interactiva de Bash dentro de un contenedor en ejecución llamado `mi-servidor`?",
         [("a", "docker exec -it mi-servidor bash"),
          ("b", "docker run -it mi-servidor bash"),
          ("c", "docker start mi-servidor bash"),
          ("d", "docker enter mi-servidor bash")],
         ["a"], "easy", "single",
         "`docker exec -it <nombre> <comando>` permite lanzar un nuevo shell (bash o sh) dentro de un contenedor en funcionamiento.",
         {"b": "'docker run' crearía un nuevo contenedor secundario a partir de la imagen, en vez de acceder al contenedor existente.",
          "c": "'docker start' solo arranca un contenedor previamente detenido y no recibe comandos arbitrarios de entrada.",
          "d": "'docker enter' no es un comando nativo de Docker CLI."}),

        ("lab1-068", "¿Qué comando permite detener de forma inmediata y forzosa un contenedor enviando la señal SIGKILL (código de salida 137)?",
         [("a", "docker kill"),
          ("b", "docker stop"),
          ("c", "docker pause"),
          ("d", "docker suspend")],
         ["a"], "easy", "single",
         "`docker kill` envía inmediatamente la señal SIGKILL (o la señal especificada con `--signal`), terminando el proceso sin esperar un apagado limpio.",
         {"b": "`docker stop` envía primero SIGTERM y espera un periodo de gracia (10 segundos por defecto) antes de enviar SIGKILL.",
          "c": "`docker pause` congela los procesos usando el freezer cgroup sin terminarlos.",
          "d": "`docker suspend` no existe en Docker CLI."}),

        ("lab1-069", "¿Cómo funciona el apagado limpio realizado por `docker stop <contenedor>`?",
         [("a", "Envía una señal SIGTERM al proceso principal (PID 1), espera un tiempo de gracia (10 segundos por defecto) para que guarde estado y finalice, y si no responde envía SIGKILL."),
          ("b", "Corta la alimentación eléctrica de la máquina de forma inmediata."),
          ("c", "Elimina los archivos del contenedor antes de matar los procesos."),
          ("d", "Suspende los hilos de ejecución en el disco duro permanentemente.")],
         ["a"], "medium", "single",
         "Este mecanismo permite que aplicaciones web, bases de datos y APIs cierren conexiones de red, completen transacciones y liberen recursos de forma ordenada.",
         {"b": "Docker no apaga la máquina anfitriona.",
          "c": "Los archivos permanecen almacenados en la capa del contenedor.",
          "d": "No realiza una hibernación de memoria a disco."}),

        ("lab1-070", "¿Qué comando permite suspender temporalmente la ejecución de todos los procesos dentro de un contenedor sin terminarlos utilizando el cgroup freezer?",
         [("a", "docker pause"),
          ("b", "docker sleep"),
          ("c", "docker freeze"),
          ("d", "docker halt")],
         ["a"], "medium", "single",
         "`docker pause <contenedor>` congela los procesos del contenedor inmediatamente; pueden reanudarse en el mismo punto exacto con `docker unpause`.",
         {"b": "'docker sleep' no es un comando de Docker CLI.",
          "c": "'docker freeze' no es el nombre del subcomando en la CLI (es 'pause').",
          "d": "'docker halt' no existe en Docker."})
    ]

    for item in vm_vs_c:
        qid, qtext, raw_opts, correct, diff, qtype, exp_c, exp_w = item
        options = [{"id": o[0], "text": o[1]} for o in raw_opts]
        # Determine topic
        topic = "Contenedores vs Máquinas Virtuales" if int(qid.split('-')[1]) <= 35 else "Arquitectura Docker Engine"
        questions.append({
            "id": qid,
            "lab": 1,
            "topic": topic,
            "difficulty": diff,
            "type": qtype,
            "question": qtext,
            "options": options,
            "correct": correct,
            "explanation": {
                "correct": exp_c,
                "wrong": exp_w
            },
            "source": "P1-Dockerización de Aplicaciones Modernas / Transparencias Práctica 1"
        })

    return questions

if __name__ == "__main__":
    q = get_questions()
    print(f"Lab 1 Part 1 loaded successfully: {len(q)} questions.")
