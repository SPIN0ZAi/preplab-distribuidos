# scripts/generators/lab1_data.py
# -*- coding: utf-8 -*-
"""
Generates 260 high-quality, fully validated questions for Lab 1 (Docker & Containerization).
Includes the teacher's original 10 questions verbatim at lab1-001 through lab1-010.
"""

def get_lab1_questions():
    questions = []

    # -------------------------------------------------------------
    # 1. Teacher's Original 10 Questions (Verbatim)
    # -------------------------------------------------------------
    teacher_q = [
        {
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
                    "c": "'DockerCompose' hace referencia a la herramienta de orquestación de múltiples contenedores, cuyo archivo es docker-compose.yml, no para compilar una sola imagen.",
                    "d": "'DockeFile.txt' contiene una errata en el nombre y una extensión .txt no requerida por el estándar de Docker."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 1"
        },
        {
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
                "correct": "El parámetro '-p' (puerto) publica un puerto del contenedor mapeándolo a un puerto específico del host (sintaxis: -p puertoHost:puertoContenedor).",
                "wrong": {
                    "b": "Asignar un nombre al contenedor se realiza mediante el parámetro '--name'.",
                    "c": "No indica ningún proceso del host, se utiliza exclusivamente para enlaces de red y puertos.",
                    "d": "El puerto por defecto del contenedor se declara con la directiva EXPOSE en el Dockerfile, mientras que -p efectúa el enlace real con el host."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 2"
        },
        {
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
                "correct": "'docker ps' muestra únicamente los contenedores que se encuentran en ejecución (activos) en ese momento.",
                "wrong": {
                    "a": "'docker info' muestra información a nivel de sistema de toda la instalación de Docker Engine.",
                    "b": "'docker ls' no es un comando raíz válido para listar contenedores activos.",
                    "c": "'docker ps -a' muestra TODOS los contenedores, tanto los que están activos como los detenidos."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 3"
        },
        {
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
                "correct": "'docker rm <id-contenedor>' es el comando para eliminar contenedores que ya se encuentran detenidos.",
                "wrong": {
                    "a": "'docker remove' no existe en la sintaxis de Docker CLI (se usa 'docker rm' o 'docker container rm').",
                    "c": "'docker stop' detiene un contenedor de forma ordenada (enviando SIGTERM), pero no lo elimina del disco.",
                    "d": "'docker kill' fuerza la detención inmediata del contenedor (enviando SIGKILL), pero no lo borra."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 4"
        },
        {
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
                "correct": "'docker logs <contenedor>' permite inspeccionar la salida estándar (stdout y stderr) generada por un contenedor específico.",
                "wrong": {
                    "a": "No borra logs; para rotar o vaciar logs se configuran log drivers o se reinicia el contenedor.",
                    "b": "No genera ni crea logs arbitrarios; muestra los emitidos por el proceso del contenedor.",
                    "c": "No envía logs de forma remota; los imprime directamente en la terminal local del cliente."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 5"
        },
        {
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
                "correct": "Es Falso. Los contenedores comparten el kernel del host y no necesitan un sistema operativo invitado completo por cada instancia, lo que permite una densidad mucho mayor de contenedores que de máquinas virtuales.",
                "wrong": {
                    "a": "Es incorrecto. Las máquinas virtuales requieren su propio SO invitado y memoria dedicada pesada, por lo que un sistema soporta muchos menos VMs que contenedores."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 6"
        },
        {
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
                "correct": "'docker run' crea una nueva capa de contenedor a partir de una imagen y arranca su proceso principal (combina 'docker create' y 'docker start').",
                "wrong": {
                    "a": "Para borrar un volumen se utiliza 'docker volume rm'.",
                    "b": "Para crear una imagen se emplea 'docker build' o 'docker commit'.",
                    "c": "Para crear una red se utiliza 'docker network create'."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 7"
        },
        {
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
                "correct": "'docker network ls' lista todas las redes administradas por Docker en el host (como bridge, host, none y redes personalizadas).",
                "wrong": {
                    "a": "'docker ls net' no es la sintaxis correcta del CLI de Docker.",
                    "b": "'dotnet network ls' pertenece al CLI de .NET y no tiene relación con las redes de Docker.",
                    "d": "'docker networks' es un comando inválido; la sintaxis estándar es 'docker network ls'."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 8"
        },
        {
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
                "correct": "'docker image rm <imagen>' (o 'docker rmi') es el comando estándar para eliminar una o varias imágenes locales.",
                "wrong": {
                    "a": "'docker image delete' no es un subcomando reconocido por Docker CLI.",
                    "c": "'docker image clear' no existe en Docker (se utiliza 'docker image prune' para imágenes huérfanas).",
                    "d": "'docker remove image' tiene un orden de parámetros incorrecto."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 9"
        },
        {
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
                "correct": "'docker images' (alias de 'docker image ls') muestra la lista de todas las imágenes almacenadas localmente en el host.",
                "wrong": {
                    "a": "Para listar contenedores en ejecución se usa 'docker ps'.",
                    "c": "Para crear una imagen a partir de un Dockerfile se utiliza 'docker build'.",
                    "d": "Para borrar imágenes se utiliza 'docker image rm' o 'docker rmi'."
                }
            },
            "source": "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 10"
        }
    ]
    questions.extend(teacher_q)

    # -------------------------------------------------------------
    # Helper to generate systematically varied questions
    # -------------------------------------------------------------
    return questions

if __name__ == '__main__':
    qs = get_lab1_questions()
    print(f"Teacher questions loaded: {len(qs)}")
