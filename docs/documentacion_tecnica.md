# Documentación técnica
## Sistema experto para la recomendación de modelos de aprendizaje automático

**Asignatura:** Inteligencia Artificial II  
**Lenguaje de programación:** Python  
**Tecnología de interfaz:** Streamlit

---

## 1. Propósito del documento

El presente documento describe la estructura, arquitectura y funcionamiento técnico del sistema experto desarrollado para recomendar modelos de aprendizaje automático a partir de las características de un problema.

Se presentan los componentes principales del proyecto, la representación del conocimiento, el mecanismo de inferencia, las funcionalidades de explicación, las pruebas automatizadas y las instrucciones necesarias para ejecutar la solución.

## 2. Descripción general del sistema

El proyecto implementa un sistema experto basado en reglas que permite recomendar modelos de aprendizaje automático según las características de un problema y los datos disponibles.

El usuario proporciona información mediante una interfaz web desarrollada con Streamlit. Estas respuestas se transforman en hechos que posteriormente son evaluados por un motor de inferencia.

El motor utiliza una estrategia de encadenamiento hacia adelante (*Forward Chaining*), mediante la cual analiza las condiciones de las reglas de la base de conocimiento y genera conclusiones cuando encuentra coincidencias.

El sistema permite obtener recomendaciones y consultar las reglas que justifican cada resultado.

## 3. Arquitectura del sistema

La solución se encuentra organizada en diferentes componentes que separan la interfaz, la representación del conocimiento y el proceso de inferencia.

Los componentes principales son:

1. **Interfaz de usuario:** permite ingresar las características del problema mediante Streamlit.
2. **Generación de hechos:** transforma las respuestas del formulario en hechos iniciales.
3. **Base de conocimiento:** almacena las reglas que relacionan las condiciones con las conclusiones.
4. **Motor de inferencia:** evalúa las reglas y genera nuevas conclusiones.
5. **Módulo de explicación:** permite identificar las reglas aplicadas y justificar las recomendaciones.
6. **Módulo de pruebas:** verifica el funcionamiento de los componentes principales mediante pruebas automatizadas.

### 3.1. Flujo general del sistema

```text
             USUARIO
                |
                v
       INTERFAZ STREAMLIT
                |
                v
       FORMULARIO DE ENTRADA
                |
                v
       GENERACIÓN DE HECHOS
                |
                v
       BASE DE CONOCIMIENTO
                |
                v
        MOTOR DE INFERENCIA
                |
                v
       HECHOS Y CONCLUSIONES
                |
                v
       REGLAS APLICADAS
                |
                v
       MÓDULO DE EXPLICACIÓN
                |
                v
       PRESENTACIÓN DE RESULTADOS
```

## 4. Estructura del proyecto

La organización del proyecto se encuentra distribuida de la siguiente manera:

```text
Sistema_Experto_IA2/
│
├── docs/
│   ├── documentacion_tecnica.md
│   └── manual_usuario.md
│
├── notebooks/
│   └── Sistema experto.ipynb
│
├── src/
│   ├── app.py
│   ├── base_conocimiento.py
│   ├── motor_inferencia.py
│   ├── init.py
│   │
│   └── pages/
│       └── formulario.py
│
├── tests/
│   └── test_motor.py
│
├── README.md
└── requirements.txt
```

Los directorios `.venv`, `.venv313`, `__pycache__` y `.pytest_cache` corresponden a entornos virtuales o archivos temporales generados durante la ejecución y las pruebas. No forman parte de los componentes funcionales principales del sistema.

**Nota técnica:** en la estructura revisada aparece `init.py`. El nombre convencional para el archivo de inicialización de un paquete Python es `__init__.py`. Se debe verificar su contenido y las importaciones antes de realizar cualquier cambio.

## 5. Descripción de los componentes

### 5.1. Archivo `app.py`

Se encuentra en `src/app.py` y constituye el punto de entrada de la aplicación.

