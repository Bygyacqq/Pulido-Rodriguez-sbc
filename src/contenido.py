"""
Contenido compartido por las páginas: nombres de modelos, textos de ayuda,
diccionario de conceptos y biblioteca de modelos.

Tenerlo en un solo archivo evita que las dos páginas se desincronicen.
"""

nombres_modelos = {
    "RegresionLogistica": "Regresión Logística",
    "ArbolDecisionClasificacion": "Árbol de Decisión para Clasificación",
    "RandomForestClasificacion": "Random Forest para Clasificación",
    "GradientBoostingClasificacion": "Gradient Boosting para Clasificación",
    "RegresionLineal": "Regresión Lineal",
    "ArbolDecisionRegresion": "Árbol de Decisión para Regresión",
    "RandomForestRegresion": "Random Forest para Regresión",
    "GradientBoostingRegresion": "Gradient Boosting para Regresión",
    "KMeans": "K-Means",
    "DBSCAN": "DBSCAN",
    "IsolationForest": "Isolation Forest",
    "OneClassSVM": "One-Class SVM"
}

descripciones_modelos = {
    "RegresionLogistica": "Modelo para clasificación que permite estimar probabilidades.",
    "ArbolDecisionClasificacion": "Modelo de clasificación basado en decisiones jerárquicas.",
    "RandomForestClasificacion": "Conjunto de árboles de decisión para resolver problemas de clasificación.",
    "GradientBoostingClasificacion": "Modelo de clasificación que combina árboles de forma secuencial.",
    "RegresionLineal": "Modelo que estima relaciones lineales entre variables.",
    "ArbolDecisionRegresion": "Modelo de regresión basado en decisiones jerárquicas.",
    "RandomForestRegresion": "Conjunto de árboles para estimar valores numéricos.",
    "GradientBoostingRegresion": "Modelo de regresión que combina árboles secuencialmente.",
    "KMeans": "Algoritmo que agrupa datos en grupos según su similitud.",
    "DBSCAN": "Algoritmo que identifica grupos según la densidad de los datos.",
    "IsolationForest": "Algoritmo que identifica observaciones anómalas.",
    "OneClassSVM": "Modelo que identifica observaciones que se alejan del comportamiento normal."
}

rendimiento_modelos = {
    "RegresionLogistica": 88,
    "ArbolDecisionClasificacion": 83,
    "RandomForestClasificacion": 94,
    "GradientBoostingClasificacion": 92,
    "RegresionLineal": 89,
    "ArbolDecisionRegresion": 82,
    "RandomForestRegresion": 93,
    "GradientBoostingRegresion": 91,
    "KMeans": 87,
    "DBSCAN": 90,
    "IsolationForest": 89,
    "OneClassSVM": 85
}

descripciones_predicados = {
    "Objetivo": "Objetivo del problema",
    "EstadoEtiquetas": "Estado de las etiquetas",
    "DatosTabulares": "Los datos tienen estructura tabular",
    "Relaciones": "Tipo de relaciones entre variables",
    "RequiereInterpretabilidad": "Se requiere interpretabilidad",
    "RequiereProbabilidades": "Se requieren probabilidades",
    "EstructuraGrupos": "Estructura de los grupos",
    "DatosEscalados": "Los datos están escalados",
    "RequiereEtiquetas": "El problema requiere etiquetas"
}

valores_legibles = {
    "Clasificacion": "Clasificación",
    "Regresion": "Regresión",
    "Clustering": "Clustering",
    "Anomalias": "Detección de anomalías",
    "Etiquetados": "Etiquetados",
    "NoEtiquetados": "No etiquetados",
    "Lineales": "Lineales",
    "Complejas": "Complejas",
    "Compactos": "Compactos",
    "DensidadesVariables": "Densidades variables"
}

