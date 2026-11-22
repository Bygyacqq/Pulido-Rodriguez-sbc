# Sistema Experto de Machine Learning

## 1. Descripción del proyecto

El Sistema Experto de Machine Learning es una aplicación desarrollada en Python que permite orientar la selección de modelos de aprendizaje automático a partir de las características de un problema y de los datos disponibles.

El sistema utiliza una base de conocimiento compuesta por 15 reglas de producción y un motor de inferencia basado en encadenamiento hacia adelante (*Forward Chaining*), encargado de evaluar los hechos ingresados y generar recomendaciones.

La aplicación cuenta con una interfaz gráfica desarrollada con Streamlit, que permite al usuario ingresar las características de su problema, consultar los modelos recomendados y conocer las razones que justifican cada recomendación.

## 2. Objetivo general

Desarrollar un sistema experto que facilite la selección de modelos de Machine Learning mediante reglas de conocimiento e inferencia lógica, considerando el objetivo del problema, las características de los datos y los requerimientos del análisis.

## 3. Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar la lógica del sistema.
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

El sistema contempla los siguientes modelos y algoritmos:

| Categoría | Modelos |
|---|---|
| Clasificación | Regresión Logística, Árbol de Decisión, Random Forest y Gradient Boosting |
| Regresión | Regresión Lineal, Árbol de Decisión, Random Forest y Gradient Boosting |
| Clustering | K-Means y DBSCAN |
| Detección de anomalías | Isolation Forest y One-Class SVM |

## 6. Estructura del proyecto

```text
Sistema_Experto_IA2/
│
├── src/
│   ├── app.py
│   ├── base_conocimiento.py
│   ├── motor_inferencia.py
│   └── pages/
│       └── formulario.py
│
├── docs/
|
|── notebooks/
|    |── Sistema experto.ipynb
│
├── tests/
│   └── test_motor_inferencia.py
│
├── .venv/
│
└── README.md
```

## 7. Instalación y configuración

### 7.1. Requisitos previos

- Python instalado.
- Visual Studio Code o un editor de código.
- Acceso a una terminal de comandos.

### 7.2. Crear el entorno virtual

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m venv .venv
```

### 7.3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 7.4. Instalar las dependencias

Si el proyecto cuenta con un archivo `requirements.txt`, ejecutar:

```bash
pip install -r requirements.txt
```

También se pueden instalar las herramientas utilizadas para ejecutar la aplicación y las pruebas:

```bash
python -m pip install streamlit pytest
```

## 8. Ejecución de la aplicación

Desde la carpeta raíz del proyecto, ejecutar:

```bash
streamlit run src/app.py
```

Streamlit iniciará el servidor local y permitirá acceder a la aplicación desde el navegador.

## 9. Base de conocimiento

La base de conocimiento se encuentra en `src/base_conocimiento.py`.

Está compuesta por 15 reglas de producción que representan las condiciones necesarias para generar recomendaciones y advertencias.

Las reglas contemplan:

- Selección de modelos para clasificación.
- Selección de modelos para regresión.
- Selección de algoritmos de clustering.
- Selección de algoritmos para detección de anomalías.
- Identificación de problemas relacionados con la disponibilidad de etiquetas.

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
tests/test_motor_inferencia.py
```

Para ejecutarlas, utilizar:

```bash
python -m pytest tests/ -v
```

Actualmente se han implementado 10 pruebas automatizadas para verificar:

1. La existencia de las 15 reglas de producción.
2. La recomendación de Regresión Logística.
3. La activación simultánea de múltiples reglas.
4. El comportamiento cuando no se generan conclusiones.
5. La advertencia por ausencia de datos etiquetados.
6. La explicación del razonamiento.
7. La justificación de una conclusión específica.
8. La consulta de conclusiones sin una regla responsable.
9. El registro de eventos del motor de inferencia.
10. El cumplimiento del límite máximo de iteraciones.

**Resultado de validación:** las 10 pruebas automatizadas ejecutadas finalizaron satisfactoriamente.

## 12. Autores

Proyecto desarrollado como parte de la asignatura Inteligencia Artificial II.