Su función principal es presentar la página inicial del sistema experto mediante Streamlit y permitir el acceso al formulario de consulta.

### 5.2. Archivo `formulario.py`

Se encuentra en `src/pages/formulario.py`.

Contiene el formulario mediante el cual el usuario ingresa las características del problema.

Entre las características contempladas se encuentran:

- Objetivo del problema.
- Estado de las etiquetas.
- Disponibilidad de datos tabulares.
- Tipo de relaciones entre variables.
- Estructura de los grupos.
- Disponibilidad de datos escalados.
- Necesidad de interpretabilidad.
- Necesidad de probabilidades.
- Requerimiento de etiquetas.

Las respuestas se convierten en hechos iniciales que posteriormente son procesados por el motor de inferencia.

Este componente también presenta las recomendaciones, las explicaciones y la opción de reiniciar el formulario.

### 5.3. Archivo `base_conocimiento.py`

Contiene la representación del conocimiento mediante reglas de producción.

El archivo incluye la función:

```python
crear_regla(identificador, condiciones, conclusion, descripcion)
```

Esta función permite construir las reglas mediante un diccionario con los siguientes elementos:

| Elemento | Descripción |
|---|---|
| `id` | Identificador único de la regla. |
| `condiciones` | Conjunto de condiciones necesarias para activar la regla. |
| `conclusion` | Resultado que se genera cuando se cumplen las condiciones. |
| `descripcion` | Explicación del propósito de la regla. |

La función `crear_base_conocimiento()` construye y retorna una base de conocimiento compuesta por 15 reglas.

### 5.4. Archivo `motor_inferencia.py`

Contiene el mecanismo encargado de evaluar las reglas y generar conclusiones.

La función principal es:

```python
encadenamiento_hacia_adelante(
    hechos_iniciales,
    base_conocimiento,
    max_iteraciones=100
)
```

Esta función recibe:

- Los hechos iniciales.
- La base de conocimiento.
- El número máximo de iteraciones permitido.

El proceso retorna dos elementos:

- El conjunto de hechos finales.
- La lista de reglas aplicadas.

El motor evalúa si las condiciones de cada regla se encuentran contenidas en el conjunto de hechos conocidos. Cuando se cumplen, registra la regla y agrega su conclusión si todavía no existe.

### 5.5. Funciones de explicación

El motor también incorpora las siguientes funciones:

**`explicar_razonamiento(reglas_aplicadas)`**

Recorre las reglas que fueron activadas durante el proceso y presenta su identificador, descripción y conclusión.

**`porque(conclusion, reglas_aplicadas)`**

Permite consultar las reglas responsables de una conclusión específica. Presenta las condiciones necesarias y la descripción de las reglas encontradas.

Estas funciones aportan transparencia y permiten comprender cómo se obtuvo una recomendación.

## 6. Base de conocimiento

La base de conocimiento está compuesta por 15 reglas identificadas desde R1 hasta R15.

Las reglas relacionan las características del problema con diferentes modelos de aprendizaje automático y conclusiones auxiliares.

### 6.1. Descripción de las reglas

| Regla | Condiciones | Conclusión |
|---|---|---|
| R1 | Objetivo Clasificación y datos tabulares | Regresión logística |
| R2 | Objetivo Clasificación y requiere interpretabilidad | Árbol de decisión para clasificación |
| R3 | Objetivo Clasificación y relaciones complejas | Random Forest para clasificación |
| R4 | Objetivo Clasificación, relaciones complejas y datos tabulares | Gradient Boosting para clasificación |
| R5 | Objetivo Clasificación y requiere probabilidades | Regresión logística |
| R6 | Objetivo Regresión y relaciones lineales | Regresión lineal |
| R7 | Objetivo Regresión y requiere interpretabilidad | Árbol de decisión para regresión |
| R8 | Objetivo Regresión, relaciones complejas y datos tabulares | Random Forest para regresión |
| R9 | Objetivo Regresión, relaciones complejas y datos tabulares | Gradient Boosting para regresión |
| R10 | Objetivo Clustering, grupos compactos y datos tabulares | K-Means |
| R11 | Objetivo Clustering y grupos de densidades variables | DBSCAN |
| R12 | Objetivo Anomalías y datos tabulares | Isolation Forest |
| R13 | Objetivo Anomalías y datos escalados | One-Class SVM |
| R14 | Requiere etiquetas y estado de etiquetas etiquetados | Modelo supervisado |
| R15 | Requiere etiquetas y estado de etiquetas no etiquetados | Advertencia de datos no etiquetados |

