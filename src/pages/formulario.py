import streamlit as st

from base_conocimiento import crear_base_conocimiento

import io
from contextlib import redirect_stdout
from motor_inferencia import (
    encadenamiento_hacia_adelante,
    explicar_razonamiento,
    porque
)

# Configuración de la página
st.set_page_config(
    page_title="Sistema Experto de Machine Learning",
    page_icon="🤖",
    layout="wide"
)

# Ocultar navegación lateral
st.set_option("client.showSidebarNavigation", False)


# Diseño visual del formulario

st.markdown("""

<style>

/* ==================================================
   1. CONFIGURACIÓN GENERAL
================================================== */

[data-testid="stSidebar"],
[data-testid="collapsedControl"] {
    display: none;
}

.block-container {
    max-width: 1250px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, rgba(22,119,210,.15), transparent 38%),
        radial-gradient(ellipse at 90% 35%, rgba(128,87,216,.12), transparent 35%),
        linear-gradient(135deg, #080F1E, #0B1425 55%, #10182B);
    color: #E8F0FC;
}


/* ==================================================
   2. TIPOGRAFÍA - MODO OSCURO
================================================== */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #F0F6FF !important;
}

.stApp p,
.stApp li,
.stApp label {
    color: #C5D3E8;
}

[data-testid="stCaptionContainer"] {
    color: #AFC1D9 !important;
}


/* ==================================================
   3. ENCABEZADO PRINCIPAL
================================================== */

.form-hero {
    background:
        radial-gradient(circle at 90% 20%, rgba(45,190,255,.22), transparent 30%),
        linear-gradient(115deg, #102846, #174E83);
    border: 1px solid rgba(94,190,255,.3);
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 25px;
    box-shadow: 0 12px 35px rgba(0,0,0,.2);
}

.form-hero .eyebrow {
    color: #7DE3FF;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.form-hero h1 {
    color: #FFFFFF !important;
    font-size: 34px;
    margin: 12px 0;
}

.form-hero p {
    color: #D6E9FC !important;
    font-size: 15px;
}


/* ==================================================
   4. FORMULARIO
================================================== */

[data-testid="stForm"] {
    background: rgba(17,31,52,.78);
    border: 1px solid rgba(93,153,210,.3);
    border-radius: 18px;
    padding: 25px;
}

/* Etiquetas de campos */

div[data-testid="stSelectbox"] label,
div[data-testid="stCheckbox"] label {
    color: #E5F1FF !important;
    font-weight: 600;
}

/* Selectores */

div[data-testid="stSelectbox"] > div > div {
    background-color: #14243B;
    border-color: #345578;
    border-radius: 9px;
}

/* Casillas */

div[data-testid="stCheckbox"] {
    background: rgba(24,45,72,.55);
    padding: 9px 12px;
    border-radius: 9px;
    margin: 5px 0;
}

/* Menús desplegables */

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #14243B !important;
}

[data-baseweb="menu"] li,
[data-baseweb="option"] {
    color: #FFFFFF !important;
}


/* ==================================================
   5. MENSAJES INFORMATIVOS
   FONDO CLARO Y TEXTO OSCURO EN AMBOS TEMAS
================================================== */


.stApp [data-testid="stAlert"] {
    background-color: #1B2B43 !important;
    border: 1px solid #52769F !important;
    border-radius: 12px !important;
}

/* Texto de las alertas */
.stApp [data-testid="stAlert"] p,
.stApp [data-testid="stAlert"] span,
.stApp [data-testid="stAlert"] div {
    color: #E8F0FC !important;
    opacity: 1 !important;
}


/* ==================================================
   6. BOTONES
================================================== */

.stButton button,
.stFormSubmitButton button {
    background: linear-gradient(100deg, #1677D2, #6855D9);
    color: #FFFFFF !important;
    border: 1px solid rgba(120,190,255,.35);
    border-radius: 10px;
    font-weight: 700;
    padding: 11px 20px;
    transition: all .25s ease;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    background: linear-gradient(100deg, #218FEA, #8068EB);
    border-color: #73D8FF;
    box-shadow: 0 5px 20px rgba(38,143,230,.3);
}


/* ==================================================
   7. TARJETAS DE RESULTADOS
================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(18,34,56,.7);
    border: 1px solid rgba(93,153,210,.3);
    border-radius: 14px;
}


/* ==================================================
   8. SEPARADORES
================================================== */

hr {
    border-color: rgba(112,157,205,.25);
    margin: 25px 0;
}


/* ==================================================
   9. MODO CLARO
================================================== */

html[data-theme="light"] .stApp {
    background: linear-gradient(135deg, #F0F5FC, #E7EFFA) !important;
    color: #17365D !important;
}

/* Textos generales */

html[data-theme="light"] .stApp h1,
html[data-theme="light"] .stApp h2,
html[data-theme="light"] .stApp h3,
html[data-theme="light"] .stApp h4 {
    color: #17365D !important;
}

html[data-theme="light"] .stApp p,
html[data-theme="light"] .stApp li,
html[data-theme="light"] .stApp label {
    color: #344B68;
}

html[data-theme="light"] [data-testid="stCaptionContainer"] {
    color: #526781 !important;
}

/* Formulario */

html[data-theme="light"] [data-testid="stForm"] {
    background: #FFFFFF;
    border-color: #C9D9EC;
}

html[data-theme="light"] div[data-testid="stSelectbox"] label,
html[data-theme="light"] div[data-testid="stCheckbox"] label {
    color: #17365D !important;
}

html[data-theme="light"] div[data-testid="stSelectbox"] > div > div {
    background: #FFFFFF;
    border-color: #B9CBE0;
}

html[data-theme="light"] div[data-testid="stCheckbox"] {
    background: #EDF3FA;
}

/* Opciones desplegables */

html[data-theme="light"] [data-baseweb="popover"],
html[data-theme="light"] [data-baseweb="menu"] {
    background: #FFFFFF !important;
}

html[data-theme="light"] [data-baseweb="menu"] li,
html[data-theme="light"] [data-baseweb="option"] {
    color: #17365D !important;
}

/* Tarjetas */

html[data-theme="light"] div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border-color: #C9D9EC;
}

/* Los mensajes informativos conservan su estilo
   claro y texto oscuro en ambos temas */


/* ==================================================
   10. DISEÑO RESPONSIVE
================================================== */

@media (max-width: 768px) {

    .form-hero {
        padding: 23px;
    }

    .form-hero h1 {
        font-size: 27px;
    }

    [data-testid="stForm"] {
        padding: 14px;
    }

    .block-container {
        padding-top: 1.5rem;
    }
}

</style>
""", unsafe_allow_html=True)




