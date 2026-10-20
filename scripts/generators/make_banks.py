# scripts/generators/make_banks.py
# -*- coding: utf-8 -*-
"""
Generates 260 questions for Lab 1 and 260 questions for Lab 2.
Total = 520 questions.
Writes to src/data/lab1.json and src/data/lab2.json.
"""
import json
import os
import sys

def build_data():
    lab1 = []
    lab2 = []
    seen1 = set()
    seen2 = set()

    def add1(qid, topic, diff, qtype, qtext, options, correct, exp_c, exp_w, src):
        norm = qtext.strip().lower()
        if norm in seen1:
            raise ValueError(f"Duplicate question text in Lab 1: {qtext}")
        seen1.add(norm)
        opt_ids = [o["id"] for o in options]
        for c in correct:
            if c not in opt_ids:
                raise ValueError(f"Correct {c} not in {opt_ids} for {qid}")
        for opt_id in opt_ids:
            if opt_id not in correct and opt_id not in exp_w:
                raise ValueError(f"Missing wrong explanation for {opt_id} in {qid}")
        lab1.append({
            "id": qid,
            "lab": 1,
            "topic": topic,
            "difficulty": diff,
            "type": qtype,
            "question": qtext,
            "options": options,
            "correct": correct,
            "explanation": {"correct": exp_c, "wrong": exp_w},
            "source": src
        })

    def add2(qid, topic, diff, qtype, qtext, options, correct, exp_c, exp_w, src):
        norm = qtext.strip().lower()
        if norm in seen2:
            raise ValueError(f"Duplicate question text in Lab 2: {qtext}")
        seen2.add(norm)
        opt_ids = [o["id"] for o in options]
        for c in correct:
            if c not in opt_ids:
                raise ValueError(f"Correct {c} not in {opt_ids} for {qid}")
        for opt_id in opt_ids:
            if opt_id not in correct and opt_id not in exp_w:
                raise ValueError(f"Missing wrong explanation for {opt_id} in {qid}")
        lab2.append({
            "id": qid,
            "lab": 2,
            "topic": topic,
            "difficulty": diff,
            "type": qtype,
            "question": qtext,
            "options": options,
            "correct": correct,
            "explanation": {"correct": exp_c, "wrong": exp_w},
            "source": src
        })

    # =========================================================================
    # LAB 1: TEACHER'S 10 ORIGINAL QUESTIONS (lab1-001 to lab1-010)
    # =========================================================================
    add1("lab1-001", "Dockerfile e Imágenes", "easy", "single",
        "¿Qué archivo se usa para construir imágenes personalizadas en Docker?",
        [{"id": "a", "text": "docker-config"}, {"id": "b", "text": "Dockerfile"}, {"id": "c", "text": "DockerCompose"}, {"id": "d", "text": "DockeFile.txt"}],
        ["b"],
        "El archivo estándar reconocido por el motor de Docker para definir los pasos de construcción de una imagen es 'Dockerfile' (sin extensión).",
        {"a": "'docker-config' no es el nombre estándar del archivo de construcción en Docker.", "c": "'DockerCompose' es para orquestación de múltiples contenedores.", "d": "'DockeFile.txt' contiene una errata tipográfica y una extensión innecesaria."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 1")

    add1("lab1-002", "Redes y Mapeo de Puertos", "easy", "single",
        "¿Qué hace el parámetro \"-p\" en el comando \"docker run\"?",
        [{"id": "a", "text": "Mapea puertos del host al contenedor"}, {"id": "b", "text": "Asigna un nombre al contenedor"}, {"id": "c", "text": "Indica el proceso en el host"}, {"id": "d", "text": "Asigna el puerto por defecto que usa el contenedor"}],
        ["a"],
        "El parámetro '-p' publica un puerto enlazándolo entre la máquina anfitriona (host) y el contenedor (-p puertoHost:puertoContenedor).",
        {"b": "Asignar un nombre al contenedor se hace con el parámetro '--name'.", "c": "No interactúa con el identificador de proceso (PID) del host.", "d": "El puerto por defecto que escucha la aplicación se define en el Dockerfile mediante la directiva EXPOSE."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 2")

    add1("lab1-003", "Comandos Docker CLI", "easy", "single",
        "¿Qué comando de Docker se usa para ver los contenedores activos?",
        [{"id": "a", "text": "docker info"}, {"id": "b", "text": "docker ls"}, {"id": "c", "text": "docker ps -a"}, {"id": "d", "text": "docker ps"}],
        ["d"],
        "'docker ps' lista exclusivamente los contenedores que se encuentran en ejecución (activos).",
        {"a": "'docker info' muestra información general del sistema y del demonio Docker Engine.", "b": "'docker ls' no existe como comando global.", "c": "'docker ps -a' muestra todos los contenedores existentes, incluyendo los detenidos."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 3")

    add1("lab1-004", "Ciclo de Vida de Contenedores", "easy", "single",
        "¿Con qué comando se eliminan contenedores detenidos?",
        [{"id": "a", "text": "docker remove"}, {"id": "b", "text": "docker rm"}, {"id": "c", "text": "docker stop"}, {"id": "d", "text": "docker kill"}],
        ["b"],
        "'docker rm <id-contenedor>' elimina contenedores que ya no están en ejecución.",
        {"a": "'docker remove' no es la sintaxis admitida por el CLI de Docker.", "c": "'docker stop' detiene la ejecución del contenedor de forma limpia, pero no lo borra del almacenamiento.", "d": "'docker kill' interrumpe forzosamente el contenedor enviando SIGKILL, pero preserva su existencia en disco."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 4")

    add1("lab1-005", "Comandos Docker CLI", "easy", "single",
        "¿Para qué sirve el comando docker logs?",
        [{"id": "a", "text": "Eliminar los logs"}, {"id": "b", "text": "Crear logs"}, {"id": "c", "text": "Mandar logs al host"}, {"id": "d", "text": "Consultar logs de un contenedor en concreto"}],
        ["d"],
        "'docker logs' recopila e imprime las salidas stdout y stderr generadas por el proceso principal de un contenedor.",
        {"a": "No borra archivos de log existentes en el demonio.", "b": "No genera entradas de log ficticias; muestra la salida emitida por la aplicación.", "c": "No transporta logs a servidores de logging remotos del host de manera directa."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 5")

    add1("lab1-006", "Contenedores vs Máquinas Virtuales", "easy", "truefalse",
        "En un sistema informático, se pueden ejecutar más máquinas virtuales que contenedores.",
        [{"id": "a", "text": "Verdadero"}, {"id": "b", "text": "Falso"}],
        ["b"],
        "Es Falso. Los contenedores comparten el kernel del host y no necesitan una capa completa de SO invitado ni virtualización de hardware, lo que permite ejecutar una cantidad mucho mayor de contenedores que de máquinas virtuales.",
        {"a": "Es incorrecto. Las máquinas virtuales requieren duplicar el kernel, la memoria dedicada y los servicios del sistema operativo, consumiendo muchísimos más recursos."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 6")

    add1("lab1-007", "Comandos Docker CLI", "easy", "single",
        "¿Para qué sirve el comando \"docker run\"?",
        [{"id": "a", "text": "Borrar un volumen"}, {"id": "b", "text": "Crear una imagen en Docker"}, {"id": "c", "text": "Crear una red nueva"}, {"id": "d", "text": "Crear y ejecutar un contenedor"}],
        ["d"],
        "'docker run' instancia una nueva capa de lectura/escritura a partir de la imagen especificada y arranca su proceso.",
        {"a": "Para borrar volúmenes se utiliza 'docker volume rm'.", "b": "Para construir imágenes se emplea 'docker build'.", "c": "Para crear redes se ejecuta 'docker network create'."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 7")

    add1("lab1-008", "Redes y Mapeo de Puertos", "easy", "single",
        "¿Qué comando de Docker muestra todas las redes existentes?",
        [{"id": "a", "text": "docker ls net"}, {"id": "b", "text": "dotnet network ls"}, {"id": "c", "text": "docker network ls"}, {"id": "d", "text": "docker networks"}],
        ["c"],
        "'docker network ls' enumera todas las redes configuradas en el demonio de Docker.",
        {"a": "'docker ls net' es una combinación sintáctica no admitida en Docker CLI.", "b": "'dotnet network ls' pertenece a .NET y no tiene herramientas de administración de red.", "d": "'docker networks' no es un comando reconocido."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 8")

    add1("lab1-009", "Gestión de Imágenes", "easy", "single",
        "¿Cómo se eliminan imágenes en Docker?",
        [{"id": "a", "text": "docker image delete"}, {"id": "b", "text": "docker image rm"}, {"id": "c", "text": "docker image clear"}, {"id": "d", "text": "docker remove image"}],
        ["b"],
        "'docker image rm' (o 'docker rmi') borra una o varias imágenes locales.",
        {"a": "'docker image delete' no existe como subcomando en Docker.", "c": "'docker image clear' no es un comando de Docker.", "d": "'docker remove image' no coincide con la gramática objeto-verbo de Docker CLI."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 9")

    add1("lab1-010", "Gestión de Imágenes", "easy", "single",
        "¿Para qué sirve el comando \"docker images\"?",
        [{"id": "a", "text": "Listar los contenedores en ejecución"}, {"id": "b", "text": "Listar las imágenes locales"}, {"id": "c", "text": "Crear una imagen"}, {"id": "d", "text": "Borrar imágenes"}],
        ["b"],
        "'docker images' muestra todas las imágenes descargadas o compiladas que residen localmente en el host.",
        {"a": "Listar contenedores en ejecución es la función de 'docker ps'.", "c": "Crear imágenes a partir de un Dockerfile se hace con 'docker build'.", "d": "Borrar imágenes se hace con 'docker image rm'."},
        "Cuestionario Autoevaluación - Práctica 1 (Campus Virtual) - Pregunta 10")

    return lab1, lab2

if __name__ == '__main__':
    l1, l2 = build_data()
    print("Base initialized:", len(l1), len(l2))
