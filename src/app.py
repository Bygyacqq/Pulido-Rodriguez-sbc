
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Sistema Experto de Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.set_option("client.showSidebarNavigation", False)

# --------------------------------------------------
# DISEÑO VISUAL
# --------------------------------------------------

st.markdown("""
<style>

/* Fondo general */
.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, rgba(22, 119, 210, 0.16), transparent 38%),
        radial-gradient(ellipse at 90% 35%, rgba(128, 87, 216, 0.13), transparent 35%),
        linear-gradient(135deg, #080F1E 0%, #0B1425 50%, #10182B 100%);
    color: #E8F0FC;
}

/* Ocultar navegación lateral */
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* Área principal */
.block-container {
    max-width: 1450px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Textos generales */
h1, h2, h3, h4 {
    color: #F0F6FF !important;
}

p, li, label {
    color: #C5D3E8;
}

/* Encabezado principal */
.hero {
    position: relative;
    overflow: hidden;
    padding: 48px 45px;
    border-radius: 22px;
    margin-bottom: 35px;
    background:
        radial-gradient(circle at 85% 20%, rgba(45, 190, 255, 0.28), transparent 30%),
        linear-gradient(115deg, #102846 0%, #123D68 55%, #174E83 100%);
    border: 1px solid rgba(94, 190, 255, 0.28);
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.25);
}

.hero::after {
    content: "";
    position: absolute;
    width: 320px;
    height: 320px;
    right: -90px;
    top: -130px;
    border: 1px solid rgba(100, 210, 255, 0.28);
    border-radius: 50%;
    box-shadow:
        0 0 0 35px rgba(100, 210, 255, 0.04),
        0 0 0 75px rgba(100, 210, 255, 0.035);
}

.hero-label {
    color: #7DE3FF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.hero h1 {
    color: white !important;
    font-size: clamp(30px, 4vw, 45px);
    font-weight: 800;
    margin-bottom: 15px;
    line-height: 1.2;
}

.hero p {
    color: #D6E9FC;
    font-size: 16px;
    max-width: 760px;
    line-height: 1.8;
}

/* Secciones */
.section-label {
    color: #55C8F0;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 7px;
}

.section-description {
    color: #AFC1D9;
    font-size: 15px;
    margin-bottom: 20px;
}

/* Tarjetas */
.feature-card {
    background: linear-gradient(145deg, #14243B, #101D32);
    border: 1px solid rgba(93, 153, 210, 0.25);
    border-radius: 16px;
    padding: 25px 22px;
    min-height: 205px;
    height: 100%;
    transition: all 0.25s ease;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16);
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(72, 196, 255, 0.7);
    box-shadow: 0 12px 30px rgba(20, 130, 220, 0.16);
}

.card-number {
    color: #5CCBFA;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 15px;
}

.card-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.feature-card h3 {
    color: #F0F6FF !important;
    font-size: 19px;
    margin-bottom: 10px;
}

.feature-card p {
    color: #B9C9DE;
    font-size: 14px;
    line-height: 1.7;
}

/* Diccionario */
div[data-testid="stExpander"] {
    background: rgba(18, 34, 56, 0.78);
    border: 1px solid rgba(93, 153, 210, 0.24);
    border-radius: 12px;
    margin-bottom: 10px;
}

div[data-testid="stExpander"] summary {
    color: #EAF4FF;
}

/* Separadores */
hr {
    border-color: rgba(112, 157, 205, 0.22);
    margin-top: 32px;
    margin-bottom: 32px;
}

/* Botones */
.stButton button {
    background: linear-gradient(100deg, #1677D2, #6855D9);
    color: white !important;
    border: 1px solid rgba(120, 190, 255, 0.35);
    border-radius: 10px;
    padding: 13px 25px;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton button:hover {
    background: linear-gradient(100deg, #218FEA, #8068EB);
    border-color: #73D8FF;
    box-shadow: 0 5px 22px rgba(38, 143, 230, 0.3);
    transform: translateY(-2px);
}

/* Pie de página */
.footer {
    text-align: center;
    color: #8196B2;
    font-size: 12px;
    padding: 25px 0 5px 0;
}

/* Ajustes para pantallas pequeñas */
@media (max-width: 768px) {
    .hero {
        padding: 30px 23px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .block-container {
        padding-top: 1.5rem;
    }
}
html[data-theme="light"] div[data-testid="stExpander"] summary {
    color: #17365D;
}

/* Mensajes informativos */
html[data-theme="light"] div[data-testid="stAlert"] {
    background: #E8F2FC;
    border-color: #B8D4F0;
    color: #17365D;
}

/* Textos auxiliares */
html[data-theme="light"] [data-testid="stCaptionContainer"] {
    color: #526781;
}

/* Separadores */
html[data-theme="light"] hr {
    border-color: #C9D9EC;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENCABEZADO PRINCIPAL
# --------------------------------------------------

st.html("""
<div class="hero">
    <div class="hero-label">INTELIGENCIA ARTIFICIAL · MACHINE LEARNING</div>

    <h1>🤖 Sistema Experto de<br>Machine Learning</h1>

    <p>
        Una herramienta inteligente para orientar la selección de modelos
        de aprendizaje automático mediante reglas de conocimiento e
        inferencia lógica.
    </p>
</div>
""")

# --------------------------------------------------
# BIENVENIDA
# --------------------------------------------------

st.markdown('<div class="section-label">BIENVENIDA</div>',
            unsafe_allow_html=True)

st.markdown("## Descubre el modelo adecuado para tu problema")

st.markdown("""
<div class="section-description">
Esta aplicación utiliza un sistema experto basado en reglas de conocimiento
e inferencia lógica para recomendar modelos de Machine Learning según
las características de un problema.
</div>
""", unsafe_allow_html=True)

st.divider()


# --------------------------------------------------
# OBJETIVO
# --------------------------------------------------

st.markdown('<div class="section-label">PROPÓSITO DEL SISTEMA</div>',
            unsafe_allow_html=True)

st.header("🎯 Objetivo de la aplicación")

st.write("""
Orientar al usuario en la selección de modelos de Machine Learning
mediante el análisis de las características de sus datos, el objetivo
del problema y los requerimientos del análisis.
""")


# --------------------------------------------------
# FUNCIONAMIENTO
# --------------------------------------------------

st.divider()

st.markdown('<div class="section-label">PROCESO DE INFERENCIA</div>',
            unsafe_allow_html=True)

st.header("⚙️ ¿Cómo funciona el sistema?")

st.markdown("""
<div class="section-description">
El sistema experto desarrolla el proceso de recomendación mediante tres etapas:
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="card-number">01</div>
        <div class="card-icon">📝</div>
        <h3>Ingreso de información</h3>
        <p>
            El usuario describe su problema, las características
            de sus datos y sus necesidades.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="card-number">02</div>
        <div class="card-icon">🧠</div>
        <h3>Motor de inferencia</h3>
        <p>
            El sistema analiza la información y aplica las reglas
            de su base de conocimiento.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="card-number">03</div>
        <div class="card-icon">🎯</div>
        <h3>Recomendaciones</h3>
        <p>
            Se presentan los modelos de Machine Learning
            recomendados y la explicación correspondiente.
        </p>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# DICCIONARIO DE CONCEPTOS
# --------------------------------------------------

st.divider()

st.markdown('<div class="section-label">CENTRO DE CONOCIMIENTO</div>',
            unsafe_allow_html=True)

st.header("📖 Diccionario de conceptos")

st.markdown("""
<div class="section-description">
Consulta las siguientes categorías para comprender los conceptos
utilizados en el formulario.
</div>
""", unsafe_allow_html=True)

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

for categoria, conceptos in diccionario.items():

    with st.expander(categoria):

        for concepto, descripcion in conceptos.items():

            st.markdown(f"**{concepto}**")
            st.write(descripcion)
            st.divider()


# --------------------------------------------------
# BIBLIOTECA DE MODELOS DE MACHINE LEARNING
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-label">BIBLIOTECA DE ALGORITMOS</div>',
    unsafe_allow_html=True
)

