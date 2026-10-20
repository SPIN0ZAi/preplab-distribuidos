# ⚡ PrepLab — Sistemas Distribuidos (Prácticas 1 y 2)

Plataforma web estática moderna, ligera y de alto rendimiento diseñada para la preparación y autoevaluación exhaustiva de los exámenes de laboratorio de **Sistemas Distribuidos**:
- **Práctica 1**: Dockerización de aplicaciones modernas, contenedores, redes de puente (*bridge*), volúmenes, Compose, Dockerfiles multi-stage, .NET 10 Web API, CORS, Blazor WebAssembly y Nginx reverse proxy.
- **Práctica 2**: Arquitecturas RPC, gRPC con ASP.NET Core, Protocol Buffers (Proto3), HTTP/2 sin TLS (`Cleartext HTTP/2`), tipos de comunicación (Unary, Server/Client Streaming, Bidirectional), y sincronización de concurrencia en C# (`lock`, `Monitor`, `Mutex`, `SemaphoreSlim`, `Interlocked`, `ReaderWriterLockSlim`).

Construido siguiendo la metodología **AI-DLC (AI Development Life Cycle)** combinada con **SDD (Software Design Document)** para garantizar trazabilidad rigurosa, cero alucinaciones y cumplimiento exacto de los criterios pedagógicos del profesor.

---

## 🚀 Características Principales

1. **Banco de Preguntas Exhaustivo (520 preguntas verificadas)**:
   - **260 preguntas de la Práctica 1** (incluyendo textualmente las 10 preguntas originales del examen de muestra del profesor `lab1-001` a `lab1-010`).
   - **260 preguntas de la Práctica 2** (cobertura total de gRPC, sintaxis Proto3, HTTP/2 `ListenOptions.Protocols`, y primitivas de sincronización de hilos).
   - **0 duplicados** y validación automatizada mediante schema JSON (`npm run validate`).
   - **Explicaciones completas**: cada pregunta incluye tanto el razonamiento de la respuesta correcta como la justificación específica de por qué cada distractor es incorrecto (`explanation.wrong[optId]`).

2. **Simulacros de Examen Personalizados**:
   - Intentos aleatorios de **20 preguntas**.
   - **Muestreo ponderado inteligente**:
     - Preguntas no vistas previamente: **3.0x** de probabilidad.
     - Preguntas falladas en intentos anteriores: **2.5x** de probabilidad.
     - Preguntas ya acertadas: **1.0x** de probabilidad.
   - Opciones barajadas dinámicamente mediante el algoritmo Fisher-Yates para evitar memorización por posición.

3. **Temporizador Preciso basado en Marcas de Tiempo**:
   - Ajustable: Preajustes de 10, 20, 30, 45, 60 minutos, minutos personalizados o desactivado.
   - No sufre desvíos por inactividad de pestañas o suspensión gracias a cálculo continuo contra `Date.now()`.
   - Alerta visual con pulso ámbar/rojo al restar menos de 60 segundos.
   - Entrega automática al expirar el tiempo.

4. **Revisión Detallada y Reintento de Errores**:
   - Criterio de aprobado oficial: $\ge 50\%$.
   - Filtros de revisión: *Todas*, *Solo Falladas*, *Acertadas*.
   - Botón directo **"Reintentar preguntas falladas"** para reforzar inmediatamente los conceptos errados.
   - Tarjetas de explicación que desglosan minuciosamente la justificación de la opción correcta y de cada alternativa errónea.

5. **Historial Persistente y Análisis de Debilidades por Tema**:
   - Almacenamiento local seguro (`localStorage`) sin necesidad de base de datos ni registro externo.
   - Recuperación automática de sesiones interrumpidas (puedes cerrar el navegador y reanudar donde lo dejaste).
   - Tabla analítica de debilidades ordenada de menor a mayor tasa de acierto con barras de progreso codificadas por color (rojo < 60%, amarillo 60-79%, verde ≥ 80%).