Las reglas pueden activarse simultáneamente cuando sus condiciones se cumplen. Por esta razón, una consulta puede producir varias recomendaciones.

## 7. Mecanismo de inferencia

El sistema utiliza encadenamiento hacia adelante (*Forward Chaining*), una estrategia de inferencia que parte de hechos conocidos para obtener nuevas conclusiones mediante la aplicación de reglas.

### 7.1. Etapas del proceso

1. Se inicializa el conjunto de hechos con las respuestas del usuario.
2. Se recorren las reglas disponibles en la base de conocimiento.
3. Se comparan las condiciones de cada regla con los hechos existentes.
4. Si todas las condiciones se cumplen, la regla se registra como aplicada.
5. Se incorpora la conclusión correspondiente si todavía no está presente.
6. Se repite el proceso mientras se generen nuevos hechos y no se alcance el límite de iteraciones.
7. Se retornan los hechos finales y las reglas aplicadas.

La comprobación principal consiste en verificar que todas las condiciones de una regla estén contenidas en el conjunto de hechos conocidos.

### 7.2. Controles de seguridad

El motor incorpora mecanismos para controlar la ejecución:

- **Límite de iteraciones:** establece un máximo de ciclos para evitar procesos indefinidos.
- **Detección de estados repetidos:** permite detener el proceso si se identifica un estado previamente visitado.
- **Registro de eventos:** permite realizar seguimiento de las operaciones ejecutadas durante la inferencia.

## 8. Registro de eventos

El proyecto utiliza el módulo `logging` de Python para registrar los eventos relevantes del motor de inferencia.

Entre los eventos registrados se encuentran:

- Inicio del proceso de inferencia.
- Número de iteración.
- Activación de reglas.
- Generación de nuevas conclusiones.
- Advertencias por límite de iteraciones.
- Detección de estados repetidos.
- Finalización del proceso.

Este mecanismo facilita el seguimiento y la depuración del funcionamiento del sistema.

## 9. Pruebas automatizadas

El proyecto utiliza `pytest` para verificar el comportamiento de los componentes principales.

Se implementaron y ejecutaron 10 pruebas automatizadas:

| N.º | Nombre de la prueba | Objetivo |
|---:|---|---|
| 1 | `test_base_conocimiento_contiene_15_reglas` | Verificar que la base de conocimiento contenga 15 reglas. |
| 2 | `test_encadenamiento_recomienda_regresion_logistica` | Comprobar la generación de la recomendación de regresión logística. |
| 3 | `test_encadenamiento_activa_varias_reglas` | Verificar que varias reglas puedan activarse simultáneamente. |
| 4 | `test_encadenamiento_sin_conclusiones` | Comprobar el comportamiento cuando ninguna regla genera conclusiones. |
| 5 | `test_advertencia_datos_no_etiquetados` | Verificar la advertencia asociada a datos no etiquetados. |
| 6 | `test_explicar_razonamiento_muestra_reglas_aplicadas` | Comprobar que se presenten las reglas aplicadas. |
| 7 | `test_porque_explicar_conclusion_especifica` | Verificar la consulta de explicación de una conclusión específica. |
| 8 | `test_porque_sin_regla_responsable` | Comprobar el comportamiento cuando no existe una regla responsable. |
| 9 | `test_logging_registra_eventos_del_motor` | Verificar el registro de eventos del motor de inferencia. |
| 10 | `test_motor_respeta_limite_de_iteraciones` | Comprobar el cumplimiento del límite de iteraciones. |