diccionario = {
    "🎯 Objetivos del problema": {
        "Clasificación": "Problemas cuyo objetivo es asignar una categoría o clase a los datos.",
        "Regresión": "Problemas cuyo objetivo es predecir un valor numérico.",
        "Clustering": "Proceso de agrupar datos según sus características o similitudes.",
        "Detección de anomalías": "Identificación de observaciones que presentan comportamientos inusuales."
    },

    "📊 Características de los datos": {
        "Datos tabulares": "Información organizada en filas y columnas.",
        "Datos etiquetados": "Datos que cuentan con una categoría o resultado conocido.",
        "Datos no etiquetados": "Datos que no tienen una categoría o resultado previamente asignado.",
        "Datos escalados": "Datos cuyos valores han sido transformados a una escala determinada."
    },

    "🔗 Relaciones y estructura": {
        "Relaciones lineales": "Relaciones entre variables que pueden representarse aproximadamente mediante una línea recta.",
        "Relaciones complejas": "Relaciones entre variables que no se representan fácilmente mediante una relación lineal.",
        "Grupos compactos": "Conjuntos de datos cuyos elementos se encuentran relativamente próximos entre sí.",
        "Densidades variables": "Grupos de datos que presentan diferentes concentraciones de observaciones."
    },

    "⚙️ Requerimientos del análisis": {
        "Interpretabilidad": "Capacidad de comprender cómo un modelo genera sus predicciones.",
        "Probabilidades": "Valores que representan la posibilidad de que ocurra un resultado."
    }
}