# Cargar base de conocimiento
base_conocimiento = crear_base_conocimiento()
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

# Título

# Encabezado del formulario
st.html("""
<div class="form-hero">
    <div class="eyebrow">INTELIGENCIA ARTIFICIAL · DIAGNÓSTICO</div>
    <h1>🧠 Analicemos tu problema</h1>
    <p>
        Describe las características de tus datos y los objetivos
        de tu análisis. El sistema experto evaluará las condiciones
        y recomendará los modelos de Machine Learning más adecuados.
    </p>
</div>
""")


st.success(f"Base de conocimiento cargada: {len(base_conocimiento)} reglas")
def aplicar_caso():
    casos = {
        "Clasificación": {
            "objetivo": "Clasificacion",
            "etiquetas": "Etiquetados",
            "tabulares": True,
            "relaciones": "Complejas",
            "interpretabilidad": False,
            "probabilidades": False,
            "requiere_etiquetas": True,
            "grupos": "Compactos",
            "escalados": False
        },
        "Regresión": {
            "objetivo": "Regresion",
            "etiquetas": "Etiquetados",
            "tabulares": True,
            "relaciones": "Lineales",
            "interpretabilidad": True,
            "probabilidades": False,
            "requiere_etiquetas": True,
            "grupos": "Compactos",
            "escalados": False
        },
        "Clustering": {
            "objetivo": "Clustering",
            "etiquetas": "NoEtiquetados",
            "tabulares": True,
            "relaciones": "Complejas",
            "interpretabilidad": False,
            "probabilidades": False,
            "requiere_etiquetas": False,
            "grupos": "Compactos",
            "escalados": True
        },
        "Detección de anomalías": {
            "objetivo": "Anomalias",
            "etiquetas": "NoEtiquetados",
            "tabulares": True,
            "relaciones": "Complejas",
            "interpretabilidad": False,
            "probabilidades": False,
            "requiere_etiquetas": False,
            "grupos": "DensidadesVariables",
            "escalados": True
        },
    }

    caso = st.session_state["caso_prueba"]

    if caso in casos:
        datos = casos[caso]

        for campo, valor in datos.items():
            st.session_state[campo] = valor
