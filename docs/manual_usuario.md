# Manual de usuario
## Sistema experto para la recomendación de modelos de aprendizaje automático

**Asignatura:** Inteligencia Artificial II  
**Tecnología:** Python y Streamlit

---

## 1. Introducción

Este manual describe el procedimiento para utilizar el sistema experto desarrollado para recomendar modelos de aprendizaje automático a partir de las características de un problema y de los datos disponibles.

La aplicación permite ingresar información mediante un formulario, ejecutar el proceso de inferencia y consultar las recomendaciones generadas junto con una explicación de las reglas que se activaron.

El sistema funciona como una herramienta de apoyo a la toma de decisiones. Sus recomendaciones constituyen una orientación inicial y no sustituyen la experimentación, la validación de modelos ni el criterio profesional.

## 2. Requisitos para utilizar la aplicación

Para ejecutar el proyecto se requiere:

- Python 3.13 instalado.
- Las dependencias declaradas en el archivo `requirements.txt`.
- La carpeta del proyecto disponible localmente.
- Una terminal ubicada en la carpeta principal del proyecto.

## 3. Instalación y ejecución

### 3.1. Crear el entorno virtual

Desde PowerShell, ubicado en la carpeta raíz del proyecto, ejecutar:

```powershell
py -3.13 -m venv .venv313
```

### 3.2. Activar el entorno virtual

```powershell
.\.venv313\Scripts\Activate.ps1
```

### 3.3. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 3.4. Ejecutar la aplicación

```powershell
streamlit run src/app.py
```

Streamlit mostrará una dirección local en la terminal y abrirá la aplicación en el navegador. Si no se abre automáticamente, se puede copiar la dirección indicada y pegarla en el navegador.

Para detener la aplicación, regresar a la terminal y presionar `Ctrl + C`.

## 4. Uso de la aplicación

### 4.1. Página principal

La página principal presenta el propósito del sistema experto y explica su funcionamiento general. Desde allí, el usuario puede acceder al formulario para registrar las características del problema que desea analizar.

### 4.2. Diligenciamiento del formulario

El usuario debe seleccionar las características que correspondan al problema que desea evaluar.

Las variables contempladas incluyen:

| Característica | Descripción |
|---|---|
| Objetivo | Identifica si el problema corresponde a clasificación, regresión, clustering o detección de anomalías. |
| Estado de las etiquetas | Indica si los datos están etiquetados o no etiquetados. |
| Datos tabulares | Identifica si la información está organizada en filas y columnas. |
| Tipo de relaciones | Permite indicar si las relaciones entre variables son lineales o complejas. |
| Estructura de los grupos | Permite identificar si los grupos son compactos o presentan densidades variables. |
| Datos escalados | Indica si los datos ya fueron escalados o normalizados. |
| Interpretabilidad | Identifica si se necesita que el modelo sea fácil de interpretar. |
| Probabilidades | Indica si se requieren probabilidades asociadas a las predicciones. |
| Requiere etiquetas | Identifica si el escenario necesita etiquetas para el aprendizaje supervisado. |

Es importante responder de acuerdo con las características reales del problema y no seleccionar opciones únicamente para obtener un modelo específico.

### 4.3. Ejecución del proceso de recomendación

Una vez diligenciado el formulario, el usuario debe presionar el botón de envío.

La aplicación transforma las respuestas en hechos iniciales y ejecuta el motor de inferencia sobre la base de conocimiento.

El motor evalúa las condiciones de las reglas y genera las conclusiones correspondientes cuando encuentra coincidencias.

### 4.4. Interpretación de los resultados

La aplicación presenta los modelos que se obtuvieron como conclusiones del proceso de inferencia.

Entre los modelos contemplados en la base de conocimiento se encuentran:

- Regresión logística.
- Árbol de decisión para clasificación.
- Random Forest para clasificación.
- Gradient Boosting para clasificación.
- Regresión lineal.
- Árbol de decisión para regresión.
- Random Forest para regresión.
- Gradient Boosting para regresión.
- K-Means.
- DBSCAN.
- Isolation Forest.
- One-Class SVM.

Dependiendo de las características ingresadas, el sistema puede generar una o varias recomendaciones.

Si ninguna regla produce una recomendación, la aplicación presenta el siguiente mensaje:

**No se encontraron recomendaciones para las características ingresadas.**

Esto significa que las respuestas no satisficieron los antecedentes de las reglas disponibles. No significa necesariamente que no exista un modelo adecuado para el problema.

### 4.5. Consulta de explicaciones

La aplicación incluye una sección denominada **¿Por qué se recomienda este modelo?**

Esta funcionalidad permite consultar la justificación de una recomendación específica.

La explicación presenta:

- La regla que generó la recomendación.
- La descripción de la regla.
- Las condiciones necesarias para que se activara.
- La conclusión obtenida.

De esta manera, el usuario puede comprender el razonamiento utilizado por el sistema experto.

### 4.6. Reinicio del formulario

La aplicación dispone de un botón para reiniciar el formulario y volver al estado inicial.

Esta opción permite realizar nuevas consultas con diferentes características sin necesidad de cerrar la aplicación.

## 5. Ejemplos de escenarios

Los siguientes escenarios corresponden a pruebas realizadas durante la validación funcional del sistema.

| Objetivo | Características relevantes | Recomendaciones obtenidas |
|---|---|---|
| Clasificación | Datos tabulares y relaciones complejas | Regresión logística, Random Forest y Gradient Boosting para clasificación. |
| Regresión | Relaciones lineales | Regresión lineal y árbol de decisión para regresión, según las condiciones adicionales seleccionadas. |
| Clustering | Grupos compactos y datos tabulares | K-Means. |
| Detección de anomalías | Datos tabulares y datos escalados | Isolation Forest y One-Class SVM. |

Los resultados dependen de la combinación exacta de hechos ingresados y de las reglas activadas.

## 6. Recomendaciones de uso

Para obtener resultados coherentes se recomienda:

- Identificar correctamente el objetivo del problema.
- Verificar si los datos cuentan con etiquetas.
- Determinar si la información es tabular.
- Analizar el tipo de relaciones entre las variables.
- Identificar si los datos requieren escalado.
- Revisar las explicaciones de las recomendaciones generadas.
- Evaluar posteriormente los modelos con datos reales y métricas apropiadas antes de utilizarlos en un entorno productivo.

## 7. Solución de problemas frecuentes

| Situación | Solución recomendada |
|---|---|
| El comando `streamlit` no se reconoce | Activar el entorno virtual e instalar las dependencias desde `requirements.txt`. |
| No se abre automáticamente el navegador | Copiar la dirección local que Streamlit muestra en la terminal. |
| No aparecen recomendaciones | Revisar las respuestas del formulario y verificar si coinciden con las condiciones de las reglas. |
| Se desea realizar otra consulta | Utilizar el botón de reinicio de la aplicación. |
| La aplicación presenta un error al iniciar | Revisar el mensaje de error en la terminal y verificar las dependencias instaladas. |

## 8. Alcance y limitaciones

El sistema utiliza reglas previamente definidas en una base de conocimiento. Por lo tanto, sus resultados están limitados a los modelos y combinaciones de condiciones representados en dichas reglas.

La aplicación no entrena automáticamente los modelos, no compara su desempeño experimental y no garantiza que una recomendación sea la mejor para cualquier conjunto de datos.

Las recomendaciones deben considerarse un punto de partida para el análisis y la selección posterior del modelo.

---

**Fin del manual de usuario.**