### 9.1. Ejecución de las pruebas

Para ejecutar las pruebas desde PowerShell, con el entorno virtual activado, utilizar:

```powershell
python -m pytest tests/ -v
```

### 9.2. Resultado de la validación

Durante la validación del proyecto se obtuvo el siguiente resultado:

```text
10 passed
```

Esto indica que las 10 pruebas automatizadas ejecutadas finalizaron satisfactoriamente en el entorno Python 3.13.

## 10. Tecnologías y herramientas utilizadas

| Tecnología | Utilización |
|---|---|
| Python 3.13 | Lenguaje de programación principal. |
| Streamlit | Desarrollo de la interfaz web. |
| Pytest | Ejecución de pruebas automatizadas. |
| Logging | Registro de eventos del motor de inferencia. |
| Jupyter Notebook | Entorno de trabajo y experimentación. |
| PowerShell | Ejecución de comandos y administración del entorno. |

## 11. Instalación y ejecución del proyecto

### 11.1. Crear el entorno virtual

```powershell
py -3.13 -m venv .venv313
```

### 11.2. Activar el entorno

```powershell
.\.venv313\Scripts\Activate.ps1
```

### 11.3. Actualizar pip

```powershell
python -m pip install --upgrade pip
```

### 11.4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 11.5. Ejecutar las pruebas

```powershell
python -m pytest tests/ -v
```

### 11.6. Ejecutar la aplicación

```powershell
streamlit run src/app.py
```

## 12. Dependencias del proyecto

El archivo `requirements.txt` contiene las dependencias externas necesarias para ejecutar el proyecto.

En la configuración revisada se incluyen:

- `streamlit`: permite construir y ejecutar la interfaz web.
- `pytest`: permite ejecutar las pruebas automatizadas.

El módulo `logging` pertenece a la biblioteca estándar de Python, por lo que no requiere instalación adicional.

## 13. Alcance y limitaciones

El sistema presenta las siguientes características y limitaciones:

- La base de conocimiento está compuesta por reglas definidas previamente.
- Las recomendaciones dependen de las condiciones establecidas en dichas reglas.
- El motor realiza inferencia simbólica y no entrena modelos de aprendizaje automático.
- El sistema no calcula métricas de desempeño ni selecciona automáticamente el modelo con mejores resultados experimentales.
- La calidad de las recomendaciones depende de la pertinencia y cobertura de la base de conocimiento.
- Las recomendaciones deben validarse posteriormente mediante experimentación con datos reales.

## 14. Posibles mejoras futuras

Como oportunidades de evolución del proyecto se consideran:

- Ampliar la base de conocimiento con nuevos modelos y condiciones.
- Incorporar validaciones adicionales en el formulario.
- Integrar métricas de evaluación de modelos.
- Incorporar conjuntos de datos de prueba para comparar recomendaciones.
- Ampliar la cobertura de las pruebas automatizadas.
- Mejorar la gestión y documentación de las dependencias.

## 15. Conclusiones

El proyecto integra una interfaz web, una base de conocimiento basada en reglas y un motor de inferencia mediante encadenamiento hacia adelante.

La separación de los componentes permite organizar el código y facilitar su mantenimiento. Asimismo, la incorporación de funciones de explicación permite identificar las reglas responsables de las recomendaciones, aportando transparencia al proceso de razonamiento.

Finalmente, la ejecución satisfactoria de las 10 pruebas automatizadas y la comprobación funcional de la aplicación en Streamlit constituyen evidencias de validación del funcionamiento implementado.

---

**Fin de la documentación técnica.**