st.header("🧠 Biblioteca de modelos de Machine Learning")

st.markdown("""
<div class="section-description">
Conoce los algoritmos que utiliza el sistema experto, sus aplicaciones,
su funcionamiento y algunos ejemplos de uso.
</div>
""", unsafe_allow_html=True)

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

for categoria, modelos_categoria in biblioteca_modelos.items():

    st.subheader(categoria)

    for nombre_modelo, informacion in modelos_categoria.items():

        with st.expander(f"📘 {nombre_modelo}"):

            st.markdown("**¿Qué es?**")
            st.write(informacion["que_es"])

            st.markdown("**¿Para qué sirve?**")
            st.write(informacion["para_que"])

            st.markdown("**¿Cómo funciona?**")
            st.write(informacion["como_funciona"])

            st.markdown("**💡 Ejemplo práctico**")
            st.info(informacion["ejemplo"])

# --------------------------------------------------
# LLAMADO A LA ACCIÓN
# --------------------------------------------------

st.divider()

st.markdown('<div class="section-label">COMIENZA TU ANÁLISIS</div>',
            unsafe_allow_html=True)

st.header("🚀 Encuentra modelos adecuados para tu problema")

st.write("""
Completa el formulario y permite que el sistema experto analice
las características de tus datos y tus necesidades.
""")

if st.button(
    "🚀 Comenzar diagnóstico",
    type="primary",
    use_container_width=True
):
    st.switch_page("pages/formulario.py")


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

st.markdown("""
<div class="footer">
    SISTEMA EXPERTO DE MACHINE LEARNING · INTELIGENCIA ARTIFICIAL II
</div>
""", unsafe_allow_html=True)