# Formulario de entrada
st.header("Características del problema")
caso_prueba = st.selectbox(
    "Selecciona un escenario de demostración:",
    [
        "Personalizado",
        "Clasificación",
        "Regresión",
        "Clustering",
        "Detección de anomalías"
    ],
    key="caso_prueba",
    on_change=aplicar_caso
)

with st.form("formulario_problema"):

    # 1. Objetivo del problema
    st.subheader("🎯 1. Objetivo del problema")
    st.caption("Selecciona qué deseas lograr con el análisis de tus datos.")

    objetivo = st.selectbox(
        "¿Cuál es el objetivo del problema?",
        ["Clasificacion", "Regresion", "Clustering", "Anomalias"],
        key="objetivo"
    )

    # 2. Características de los datos
    st.divider()
    st.subheader("📊 2. Características de los datos")
    st.caption("Describe la estructura y las características de la información.")

    estado_etiquetas = st.selectbox(
        "¿Cómo se encuentran las etiquetas de los datos?",
        ["Etiquetados", "NoEtiquetados"],
        key="etiquetas"
    )

    datos_tabulares = st.checkbox(
        "Los datos tienen estructura tabular",
        key="tabulares"
    )

    relaciones = st.selectbox(
        "¿Qué tipo de relaciones existen entre los datos?",
        ["Lineales", "Complejas"],
        key="relaciones"
    )

    estructura_grupos = st.selectbox(
        "¿Cómo se distribuyen los grupos?",
        ["Compactos", "Densidades Variables"],
        key="grupos"
    )

    datos_escalados = st.checkbox(
        "Los datos están escalados",
        key="escalados"
    )

    # 3. Requerimientos del análisis
    st.divider()
    st.subheader("⚙️ 3. Requerimientos del análisis")
    st.caption("Indica qué características esperas del modelo recomendado.")

    requiere_interpretabilidad = st.checkbox(
        "Se requiere interpretabilidad",
        key="interpretabilidad"
    )

    requiere_probabilidades = st.checkbox(
        "Se requiere obtener probabilidades",
        key="probabilidades"
    )

    requiere_etiquetas = st.checkbox(
        "El problema requiere etiquetas",
        key="requiere_etiquetas"
    )

    # Botón de envío
    ejecutar = st.form_submit_button("Generar recomendaciones")
st.caption(
    "Indica si tus datos cuentan con resultados o categorías previamente conocidos."
)

if estado_etiquetas == "Etiquetados":
    st.info(
        "Etiquetados: Cada registro cuenta con una categoría o resultado conocido. "
        "Ejemplo: Transacciones identificadas como fraudulentas o legítimas."
    )

else:
    st.info(
        "No etiquetados: Los datos no tienen categorías o resultados previamente "
        "asignados. Ejemplo: Un conjunto de clientes sin clasificación previa."
    )

if st.button("Limpiar formulario y resultados"):
        st.session_state.clear()
        st.rerun()
if objetivo == "Clasificacion":
    st.info("Clasificación: Permite predecir categorías. Ejemplo: Determinar si un correo es spam o no.")

elif objetivo == "Regresion":
    st.info("Regresión: Permite predecir valores numéricos. Ejemplo: Estimar el precio de una vivienda.")

elif objetivo == "Clustering":
    st.info("Clustering: Permite agrupar datos similares sin categorías previamente definidas.")

elif objetivo == "Anomalias":
    st.info("Detección de anomalías: permite identificar datos que presentan comportamientos inusuales.")

st.caption(
    "Indica cómo se relacionan las variables dentro de tu conjunto de datos."
)

if relaciones == "Lineales":
    st.info(
        "Relaciones lineales: Los cambios en una variable se relacionan "
        "de manera aproximadamente proporcional con otra. "
        "Ejemplo: A mayor cantidad de horas trabajadas, mayor salario."
    )

else:
    st.info(
        "Relaciones Complejas: existen patrones o interacciones entre "
        "variables que no siguen una relación lineal sencilla. "
        "Ejemplo: El comportamiento de compra de un cliente puede "
        "depender de su edad, ingresos y hábitos."
    )
st.caption(
    "Describe cómo se agrupan o distribuyen los datos dentro del conjunto."
)

if estructura_grupos == "Compactos":
    st.info(
        "Grupos compactos: Los elementos de cada grupo se encuentran "
        "cerca unos de otros y separados de otros grupos. "
        "Ejemplo: Clientes agrupados según características similares."
    )