6. **Sistema Visual de Doble Capa (Venus Soft-UI + Apple Liquid Glass)**:
   - **Capa de Contenido (Venus Dashboard Builder)**: Tarjetas blancas opacas (#FFFFFF / #111827 en dark mode) con sombras difusas, acentos índigo eléctrico (`#4318FF`) y contraste superior a 7:1 para una lectura óptima y descansada de las 520 preguntas.
   - **Capa de Cromo (Apple Liquid Glass - iOS 26)**: Superficies translúcidas flotantes con fórmula óptica de 6 capas (doble pasada de desenfoque + saturación, borde especular de 1px, resalte interior y degradado en ángulo) para barras de navegación, temporizador y modales.
   - **Regla 10 (Disciplina de Vidrio)**: El cristal translúcido está estrictamente limitado a la navegación (< 25% del viewport). Las preguntas, respuestas y bloques de código residen siempre en tarjetas sólidas opacas para evitar la fatiga visual.
   - **Gráficos SVG de Dependencia Cero**: Gráficos de barras redondeadas estilo Venus con una barra destacada en índigo, líneas de área fluidas con curvas cúbicas de Bézier y medidores circulares de puntuación sin dependencias externas pesadas.

7. **Rendimiento Ultraligero (< 61 KB gzip inicial)**:
   - Los bancos de preguntas se cargan bajo demanda mediante importaciones dinámicas (`loadLab1Questions()`, `loadLab2Questions()`).
   - El bundle principal de JavaScript ocupa tan solo **61.00 KB gzipped** (muy por debajo del límite estricto de 200 KB).
   - Tipografía moderna: Poppins para métricas y titulares, Plus Jakarta Sans / Inter para texto general.

---

## 🛠️ Metodología AI-DLC + SDD

El desarrollo del proyecto se estructuró en cinco fases documentadas en el artefacto de diseño:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INGESTIÓN Y SÍNTESIS                                     │
│    - Extracción de PDFs y guías de Lab 1 y Lab 2           │
│    - Análisis de dificultad, estilo y distractores docente │
├─────────────────────────────────────────────────────────────┤
│ 2. SDD ARCHITECTURE & CONTRACT SPECIFICATION                │
│    - Schema TypeScript estricto                             │
│    - Reglas de validación JSON automatizadas                │
├─────────────────────────────────────────────────────────────┤
│ 3. GENERACIÓN MODULAR DEL BANCO (520 PREGUNTAS)             │
│    - 4 módulos para Lab 1 (260 preguntas)                   │
│    - 4 módulos para Lab 2 (260 preguntas)                   │
│    - Verificación contra preguntas originales del docente   │
├─────────────────────────────────────────────────────────────┤
│ 4. DESARROLLO DEL MOTOR Y COMPONENTES FRONTEND              │
│    - Storage service con recuperación de sesión             │
│    - Motor de muestreo ponderado                            │
│    - Componentes React: Landing, Quiz, Timer, Results, Modal│
├─────────────────────────────────────────────────────────────┤
│ 5. VALIDACIÓN, PRUEBAS Y OPTIMIZACIÓN VERCEL                │
│    - npm run validate: 0 errores                            │
│    - npm run build: TS OK, bundle inicial 56 KB gzip        │
│    - vercel.json configurado para despliegue estático SPA   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Estructura del Proyecto

```text
├── index.html                      # Punto de entrada HTML con meta-tags SEO y tipografía
├── package.json                    # Dependencias y scripts
├── tsconfig.json                   # Configuración TypeScript estricta
├── vite.config.ts                  # Configuración de empaquetado Vite
├── vercel.json                     # Configuración de despliegue y rewrites en Vercel
├── scripts/
│   ├── validate-questions.mjs      # Validador de schema, unicidad y distractores
│   ├── generate_master.py          # Ensamblador del banco maestro
│   └── generators/                 # Generadores modulares por práctica
│       ├── lab1_part1.py .. lab1_part4.py
│       └── lab2_part1.py .. lab2_part4.py
├── src/
│   ├── index.css                   # Sistema de diseño con tokens CSS, temas y animaciones
│   ├── main.tsx                    # Montaje de la aplicación React
│   ├── App.tsx                     # Máquina de estados principal y navegación
│   ├── types/
│   │   └── quiz.ts                 # Definiciones de tipos (Question, AttemptResult, etc.)
│   ├── services/
│   │   ├── storage.ts              # Gestor de localStorage y cálculo de debilidades
│   │   └── quizEngine.ts           # Muestreo ponderado, carga diferida y evaluación
│   ├── data/
│   │   ├── lab1.json               # 260 preguntas de Práctica 1
│   │   └── lab2.json               # 260 preguntas de Práctica 2
│   └── components/
│       ├── LandingScreen.tsx       # Selector de práctica, usuario y temporizador
│       ├── QuizScreen.tsx          # Barra de 20 preguntas, visor y modal de entrega
│       ├── Timer.tsx               # Cuenta atrás basada en timestamp con pulso visual
│       ├── ResultsScreen.tsx       # Desglose de nota, filtros y revisión de distractores
│       └── HistoryModal.tsx        # Historial de intentos y analítica de temas
```

---

## 💻 Instalación y Uso Local

### Requisitos previos
- Node.js (versión 18 o superior recomendada; probado en Node v24)
- npm

### 1. Clonar o acceder al directorio del proyecto
```bash
cd "c:/Users/ssola/Desktop/documentos de estudios/3 year/distribuidos/LAB/lab 1 and 2 test preparation"
```

### 2. Instalar dependencias
```bash
npm install
```

### 3. Validar el banco de preguntas
Ejecuta la suite de validación estricta (comprueba unicidad de IDs, campos requeridos, opciones válidas y explicaciones para cada opción incorrecta):
```bash
npm run validate
```

### 4. Iniciar el servidor de desarrollo
```bash
npm run dev
```
Abre en tu navegador la dirección indicada (por defecto [http://localhost:5173](http://localhost:5173)).

### 5. Compilar para producción
```bash
npm run build
```
Genera la versión optimizada en la carpeta `dist/` (incluye validación previa automática y verificación de TypeScript).

---

## ☁️ Despliegue en Vercel

El proyecto está preparado para desplegarse en **Vercel** de forma estática con un solo clic:

1. **Subir a GitHub**: Realiza un `git push` a tu repositorio personal en GitHub.
2. **Conectar en Vercel**:
   - Entra en [vercel.com](https://vercel.com) y selecciona **Add New Project**.
   - Importa tu repositorio.
   - Vercel detectará automáticamente la configuración definida en [vercel.json](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/vercel.json):
     - **Framework Preset**: `Vite`
     - **Build Command**: `npm run build`
     - **Output Directory**: `dist`
3. **Despliegue completado**: Vercel desplegará tu aplicación en una URL global rápida y segura (HTTPS).

---

## 📚 Desglose Temático del Banco de Preguntas

| Práctica | Preguntas | Temas Cubiertos |
| :--- | :---: | :--- |
| **Práctica 1** (Docker & .NET) | **260** | Conceptos básicos de Docker, imágenes, contenedores, redes bridge, volúmenes con nombre y bind mounts, Compose (v2, variables de entorno, depends_on), Dockerfiles multi-stage (.NET 10 SDK vs ASP.NET runtime), puertos (`EXPOSE` vs `-p`), Nginx como reverse proxy, configuración de CORS en ASP.NET Core (`WithOrigins`, preflight OPTIONS), y despliegue de Blazor WebAssembly. |
| **Práctica 2** (gRPC & Concurrencia) | **260** | Fundamentos de RPC vs REST, sintaxis Protocol Buffers v3 (`syntax = "proto3"`, tags de campo, tipos escalares, `repeated`, `optional`, `oneof`, enums), generación de stubs (`Grpc.Tools`, protoc), HTTP/2 sin cifrado (`HttpProtocols.Http2` en Kestrel), patrones gRPC (Unary, Server Streaming, Client Streaming, Bidirectional), y sincronización de concurrencia en C# (`lock`, `Monitor`, `Interlocked`, `SemaphoreSlim`, `Mutex`, `ReaderWriterLockSlim`). |
| **Total** | **520** | **Cobertura integral del temario oficial.** |

---

*Desarrollado con arquitectura moderna, tipado estricto y diseño optimizado para el éxito en el examen de Sistemas Distribuidos.*
