# scripts/generators/lab1_questions_part1.py
# -*- coding: utf-8 -*-
"""
Questions lab1-001 through lab1-130 for Lab 1.
Includes the 10 teacher questions verbatim, followed by in-depth questions on:
- Contenedores vs Máquinas Virtuales (kernel, overhead, density, startup, namespaces, cgroups)
- Arquitectura Docker Engine (dockerd, client, containerd, runc, Docker Hub, registries)
- Comandos CLI y Ciclo de Vida de Contenedores (run, ps, stop, kill, rm, pause, logs, stats, inspect, exec)
"""

def get_part1():
    q = []

    # -------------------------------------------------------------
    # TEACHER'S 10 QUESTIONS VERBATIM (lab1-001 to lab1-010)
    # -------------------------------------------------------------
    q.append({
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
                "c": "'DockerCompose' hace referencia a la herramienta de orquestación de múltiples contenedores (docker-compose.yml), no para compilar una sola imagen.",
                "d": "'DockeFile.txt' contiene una errata tipográfica y una extensión .txt no requerida ni admitida por convención en Docker."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 1"
    })

    q.append({
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

    q.append({
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
                "b": "'docker ls' no existe como comando global; se usa 'docker container ls' o 'docker ps'.",
                "c": "'docker ps -a' muestra todos los contenedores existentes, incluyendo los detenidos."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 3"
    })

    q.append({
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
                "d": "'docker kill' interrumpe forzosamente el contenedor enviando SIGKILL, pero preserva su existencia en disco."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 4"
    })

    q.append({
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
            "correct": "'docker logs' recopila e imprime las salidas stdout y stderr generadas por el proceso principal de un contenedor.",
            "wrong": {
                "a": "No borra archivos de log existentes en el demonio.",
                "b": "No genera entradas de log ficticias; muestra la salida emitida por la aplicación.",
                "c": "No transporta logs a servidores de logging remotos del host de manera directa."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 5"
    })

    q.append({
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
            "correct": "Es Falso. Los contenedores comparten el kernel del host y no necesitan una capa completa de SO invitado ni virtualización de hardware, lo que permite ejecutar una cantidad mucho mayor de contenedores que de máquinas virtuales.",
            "wrong": {
                "a": "Es incorrecto. Las máquinas virtuales requieren duplicar el kernel, la memoria dedicada y los servicios del sistema operativo, consumiendo muchísimos más recursos."
            }
        },
        "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 6"
    })

    q.append({
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

    q.append({
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

    q.append({
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

    q.append({
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

    # -------------------------------------------------------------
    # CONTENEDORES VS MÁQUINAS VIRTUALES (lab1-011 to lab1-040)
    # -------------------------------------------------------------
    q.append({
        "id": "lab1-011",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Cuál es la diferencia fundamental en la arquitectura de un contenedor frente a una máquina virtual?",
        "options": [
            {"id": "a", "text": "Los contenedores incluyen su propio kernel de sistema operativo independiente del host"},
            {"id": "b", "text": "Los contenedores comparten el kernel del sistema operativo host, mientras que cada VM ejecuta su propio SO invitado completo"},
            {"id": "c", "text": "Las máquinas virtuales no aíslan los procesos, mientras que los contenedores sí"},
            {"id": "d", "text": "Los contenedores solo pueden ejecutar código compilado en lenguaje C"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "A diferencia de las VMs (que virtualizan hardware y ejecutan un SO invitado completo con su propio kernel), los contenedores comparten el kernel del host y aíslan procesos en espacio de usuario.",
            "wrong": {
                "a": "Los contenedores no incluyen un kernel propio; utilizan el kernel del sistema anfitrión.",
                "c": "Las VMs aíslan fuertemente mediante hipervisores a nivel de hardware virtualizado.",
                "d": "Los contenedores pueden ejecutar cualquier lenguaje, binario o runtime compatible con la arquitectura del kernel."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 5-7 'Diferencia con las máquinas virtuales'"
    })

    q.append({
        "id": "lab1-012",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Cuáles son las tres características principales que definen a los contenedores según la teoría de la asignatura?",
        "options": [
            {"id": "a", "text": "Portabilidad, poca sobrecarga y aislamiento"},
            {"id": "b", "text": "Virtualización de BIOS, emulación de GPU y almacenamiento en cinta"},
            {"id": "c", "text": "Acceso root obligatorio, interfaz gráfica exclusiva y mono-hilo"},
            {"id": "d", "text": "Arranque lento, consumo intensivo de memoria y dependencia de hipervisor"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "El material docente destaca que un contenedor es un paquete de software independiente cuyas características clave son portabilidad, poca sobrecarga y aislamiento.",
            "wrong": {
                "b": "Los contenedores no virtualizan la BIOS ni emulan GPU por defecto como una máquina virtual.",
                "c": "No requieren interfaz gráfica (se suelen ejecutar como daemons o CLI) ni exigen ser mono-hilo.",
                "d": "Estas características describen las desventajas clásicas de la virtualización pesada de VMs, no de los contenedores."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 4 'Concepto de Contenedor'"
    })

    q.append({
        "id": "lab1-013",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué mecanismo del kernel de Linux utiliza Docker principalmente para limitar y monitorizar el consumo de recursos (CPU, memoria, I/O) de un contenedor?",
        "options": [
            {"id": "a", "text": "Namespaces (espacios de nombres)"},
            {"id": "b", "text": "Control Groups (cgroups)"},
            {"id": "c", "text": "Chroot jail"},
            {"id": "d", "text": "SELinux únicamente"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "Los 'cgroups' (Control Groups) del kernel se encargan de restringir, priorizar y medir los recursos de hardware (CPU, RAM, entrada/salida) asignados a cada contenedor.",
            "wrong": {
                "a": "Los namespaces proporcionan aislamiento de la vista del sistema (procesos, red, puntos de montaje), pero no controlan límites cuantitativos de CPU o RAM.",
                "c": "Chroot solo cambia el directorio raíz del proceso, sin capacidad de limitar uso de recursos.",
                "d": "SELinux es un módulo de seguridad basado en políticas de control de acceso obligatorio (MAC), no de contabilidad de recursos."
            }
        },
        "source": "P1-Dockerizacion_Aplicaciones_Modernas.pdf - Sección 2 'Fundamentos teóricos'"
    })

    q.append({
        "id": "lab1-014",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué tecnología del kernel de Linux proporciona el aislamiento de la tabla de procesos (PID), interfaces de red e identidades de usuario a los contenedores?",
        "options": [
            {"id": "a", "text": "Namespaces"},
            {"id": "b", "text": "Cgroups"},
            {"id": "c", "text": "Swap partitioning"},
            {"id": "d", "text": "Sysctl exclusivo"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "Los Namespaces aíslan las vistas de los subsistemas del sistema operativo: PID (procesos), NET (red), MNT (sistemas de archivos), IPC, UTS (nombre de máquina) y USER.",
            "wrong": {
                "b": "Cgroups limita el uso cuantitativo de recursos, no aísla las tablas ni la visibilidad del entorno.",
                "c": "Swap es el espacio de intercambio en disco cuando la memoria física se satura.",
                "d": "Sysctl es una interfaz para modificar parámetros del kernel en tiempo de ejecución."
            }
        },
        "source": "P1-Dockerizacion_Aplicaciones_Modernas.pdf - Sección 2 'Fundamentos teóricos'"
    })

    q.append({
        "id": "lab1-015",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Por qué el tiempo de arranque de un contenedor es sustancialmente menor que el de una máquina virtual?",
        "options": [
            {"id": "a", "text": "Porque el contenedor comprime el código antes de cargarlo en RAM"},
            {"id": "b", "text": "Porque el contenedor solo inicia un proceso en el kernel ya en ejecución del host, sin arrancar un SO completo"},
            {"id": "c", "text": "Porque los contenedores se ejecutan exclusivamente en la memoria caché del procesador"},
            {"id": "d", "text": "Porque las máquinas virtuales no utilizan discos duros SSD"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "Arrancar un contenedor equivale a lanzar un proceso estándar aislado sobre el kernel que ya está corriendo en el host, mientras que una VM requiere inicializar hardware virtual, BIOS, kernel y servicios del SO invitado.",
            "wrong": {
                "a": "El arranque no depende de compresión en tiempo real del código.",
                "c": "Los contenedores residen en la memoria principal (RAM) como cualquier proceso ordinario.",
                "d": "El tipo de almacenamiento físico no elimina la sobrecarga intrínseca de arrancar un kernel invitado completo en una VM."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 7 'Ventajas de los contenedores'"
    })

    q.append({
        "id": "lab1-016",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "truefalse",
        "question": "Tanto las máquinas virtuales como los contenedores proporcionan mecanismos de aislamiento de recursos.",
        "options": [
            {"id": "a", "text": "Verdadero"},
            {"id": "b", "text": "Falso"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "Es Verdadero. Las diapositivas indican explícitamente: 'Ambas ofrecen: Aislamiento de recursos', aunque las VMs lo hacen a nivel de hardware/hipervisor y los contenedores a nivel de kernel/espacio de usuario.",
            "wrong": {
                "b": "Es falso afirmar que no lo ofrecen; el aislamiento de recursos es un requisito indispensable en ambas tecnologías."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 7"
    })

    q.append({
        "id": "lab1-017",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué término describe la capacidad de empaquetar una aplicación con sus librerías para que funcione idénticamente en cualquier entorno (desarrollo, pruebas, producción)?",
        "options": [
            {"id": "a", "text": "Escalabilidad elástica"},
            {"id": "b", "text": "Portabilidad"},
            {"id": "c", "text": "Tolerancia a particiones bizantinas"},
            {"id": "d", "text": "Consistencia eventual"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "La portabilidad es la propiedad que garantiza que la imagen del contenedor se ejecute de la misma manera en cualquier máquina o sistema operativo con Docker instalado.",
            "wrong": {
                "a": "La escalabilidad elástica se refiere a la capacidad de variar el número de instancias según la carga.",
                "c": "La tolerancia a fallos bizantinos es un algoritmo de consenso distribuido ante nodos maliciosos.",
                "d": "La consistencia eventual es un modelo de datos en almacenamiento distribuido."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 4 'Concepto'"
    })

    q.append({
        "id": "lab1-018",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "hard",
        "type": "single",
        "question": "Si ejecutas un contenedor de Ubuntu en un host con Linux Fedora, ¿qué kernel ejecuta el código del contenedor?",
        "options": [
            {"id": "a", "text": "El kernel de Ubuntu emulado mediante QEMU"},
            {"id": "b", "text": "El kernel de Linux instalado en el host Fedora"},
            {"id": "c", "text": "Un kernel híbrido compilado en tiempo de arranque del contenedor"},
            {"id": "d", "text": "Docker Engine no permite ejecutar imágenes de Ubuntu sobre un host Fedora"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "En los contenedores no existe kernel invitado: todos los contenedores Linux comparten las llamadas al sistema del único kernel activo del host (en este caso, el de Fedora).",
            "wrong": {
                "a": "No se emula un kernel mediante QEMU en contenedores estándar; la imagen de Ubuntu solo aporta los binarios y librerías en espacio de usuario.",
                "c": "No existe ningún kernel híbrido temporal.",
                "d": "Cualquier distribución Linux basada en el estándar ELF puede ejecutarse en cualquier host Linux mediante contenedores."
            }
        },
        "source": "P1-Dockerizacion_Aplicaciones_Modernas.pdf - Sección 2"
    })

    q.append({
        "id": "lab1-019",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Por qué los contenedores ofrecen mayor 'densidad' de despliegue por máquina que las máquinas virtuales?",
        "options": [
            {"id": "a", "text": "Porque las imágenes de contenedor se comprimen con algoritmos zip en memoria"},
            {"id": "b", "text": "Porque al compartir una capa base común y no requerir memoria dedicada para un SO completo por instancia, ocupan una fracción de recursos"},
            {"id": "c", "text": "Porque los contenedores se ejecutan sin memoria RAM física, usando solo el disco duro"},
            {"id": "d", "text": "Porque los contenedores eliminan el protocolo TCP/IP"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "Al prescindir de la sobrecarga de un SO invitado dedicado por instancia y compartir capas inmutables, un mismo servidor físico puede alojar órdenes de magnitud más contenedores que máquinas virtuales.",
            "wrong": {
                "a": "No se comprimen con zip en la memoria RAM en ejecución.",
                "c": "Todo contenedor activo requiere memoria RAM física asignada.",
                "d": "Los contenedores hacen uso estándar de la pila de protocolos de red TCP/IP."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 7"
    })

    q.append({
        "id": "lab1-020",
        "lab": 1,
        "topic": "Contenedores vs Máquinas Virtuales",
        "difficulty": "medium",
        "type": "truefalse",
        "question": "En un contenedor, si se produce un fallo catastrófico (kernel panic) en el kernel del host, todos los contenedores de ese host caen inmediatamente.",
        "options": [
            {"id": "a", "text": "Verdadero"},
            {"id": "b", "text": "Falso"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "Es Verdadero. Dado que todos los contenedores comparten el mismo kernel del anfitrión, un pánico o corrupción del kernel del host derrumba todo el sistema y todos los contenedores en ejecución.",
            "wrong": {
                "b": "Es falso pensar que un contenedor sobrevive al fallo del único kernel sobre el cual se ejecutan sus procesos."
            }
        },
        "source": "P1-Dockerizacion_Aplicaciones_Modernas.pdf - Sección 2"
    })

    # -------------------------------------------------------------
    # ARQUITECTURA DOCKER ENGINE Y COMPONENTES (lab1-021 to lab1-045)
    # -------------------------------------------------------------
    q.append({
        "id": "lab1-021",
        "lab": 1,
        "topic": "Arquitectura Docker Engine y Componentes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Cuáles son los tres componentes fundamentales que conforman la arquitectura de Docker?",
        "options": [
            {"id": "a", "text": "Docker Engine, Docker Client y Docker Registry"},
            {"id": "b", "text": "Docker BIOS, Docker RAM y Docker Kernel"},
            {"id": "c", "text": "Docker Hypervisor, Docker VMWare y Docker VirtualBox"},
            {"id": "d", "text": "Docker Frontend, Docker Backend y Docker Database"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "La arquitectura descrita en el temario se compone de: Docker Engine (demonio/motor), Docker Client (herramienta de línea de comandos CLI) y Docker Registry (registro de almacenamiento de imágenes).",
            "wrong": {
                "b": "Docker no define componentes de BIOS ni tiene un kernel propietario.",
                "c": "Hypervisor y VMWare/VirtualBox pertenecen al ecosistema de máquinas virtuales tradicionales.",
                "d": "Esos términos representan capas habituales de aplicaciones web, no los componentes del sistema Docker."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 10 'Componentes de Docker'"
    })

    q.append({
        "id": "lab1-022",
        "lab": 1,
        "topic": "Arquitectura Docker Engine y Componentes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué componente de Docker es el responsable directo de crear, gestionar y ejecutar los contenedores?",
        "options": [
            {"id": "a", "text": "Docker Client"},
            {"id": "b", "text": "Docker Engine"},
            {"id": "c", "text": "Docker Hub"},
            {"id": "d", "text": "Docker Registry"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "El Docker Engine es el demonio que constituye el corazón de Docker, encargado de administrar el ciclo de vida real de los contenedores, redes y volúmenes.",
            "wrong": {
                "a": "Docker Client es únicamente la interfaz CLI que envía órdenes al Docker Engine.",
                "c": "Docker Hub es el servicio de registro público en la nube para alojar y compartir imágenes.",
                "d": "Docker Registry es el repositorio pasivo donde se almacenan las imágenes empaquetadas."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 10"
    })

    q.append({
        "id": "lab1-023",
        "lab": 1,
        "topic": "Arquitectura Docker Engine y Componentes",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Cómo se comunican el cliente de Docker (CLI) y el Docker Engine cuando se ejecutan en la misma máquina local?",
        "options": [
            {"id": "a", "text": "A través de señales de humo digitales sobre UDP"},
            {"id": "b", "text": "Mediante una API REST que viaja sobre un socket Unix local (/var/run/docker.sock) o Named Pipe en Windows"},
            {"id": "c", "text": "Invocando llamadas RPC mediante gRPC sobre el puerto 5000 exclusivamente"},
            {"id": "d", "text": "Modificando directamente el código fuente del kernel de Linux en memoria"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "El cliente de Docker y el demonio se comunican a través de una API REST HTTP utilizando un socket Unix local (/var/run/docker.sock en Linux/macOS) o una canalización con nombre (Named Pipe) en Windows.",
            "wrong": {
                "a": "Respuesta no técnica.",
                "c": "La comunicación principal de Docker Engine API es HTTP/REST, no gRPC sobre el puerto 5000 (el puerto 5000 es el del servidor de la Práctica 2).",
                "d": "El cliente de Docker es un programa en espacio de usuario y no modifica el código del kernel."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 10-11"
    })

    q.append({
        "id": "lab1-024",
        "lab": 1,
        "topic": "Arquitectura Docker Engine y Componentes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Cuál es el registro público oficial por defecto utilizado por Docker para descargar imágenes cuando no se especifica ningún servidor?",
        "options": [
            {"id": "a", "text": "GitHub Packages"},
            {"id": "b", "text": "Docker Hub"},
            {"id": "c", "text": "Google Container Registry"},
            {"id": "d", "text": "Quay.io"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "Docker Hub (hub.docker.com) es el Docker Registry predeterminado configurado en el cliente para resolver y descargar imágenes públicas.",
            "wrong": {
                "a": "GitHub Packages es un registro alternativo de terceros (ghcr.io).",
                "c": "Google Container Registry (gcr.io / artifact registry) es el servicio de nube de Google.",
                "d": "Quay.io es un registro gestionado por Red Hat."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 10"
    })

    q.append({
        "id": "lab1-025",
        "lab": 1,
        "topic": "Arquitectura Docker Engine y Componentes",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué comando se utiliza para verificar la versión instalada y comprobar que Docker Engine está respondiendo?",
        "options": [
            {"id": "a", "text": "docker version"},
            {"id": "b", "text": "dotnet --version"},
            {"id": "c", "text": "docker check-health"},
            {"id": "d", "text": "docker ping"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "'docker version' muestra los detalles tanto del cliente CLI como del servidor Docker Engine, confirmando la comunicación entre ambos.",
            "wrong": {
                "b": "'dotnet --version' comprueba la versión del SDK de .NET, no el estado del motor de Docker.",
                "c": "'docker check-health' no es un comando de la CLI de Docker.",
                "d": "'docker ping' no existe como comando en el CLI."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 12 'Verificar instalación de Docker'"
    })

    # -------------------------------------------------------------
    # CICLO DE VIDA Y COMANDOS CLI DE CONTENEDORES (lab1-026 to lab1-070)
    # -------------------------------------------------------------
    q.append({
        "id": "lab1-026",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué hace el parámetro \"-d\" al ejecutar \"docker run -d <imagen>\"?",
        "options": [
            {"id": "a", "text": "Ejecuta el contenedor en modo depuración interactiva"},
            {"id": "b", "text": "Ejecuta el contenedor en segundo plano (detached mode) e imprime el ID del contenedor"},
            {"id": "c", "text": "Destruye la imagen después de 10 segundos"},
            {"id": "d", "text": "Descarga la imagen sin arrancarla"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "El modificador '-d' o '--detach' ejecuta el contenedor en segundo plano, liberando la consola del usuario e imprimiendo el identificador único del contenedor.",
            "wrong": {
                "a": "El modo depuración no se activa con -d; para interactuar se usa '-it'.",
                "c": "No destruye la imagen; los contenedores y sus imágenes persisten en disco.",
                "d": "Descargar sin arrancar se realiza mediante 'docker pull'."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 27 'docker run -p 8080:80 -d nginx'"
    })

    q.append({
        "id": "lab1-027",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué combinación de parámetros permite abrir una sesión de terminal interactiva con una consola bash dentro de un contenedor Ubuntu recién arrancado?",
        "options": [
            {"id": "a", "text": "docker run -it ubuntu"},
            {"id": "b", "text": "docker run -d ubuntu"},
            {"id": "c", "text": "docker start ubuntu bash"},
            {"id": "d", "text": "docker inspect -t ubuntu"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "La combinación '-it' (-i para mantener abierto STDIN y -t para asignar una pseudo-terminal TTY) permite interactuar con la consola del contenedor.",
            "wrong": {
                "b": "'-d' enviaría el contenedor a segundo plano, saliendo de inmediato si no hay un proceso en primer plano.",
                "c": "'docker start' arranca contenedores previamente creados, pero no acepta imágenes directamente con esa sintaxis.",
                "d": "'docker inspect' muestra metadatos JSON de configuración, no abre sesiones interactivas."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 12 'Contenedor interactivo de ubuntu: docker run -it ubuntu'"
    })

    q.append({
        "id": "lab1-028",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué función cumple el parámetro \"--rm\" en \"docker run --rm <imagen>\"?",
        "options": [
            {"id": "a", "text": "Elimina la imagen descargada del disco cuando el contenedor finaliza"},
            {"id": "b", "text": "Elimina automáticamente el contenedor del sistema una vez que este se detiene"},
            {"id": "c", "text": "Reinicia el contenedor de manera indefinida ante cualquier error"},
            {"id": "d", "text": "Elimina la red virtual predeterminada de Docker"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "'--rm' le indica a Docker que elimine automáticamente el contenedor y su sistema de archivos efímero cuando su proceso principal termine.",
            "wrong": {
                "a": "No borra la imagen base utilizada, solo la instancia de contenedor que se ejecutó.",
                "c": "El reinicio indefinido se configura con '--restart always'.",
                "d": "No modifica las redes del demonio de Docker."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 13 'docker run --name <nombre> --rm -t -i <imagen>'"
    })

    q.append({
        "id": "lab1-029",
        "lab": 1,
        "topic": "Ciclo de Vida de Contenedores",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Cuál es la diferencia principal entre los comandos \"docker stop\" y \"docker kill\"?",
        "options": [
            {"id": "a", "text": "\"docker stop\" borra el contenedor, mientras que \"docker kill\" solo pausa los hilos"},
            {"id": "b", "text": "\"docker stop\" envía una señal SIGTERM para permitir una parada ordenada (con timeout de 10s antes de SIGKILL), mientras que \"docker kill\" envía SIGKILL de inmediato"},
            {"id": "c", "text": "\"docker kill\" apaga el host físico completo"},
            {"id": "d", "text": "No existe ninguna diferencia; son sinónimos exactos en el código de Docker"}
        ],
        "correct": ["b"],
        "explanation": {
            "correct": "'docker stop' permite una finalización ordenada enviando SIGTERM al proceso y esperando un periodo de gracia (por defecto 10s); si no termina, envía SIGKILL. 'docker kill' envía la señal forzosa SIGKILL de forma instantánea.",
            "wrong": {
                "a": "Ninguno de los dos comandos borra el contenedor del disco.",
                "c": "Solo interactúan con el proceso del contenedor objetivo, no con la máquina anfitriona.",
                "d": "Tienen comportamientos muy diferenciados en el manejo de señales POSIX."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositivas 15-16 'Parada de contenedores'"
    })

    q.append({
        "id": "lab1-030",
        "lab": 1,
        "topic": "Ciclo de Vida de Contenedores",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué comando permite detener de forma forzosa Y borrar en un único paso un contenedor que se encuentra actualmente en ejecución?",
        "options": [
            {"id": "a", "text": "docker rm -f <id-contenedor>"},
            {"id": "b", "text": "docker delete --now <id-contenedor>"},
            {"id": "c", "text": "docker kill --purge <id-contenedor>"},
            {"id": "d", "text": "docker stop -d <id-contenedor>"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "El parámetro '-f' (--force) en 'docker rm' envía un SIGKILL al contenedor si está corriendo y a continuación lo elimina del sistema.",
            "wrong": {
                "b": "'docker delete' no existe en la interfaz de línea de comandos de Docker.",
                "c": "'docker kill' no dispone de un flag '--purge' para borrar contenedores.",
                "d": "'docker stop' no acepta un flag '-d' y no borra el contenedor."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 15 'docker rm -f <id-contenedor>'"
    })

    q.append({
        "id": "lab1-031",
        "lab": 1,
        "topic": "Ciclo de Vida de Contenedores",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué comando se utiliza para suspender temporalmente la ejecución de todos los procesos de un contenedor sin detenerlo por completo?",
        "options": [
            {"id": "a", "text": "docker pause <id-contenedor>"},
            {"id": "b", "text": "docker sleep <id-contenedor>"},
            {"id": "c", "text": "docker freeze <id-contenedor>"},
            {"id": "d", "text": "docker suspend <id-contenedor>"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "'docker pause' suspende todos los procesos del contenedor utilizando el subsistema cgroups freezer. Para reanudarlos se emplea 'docker unpause'.",
            "wrong": {
                "b": "'docker sleep' no es un comando de Docker CLI.",
                "c": "Aunque use el subsistema freezer del kernel, el comando oficial de Docker es 'pause'.",
                "d": "'docker suspend' no existe en Docker."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 18 'Pausa, inspección y estadísticas'"
    })

    q.append({
        "id": "lab1-032",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué comando muestra en tiempo real estadísticas de consumo de CPU, memoria, red y disco de los contenedores activos?",
        "options": [
            {"id": "a", "text": "docker stats"},
            {"id": "b", "text": "docker top"},
            {"id": "c", "text": "docker monitor"},
            {"id": "d", "text": "docker usage"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "'docker stats' proporciona una transmisión en directo con las métricas de uso de recursos (CPU %, Memoria utilizada/límite, E/S de red y disco) de los contenedores en ejecución.",
            "wrong": {
                "b": "'docker top' lista los procesos activos dentro de un contenedor concreto, pero no estadísticas de consumo continuas.",
                "c": "'docker monitor' no es un comando de Docker.",
                "d": "'docker usage' no existe en el catálogo de comandos de Docker."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 18 'docker stats <id-contenedor>'"
    })

    q.append({
        "id": "lab1-033",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué comando permite ejecutar un comando adicional (por ejemplo, abrir una nueva sesión interactiva de bash) dentro de un contenedor que YA está en ejecución?",
        "options": [
            {"id": "a", "text": "docker exec -it <id-contenedor> /bin/bash"},
            {"id": "b", "text": "docker run -it <id-contenedor> /bin/bash"},
            {"id": "c", "text": "docker start -it <id-contenedor> /bin/bash"},
            {"id": "d", "text": "docker attach --create <id-contenedor>"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "'docker exec' ejecuta un nuevo proceso dentro del entorno aislado de un contenedor que ya se encuentra activo.",
            "wrong": {
                "b": "'docker run' crearía un contenedor completamente NUEVO a partir de una imagen, no entraría en el existente.",
                "c": "'docker start' reinicia contenedores detenidos, no inyecta nuevos comandos interactivos en uno ya activo.",
                "d": "'docker attach' conecta la terminal a la salida estándar del proceso primario existente, no crea un proceso secundario bash."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 13"
    })

    q.append({
        "id": "lab1-034",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "easy",
        "type": "single",
        "question": "¿Qué parámetro del comando \"docker logs\" permite seguir la salida de los registros en tiempo real a medida que se generan (similar a tail -f)?",
        "options": [
            {"id": "a", "text": "-f (o --follow)"},
            {"id": "b", "text": "-r (o --realtime)"},
            {"id": "c", "text": "-c (o --continuous)"},
            {"id": "d", "text": "-w (o --watch)"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "El parámetro '-f' o '--follow' mantiene abierta la conexión e imprime en pantalla cualquier nueva línea emitida por el proceso del contenedor.",
            "wrong": {
                "b": "'--realtime' no es una opción válida de 'docker logs'.",
                "c": "'-c' no es el indicador de seguimiento de salida.",
                "d": "'-w' no existe en este comando; se utiliza la opción estándar de Unix '-f'."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 18"
    })

    q.append({
        "id": "lab1-035",
        "lab": 1,
        "topic": "Comandos Docker CLI",
        "difficulty": "medium",
        "type": "single",
        "question": "¿Qué comando inspecciona todos los detalles de configuración en formato JSON (como IP asignada, volúmenes montados, variables de entorno y estado) de un contenedor?",
        "options": [
            {"id": "a", "text": "docker inspect <id-contenedor>"},
            {"id": "b", "text": "docker detail <id-contenedor>"},
            {"id": "c", "text": "docker config view <id-contenedor>"},
            {"id": "d", "text": "docker show <id-contenedor>"}
        ],
        "correct": ["a"],
        "explanation": {
            "correct": "'docker inspect' devuelve una estructura JSON detallada con la configuración interna completa de cualquier objeto de Docker (contenedor, imagen, volumen o red).",
            "wrong": {
                "b": "'docker detail' no es un comando existente.",
                "c": "'docker config' se utiliza en modo Docker Swarm para configuraciones no secretas, no para ver el estado de un contenedor.",
                "d": "'docker show' no existe en Docker CLI."
            }
        },
        "source": "Practica1-SSDD_DockerParte1.pdf - Diapositiva 18"
    })

    return q

if __name__ == '__main__':
    qs = get_part1()
    print("Part 1 questions loaded:", len(qs))