biblioteca_modelos = {
    "🎯 Modelos de clasificación": {
        "Regresión Logística": {
            "que_es": "Es un algoritmo de aprendizaje supervisado que estima la probabilidad de que una observación pertenezca a una categoría.",
            "para_que": "Se utiliza para clasificar información en categorías, especialmente cuando se requiere obtener probabilidades.",
            "como_funciona": "Analiza la relación entre las variables de entrada y la categoría objetivo. Utiliza una función logística para calcular probabilidades y asignar una clase.",
            "ejemplo": "Un banco puede estimar la probabilidad de que un cliente incumpla sus obligaciones crediticias."
        },
        "Árbol de Decisión para Clasificación": {
            "que_es": "Es un algoritmo supervisado que organiza las decisiones en una estructura de árbol.",
            "para_que": "Permite clasificar registros en diferentes categorías y facilita la interpretación de las decisiones.",
            "como_funciona": "Divide los datos mediante preguntas o condiciones sobre sus características. Cada división conduce a una nueva rama hasta llegar a una categoría final.",
            "ejemplo": "Una institución financiera puede clasificar solicitudes de crédito como aprobadas o rechazadas según diferentes características del solicitante."
        },
        "Random Forest para Clasificación": {
            "que_es": "Es un algoritmo de aprendizaje supervisado que combina múltiples árboles de decisión.",
            "para_que": "Se utiliza para clasificar datos y mejorar la estabilidad de las predicciones mediante la combinación de varios árboles.",
            "como_funciona": "Construye diferentes árboles utilizando muestras y subconjuntos de variables. Posteriormente, combina sus predicciones mediante votación para determinar la categoría final.",
            "ejemplo": "Puede utilizarse para clasificar transacciones bancarias como legítimas o fraudulentas."
        },
        "Gradient Boosting para Clasificación": {
            "que_es": "Es un método de aprendizaje supervisado que construye modelos secuenciales para mejorar progresivamente las predicciones.",
            "para_que": "Se utiliza en problemas de clasificación donde se buscan patrones complejos y un buen desempeño predictivo.",
            "como_funciona": "Construye árboles de decisión de manera secuencial. Cada nuevo árbol intenta corregir los errores cometidos por los modelos anteriores.",
            "ejemplo": "Una empresa puede utilizarlo para identificar clientes con alta probabilidad de abandonar un servicio."
        }
    },

    "📈 Modelos de regresión": {
        "Regresión Lineal": {
            "que_es": "Es un algoritmo supervisado que modela la relación entre una o varias variables independientes y una variable numérica.",
            "para_que": "Se utiliza para estimar valores continuos y analizar relaciones aproximadamente lineales entre variables.",
            "como_funciona": "Calcula una ecuación matemática que representa la relación entre las variables, buscando minimizar las diferencias entre los valores reales y los estimados.",
            "ejemplo": "Puede utilizarse para estimar el precio de una vivienda según su área, ubicación y número de habitaciones."
        },
        "Árbol de Decisión para Regresión": {
            "que_es": "Es un algoritmo supervisado que utiliza una estructura de árbol para predecir valores numéricos.",
            "para_que": "Permite realizar predicciones numéricas cuando las relaciones entre las variables pueden ser complejas.",
            "como_funciona": "Divide los datos en grupos mediante condiciones sobre sus características. En cada grupo se obtiene una predicción numérica, generalmente basada en el promedio de los valores de entrenamiento.",
            "ejemplo": "Puede estimar el valor de un vehículo según su antigüedad, kilometraje y características."
        },
        "Random Forest para Regresión": {
            "que_es": "Es un algoritmo que combina múltiples árboles de decisión para realizar predicciones numéricas.",
            "para_que": "Se utiliza para estimar valores continuos y capturar relaciones complejas entre variables.",
            "como_funciona": "Construye varios árboles con diferentes muestras de los datos y combina sus predicciones, generalmente mediante un promedio.",
            "ejemplo": "Una empresa puede estimar sus ventas futuras utilizando información histórica, temporadas y comportamiento de sus clientes."
        },
        "Gradient Boosting para Regresión": {
            "que_es": "Es un método de aprendizaje supervisado que combina árboles de decisión de manera secuencial para predecir valores numéricos.",
            "para_que": "Se utiliza cuando se necesitan capturar patrones complejos y mejorar progresivamente las predicciones.",
            "como_funciona": "Construye árboles de forma secuencial. Cada nuevo árbol aprende a corregir parte de los errores residuales de los anteriores.",
            "ejemplo": "Puede utilizarse para predecir la demanda de productos en función de las ventas anteriores, temporadas y condiciones del mercado."
        }
    },

    "🔗 Modelos de clustering": {
        "K-Means": {
            "que_es": "Es un algoritmo de aprendizaje no supervisado que agrupa observaciones según su similitud.",
            "para_que": "Se utiliza para descubrir grupos de datos cuando no existen categorías previamente definidas.",
            "como_funciona": "El usuario establece el número de grupos. El algoritmo asigna cada observación al centroide más cercano y actualiza los centroides iterativamente hasta estabilizar las agrupaciones.",
            "ejemplo": "Una empresa puede segmentar clientes según sus hábitos de compra, frecuencia de consumo y valor de sus transacciones."
        },
        "DBSCAN": {
            "que_es": "Es un algoritmo de aprendizaje no supervisado que identifica agrupaciones mediante la densidad de los datos.",
            "para_que": "Se utiliza para descubrir grupos de diferentes formas y detectar observaciones que no pertenecen a ninguna agrupación.",
            "como_funciona": "Identifica regiones con suficientes puntos cercanos entre sí, utilizando una distancia y un número mínimo de vecinos. Los puntos aislados pueden clasificarse como ruido.",
            "ejemplo": "Puede identificar zonas geográficas con concentraciones de clientes y detectar ubicaciones aisladas."
        }
    },

    "🔍 Modelos de detección de anomalías": {
        "Isolation Forest": {
            "que_es": "Es un algoritmo diseñado para identificar observaciones que presentan comportamientos diferentes al resto de los datos.",
            "para_que": "Se utiliza para detectar posibles fraudes, fallos, comportamientos inusuales y registros atípicos.",
            "como_funciona": "Construye árboles que separan aleatoriamente los datos. Las observaciones anómalas suelen aislarse mediante menos divisiones que las observaciones normales.",
            "ejemplo": "Una entidad financiera puede identificar transacciones que presentan comportamientos inusuales respecto al historial de operaciones."
        },
        "One-Class SVM": {
            "que_es": "Es un algoritmo de aprendizaje automático que aprende a representar la región donde se encuentran las observaciones consideradas normales.",
            "para_que": "Se utiliza para detectar observaciones que se alejan del comportamiento habitual de los datos.",
            "como_funciona": "Aprende una frontera que delimita la región de los datos normales. Las observaciones que quedan fuera de esa región pueden identificarse como anomalías.",
            "ejemplo": "Puede utilizarse para detectar comportamientos inusuales en sensores industriales o sistemas de monitoreo."
        }
    }
}

# Etiquetas visibles para las opciones del formulario.
# El valor interno (clave) es el que usa la base de conocimiento.
opciones_objetivo = {
    "Clasificacion": "Clasificación",
    "Regresion": "Regresión",
    "Clustering": "Clustering",
    "Anomalias": "Detección de anomalías",
}

opciones_etiquetas = {
    "Etiquetados": "Etiquetados",
    "NoEtiquetados": "No etiquetados",
}

opciones_relaciones = {
    "Lineales": "Lineales",
    "Complejas": "Complejas",
}

opciones_grupos = {
    "Compactos": "Compactos",
    "DensidadesVariables": "Densidades variables",
}