else:
    st.info(
        "Densidades variables: Los grupos presentan diferentes "
        "concentraciones de datos. Algunos pueden ser densos y otros "
        "más dispersos. Ejemplo: Agrupaciones geográficas con "
        "diferentes concentraciones de personas."
    )
    st.caption(
    "Indica si tu información está organizada en filas y columnas."
)

    st.info(
    "Datos tabulares: Información organizada en registros y campos, "
    "como una hoja de Excel o una tabla de una base de datos. "
    "Ejemplo: Una tabla de clientes con edad, ingresos y ciudad."
)
    st.markdown("**Ejemplo de datos tabulares:**")

    ejemplo_datos = {
    "Edad": [25, 32, 28],
    "Ingresos": [2000000, 3500000, 2800000],
    "Ciudad": ["Bogotá", "Cali", "Medellín"]
}

    st.dataframe(
    ejemplo_datos,
    use_container_width=True,
    hide_index=True
)
    st.caption(
    "Indica si los valores de tus variables ya fueron transformados "
    "para trabajar en una escala comparable."
)

st.info(
    "Datos escalados: Significa que los valores de las variables "
    "han sido ajustados a una escala determinada. "
    "Ejemplo: Transformar edades e ingresos para que sus magnitudes "
    "no tengan diferencias excesivas."
)

st.caption(
    "Indica si necesitas comprender cómo el modelo llega a sus predicciones."
)

st.info(
    "Interpretabilidad: Permite entender qué factores influyen "
    "en las decisiones del modelo. "
    "Ejemplo: En una evaluación crediticia, identificar qué "
    "características influyen en la aprobación de un préstamo."
)
st.caption(
    "Indica si necesitas conocer la probabilidad asociada a cada predicción."
)

st.info(
    "Probabilidades: Representan el nivel de posibilidad de que ocurra "
    "un resultado. Ejemplo: Un modelo que estima que un cliente tiene "
    "un 85 % de probabilidad de incumplir un pago."
)
st.caption(
    "Indica si el problema necesita datos con categorías o resultados conocidos "
    "para entrenar el modelo."
)

st.info(
    "Necesidad de etiquetas: Algunos modelos requieren ejemplos con "
    "respuestas conocidas para aprender a realizar predicciones. "
    "Ejemplo: para entrenar un modelo que detecte fraudes, se necesitan "
    "transacciones identificadas previamente como fraudulentas o legítimas."
)

# Procesar información del formulario
if ejecutar:

    hechos_iniciales = set()

    # Objetivo del problema
    hechos_iniciales.add(
        ("Objetivo", "problema", objetivo)
    )

    # Estado de las etiquetas
    hechos_iniciales.add(
        ("EstadoEtiquetas", "problema", estado_etiquetas)
    )

    # Características de los datos
    if datos_tabulares:
        hechos_iniciales.add(
            ("DatosTabulares", "problema")
        )
    
    hechos_iniciales.add(
        ("Relaciones", "problema", relaciones)
    )

    # Requerimientos
    if requiere_interpretabilidad:
        hechos_iniciales.add(
            ("RequiereInterpretabilidad", "problema")
        )

    if requiere_probabilidades:
        hechos_iniciales.add(
            ("RequiereProbabilidades", "problema")
        )

    if requiere_etiquetas:
        hechos_iniciales.add(
            ("RequiereEtiquetas", "problema")
        )

    # Características adicionales
    hechos_iniciales.add(
        ("EstructuraGrupos", "problema", estructura_grupos)
    )

    if datos_escalados:
        hechos_iniciales.add(
            ("DatosEscalados", "problema")
        )

    # Ejecutar motor de inferencia
    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        base_conocimiento
    )

    st.session_state["hechos_finales"] = hechos_finales
    st.session_state["reglas_aplicadas"] = reglas_aplicadas

    st.success("Análisis realizado correctamente.")
modelos = []
reglas_aplicadas = []


