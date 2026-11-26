# Sistema Experto de Machine Learning

## 1. Descripción del proyecto

El Sistema Experto de Machine Learning es una aplicación desarrollada en Python que permite orientar la selección de modelos de aprendizaje automático a partir de las características de un problema y de los datos disponibles.

El sistema utiliza una base de conocimiento compuesta por 15 reglas de producción y un motor de inferencia basado en encadenamiento hacia adelante (*Forward Chaining*), encargado de evaluar los hechos ingresados y generar recomendaciones.

La aplicación cuenta con una interfaz web desarrollada con Streamlit, que permite al usuario ingresar las características de su problema, consultar los modelos recomendados y conocer las razones que justifican cada recomendación.

**Aplicación desplegada:** https://uia3prj8pocurfuawnqcfs.streamlit.app/
**Aplicación desplegada:** [https://sistema-experto-ia2.streamlit.app/](https://uia3prj8pocurfuawnqcfs.streamlit.app/)

## 2. Objetivo general

Desarrollar un sistema experto que facilite la selección de modelos de Machine Learning mediante reglas de conocimiento e inferencia lógica, considerando el objetivo del problema, las características de los datos y los requerimientos del análisis.

## 3. Tecnologías utilizadas

- **Python 3.13:** lenguaje de programación utilizado para desarrollar la lógica del sistema.
- **Streamlit:** framework utilizado para construir la interfaz web.
- **Pytest:** herramienta utilizada para ejecutar las pruebas automatizadas.
- **Logging:** módulo utilizado para registrar eventos durante el proceso de inferencia.

## 4. Funcionalidades principales

- Identificación del objetivo del problema: clasificación, regresión, clustering y detección de anomalías.
- Evaluación de las características y estructura de los datos.
- Evaluación de requerimientos como interpretabilidad y obtención de probabilidades.
- Recomendación de modelos de Machine Learning mediante reglas de producción.
- Explicación del razonamiento utilizado para generar las recomendaciones.
- Consulta de las condiciones que justifican una conclusión mediante la función `porque()`.
- Identificación de situaciones en las que no se generan recomendaciones.
- Reinicio del formulario para realizar nuevos diagnósticos.

## 5. Modelos contemplados

| Categoría | Modelos |
|---|---|
| Clasificación | Regresión logística, Árbol de decisión, Random Forest y Gradient Boosting |
| Regresión | Regresión lineal, Árbol de decisión, Random Forest y Gradient Boosting |
| Clustering | K-Means y DBSCAN |
| Detección de anomalías | Isolation Forest y One-Class SVM |

## 6. Estructura del proyecto

```text
Sistema_Experto_IA2/
│
├── .streamlit/
│   └── config.toml          # Tema: colores, fuente y bordes
│
├── docs/
│   ├── documentacion_tecnica.md
│   └── manual_usuario.md
│
├── notebooks/
│   └── Sistema experto.ipynb
│
├── src/
│   ├── app.py               # Punto de entrada y menú de navegación
│   ├── base_conocimiento.py
│   ├── motor_inferencia.py
│   ├── contenido.py         # Textos, diccionario y biblioteca de modelos
│   ├── estilos.py           # CSS y tarjetas con explicación al pasar el cursor
│   ├── __init__.py
│   └── vistas/
│       ├── diagnostico.py   # Página principal: formulario y resultados
│       └── guia.py          # Guía, diccionario y biblioteca de modelos
│
├── tests/
│   └── test_motor.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

Los entornos virtuales y las carpetas temporales no forman parte de los archivos necesarios para la distribución del código fuente.

## 7. Instalación y configuración

### 7.1. Requisitos previos

- Python 3.13 instalado.
- Visual Studio Code u otro editor de código.
- Acceso a una terminal de comandos.
- Carpeta del proyecto disponible localmente.

### 7.2. Crear el entorno virtual

Desde PowerShell, ubicado en la carpeta raíz del proyecto, ejecutar:

```powershell
py -3.13 -m venv .venv313
```

### 7.3. Activar el entorno virtual

```powershell
.\.venv313\Scripts\Activate.ps1
```

### 7.4. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 8. Ejecución de la aplicación

Desde la carpeta raíz del proyecto, con el entorno virtual activado, ejecutar:

```powershell
python -m streamlit run src/app.py
```

Streamlit iniciará el servidor local y mostrará una dirección para acceder a la aplicación desde el navegador.

Para detener la ejecución, regresar a la terminal y presionar `Ctrl + C`.

También se puede acceder a la versión desplegada mediante:

https://uia3prj8pocurfuawnqcfs.streamlit.app/

## 9. Base de conocimiento

La base de conocimiento se encuentra en `src/base_conocimiento.py`.

Está compuesta por 15 reglas de producción que representan las condiciones necesarias para generar recomendaciones y advertencias.

Las reglas contemplan:

- Selección de modelos para clasificación.
- Selección de modelos para regresión.
- Selección de algoritmos de clustering.
- Selección de algoritmos para detección de anomalías.
- Identificación de situaciones relacionadas con la disponibilidad de etiquetas.

## 10. Motor de inferencia

El motor de inferencia se encuentra en `src/motor_inferencia.py`.

Utiliza el mecanismo de encadenamiento hacia adelante (*Forward Chaining*), que parte de un conjunto de hechos iniciales y evalúa las condiciones de las reglas de la base de conocimiento.

Cuando las condiciones de una regla se cumplen, se genera una nueva conclusión que se incorpora al conjunto de hechos.

El motor también incorpora:

- Registro de eventos mediante Logging.
- Control del número máximo de iteraciones.
- Detección de estados repetidos.
- Seguimiento de las reglas aplicadas.

Además, dispone de las funciones `explicar_razonamiento()` y `porque()`, que permiten consultar el proceso de inferencia y justificar las conclusiones obtenidas.

## 11. Pruebas automatizadas

Las pruebas automatizadas se encuentran en:

```text
tests/test_motor.py
```

Para ejecutarlas, utilizar:

```powershell
python -m pytest tests/ -v
```

El proyecto cuenta con 10 pruebas automatizadas para verificar:

1. La existencia de las 15 reglas de producción.
2. La recomendación de regresión logística.
3. La activación simultánea de múltiples reglas.
4. El comportamiento cuando no se generan conclusiones.
5. La advertencia por ausencia de datos etiquetados.
6. La explicación del razonamiento.
7. La justificación de una conclusión específica.
8. La consulta de conclusiones sin una regla responsable.
9. El registro de eventos del motor de inferencia.
10. El cumplimiento del límite máximo de iteraciones.

**Resultado de validación registrado:** las 10 pruebas automatizadas finalizaron satisfactoriamente (`10 passed`).

## 12. Alcance y limitaciones

El sistema utiliza reglas previamente definidas en una base de conocimiento. Por lo tanto, sus resultados están limitados a los modelos y combinaciones de condiciones representados en dichas reglas.

La aplicación no entrena automáticamente los modelos, no compara su desempeño experimental y no garantiza que una recomendación sea la mejor para cualquier conjunto de datos.

Los porcentajes del gráfico de rendimiento de la interfaz son demostrativos y no representan resultados de evaluaciones experimentales.

Las recomendaciones deben considerarse un punto de partida para el análisis y la selección posterior del modelo.

## 13. Autores

Proyecto desarrollado como parte de la asignatura Inteligencia Artificial II.

**Integrantes:** Dayana Michelle Pulido Moguea.

**Institución:** Geyson Fabian Rodriguez Ortiz.