# Textos que aparecen al pasar el cursor por el ícono de ayuda de cada campo.
ayudas = {
    "objetivo": (
        "Clasificación: predecir categorías (¿un correo es spam o no?).  \n"
        "Regresión: predecir un valor numérico (precio de una vivienda).  \n"
        "Clustering: agrupar datos similares sin categorías previas.  \n"
        "Detección de anomalías: encontrar datos con comportamiento inusual."
    ),
    "etiquetas": (
        "Etiquetados: cada registro tiene una categoría o resultado conocido "
        "(transacciones marcadas como fraude o legítimas).  \n"
        "No etiquetados: los datos no tienen esa categoría asignada "
        "(clientes sin clasificación previa)."
    ),
    "relaciones": (
        "Lineales: una variable cambia de forma aproximadamente proporcional "
        "con otra (más horas trabajadas, más salario).  \n"
        "Complejas: hay interacciones que no siguen una línea recta "
        "(la compra depende de edad, ingresos y hábitos a la vez)."
    ),
    "grupos": (
        "Compactos: los elementos de cada grupo están cerca entre sí y "
        "separados de otros grupos.  \n"
        "Densidades variables: algunos grupos son densos y otros dispersos "
        "(zonas geográficas con distinta concentración de personas)."
    ),
    "tabulares": (
        "Información organizada en filas y columnas, como una hoja de Excel "
        "o una tabla de base de datos. Ejemplo: clientes con edad, ingresos y ciudad."
    ),
    "escalados": (
        "Los valores de las variables ya se ajustaron a una escala comparable. "
        "Ejemplo: transformar edades e ingresos para que sus magnitudes no "
        "sean tan distintas."
    ),
    "interpretabilidad": (
        "Necesitas entender qué factores influyen en las decisiones del modelo. "
        "Ejemplo: saber qué características pesan en la aprobación de un crédito."
    ),
    "probabilidades": (
        "Necesitas la probabilidad asociada a cada predicción. Ejemplo: "
        "un cliente tiene 85 % de probabilidad de incumplir un pago."
    ),
    "requiere_etiquetas": (
        "El modelo necesita ejemplos con respuestas conocidas para aprender. "
        "Ejemplo: para detectar fraudes se necesitan transacciones ya marcadas "
        "como fraudulentas o legítimas."
    ),
    "escenario": "Carga valores de ejemplo en el formulario para probar el sistema rápido.",
}


# Escenarios de demostración (los mismos de la versión original,
# con el valor de grupos corregido a "DensidadesVariables").
escenarios = {
    "Clasificación": {
        "objetivo": "Clasificacion", "etiquetas": "Etiquetados", "tabulares": True,
        "relaciones": "Complejas", "interpretabilidad": False, "probabilidades": False,
        "requiere_etiquetas": True, "grupos": "Compactos", "escalados": False,
    },
    "Regresión": {
        "objetivo": "Regresion", "etiquetas": "Etiquetados", "tabulares": True,
        "relaciones": "Lineales", "interpretabilidad": True, "probabilidades": False,
        "requiere_etiquetas": True, "grupos": "Compactos", "escalados": False,
    },
    "Clustering": {
        "objetivo": "Clustering", "etiquetas": "NoEtiquetados", "tabulares": True,
        "relaciones": "Complejas", "interpretabilidad": False, "probabilidades": False,
        "requiere_etiquetas": False, "grupos": "Compactos", "escalados": True,
    },
    "Detección de anomalías": {
        "objetivo": "Anomalias", "etiquetas": "NoEtiquetados", "tabulares": True,
        "relaciones": "Complejas", "interpretabilidad": False, "probabilidades": False,
        "requiere_etiquetas": False, "grupos": "DensidadesVariables", "escalados": True,
    },
}


# Pasos del proceso, usados en la guía y en el menú "¿Cómo funciona?".
pasos = [
    ("📝", "Describes tu problema",
     "Indicas el objetivo, cómo son tus datos y qué esperas del modelo."),
    ("🧠", "El motor aplica las reglas",
     "Se evalúan las 15 reglas de la base de conocimiento con encadenamiento hacia adelante."),
    ("🎯", "Recibes recomendaciones",
     "Ves los modelos sugeridos y qué condiciones justificaron cada uno."),
]


def buscar_info_modelo(nombre_visible):
    """Devuelve la ficha de la biblioteca para un modelo, o None."""
    for modelos in biblioteca_modelos.values():
        if nombre_visible in modelos:
            return modelos[nombre_visible]
    return None