# Mostrar resultados
if "hechos_finales" in st.session_state:

    st.header("Resultados del análisis")

    hechos_finales = st.session_state["hechos_finales"]

    # Extraer modelos recomendados
    modelos = [
        hecho[2]
        for hecho in hechos_finales
        if hecho[0] == "RecomendarModelo"
    ]

    if modelos:
        st.subheader("Modelos recomendados")

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

        for indice, modelo in enumerate(modelos, start=1):

            nombre = nombres_modelos.get(modelo, modelo)

            descripcion = descripciones_modelos.get(
                modelo,
                "Modelo recomendado según las características ingresadas."
            )

            with st.container(border=True):
                st.markdown(f"### {indice}. {nombre}")
                st.write(descripcion)
                st.caption("Modelo identificado por el sistema experto")
                    # Gráfico de rendimiento demostrativo
        st.divider()

        st.subheader("📊 Rendimiento demostrativo de los modelos")

        st.caption(
            "Los siguientes porcentajes son valores simulados con fines "
            "educativos. No representan resultados de evaluaciones reales."
        )

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

        datos_grafico = {
            nombres_modelos.get(modelo, modelo):
            rendimiento_modelos.get(modelo, 80)
            for modelo in modelos
        }
        mejor_modelo = max(
            modelos,
            key=lambda modelo: rendimiento_modelos.get(modelo, 80)
        )

        nombre_mejor = nombres_modelos.get(mejor_modelo, mejor_modelo)
        porcentaje_mejor = rendimiento_modelos.get(mejor_modelo, 80)

        with st.container(border=True):
            st.markdown("### 🏆 Modelo destacado")
            st.markdown(f"**{nombre_mejor}**")
            st.metric(
                label="Rendimiento demostrativo",
                value=f"{porcentaje_mejor}%"
            )
        st.bar_chart(
            datos_grafico,
            horizontal=True,
            x_label="Modelo",
            y_label="Rendimiento demostrativo (%)"
        )

    else:
        st.warning(
            "No se encontraron recomendaciones para las características ingresadas."
        )


    # Mostrar advertencias
st.subheader("Reglas utilizadas")

for regla in reglas_aplicadas:

    with st.expander(f"{regla['id']} - {regla['descripcion']}"):

        # Obtener la conclusión de la regla
        conclusion = regla["conclusion"]

        st.write("**Conclusión:**")

        if conclusion[0] == "RecomendarModelo":

            nombre_conclusion = nombres_modelos.get(
                conclusion[2],
                conclusion[2]
            )

            st.write(f"Recomendar modelo: {nombre_conclusion}")

        elif conclusion[0] == "ModeloSupervisado":

            st.write("Se requiere un modelo supervisado.")

        elif conclusion[0] == "AdvertenciaDatosNoEtiquetados":

            st.write(
                "Los datos necesitan etiquetas para aplicar modelos supervisados."
            )

        st.write("**Condiciones necesarias:**")

        for condicion in regla["condiciones"]:

            predicado = condicion[0]

            descripcion = descripciones_predicados.get(
                predicado,
                predicado
            )

            if len(condicion) == 3:

                valor = valores_legibles.get(
                    condicion[2],
                    condicion[2]
                )

                st.write(f"- {descripcion}: {valor}")

            else:

                st.write(f"- {descripcion}")

# Explicación de las recomendaciones


st.header("¿Por qué se recomienda este modelo?")

if modelos:

    modelo_seleccionado = st.selectbox(
        "Selecciona un modelo para consultar su explicación:",
        modelos,
        format_func=lambda modelo: nombres_modelos.get(modelo, modelo)
    )

    reglas_aplicadas = st.session_state["reglas_aplicadas"]

    conclusion_consultada = (
        "RecomendarModelo",
        "problema",
        modelo_seleccionado
    )

    reglas_responsables = [
        regla for regla in reglas_aplicadas
        if regla["conclusion"] == conclusion_consultada
    ]

    if reglas_responsables:

        nombre_modelo = nombres_modelos.get(
            modelo_seleccionado,
            modelo_seleccionado
        )

        st.info(f"Explicación de la recomendación: {nombre_modelo}")

        for regla in reglas_responsables:

            with st.container(border=True):

                st.markdown(f"**{regla['id']} - Criterio aplicado**")

                st.write(regla["descripcion"])

                st.markdown("**Características que justifican la recomendación:**")

                for condicion in regla["condiciones"]:

                    predicado = condicion[0]

                    descripcion = descripciones_predicados.get(
                        predicado,
                        predicado
                    )

                    if len(condicion) == 3:

                        valor = valores_legibles.get(
                            condicion[2],
                            condicion[2]
                        )

                        st.write(f"- {descripcion}: {valor}")

                    else:

                        st.write(f"- {descripcion}")

    else:
        st.warning("No se encontró una explicación para este modelo.")

else:
    st.info("Primero debes generar recomendaciones para consultar sus explicaciones.")
