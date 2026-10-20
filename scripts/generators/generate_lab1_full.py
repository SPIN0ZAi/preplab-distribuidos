# scripts/generators/generate_lab1_full.py
# -*- coding: utf-8 -*-
import json
import os

def build_lab1():
    q = []

    # 1. Teacher questions (lab1-001 to lab1-010)
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
                "d": "'DockeFile.txt' contiene una errata tipográfica y una extensión .txt no admitida por convención en Docker."
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

    return q

if __name__ == '__main__':
    qs = build_lab1()
    print("Teacher count:", len(qs))
