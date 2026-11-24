import streamlit as st

from contenido import biblioteca_modelos, diccionario, pasos
from estilos import pasos_html, rejilla, tarjeta

col_titulo, col_accion = st.columns([3, 1], vertical_alignment="bottom")

with col_titulo:
    st.title("🤖 Sistema Experto de Machine Learning")
    st.write(
        "Orienta la selección de modelos de aprendizaje automático a partir "
        "del objetivo de tu problema, las características de tus datos y lo "
        "que necesitas del análisis."
    )

with col_accion:
    if st.button("Ir al diagnóstico", icon="🎯", type="primary", width="stretch"):
        st.switch_page("vistas/diagnostico.py")


# Cómo funciona
st.subheader("⚙️ Cómo funciona")
st.html(pasos_html(pasos))


# Diccionario de conceptos
st.subheader("📖 Diccionario de conceptos")
st.html('<p class="pista">Pasa el cursor sobre un concepto (o tócalo en el celular) para ver qué significa.</p>')

for categoria, conceptos in diccionario.items():
    st.markdown(f"**{categoria}**")
    rejilla(
        [tarjeta(concepto, detalle=[("", definicion)]) for concepto, definicion in conceptos.items()],
        ancho_min=220,
    )


# Biblioteca de modelos
st.subheader("🧠 Biblioteca de modelos")
st.html('<p class="pista">Cada tarjeta muestra qué es el modelo. Al pasar el cursor ves para qué sirve, cómo funciona y un ejemplo.</p>')

for categoria, modelos in biblioteca_modelos.items():
    st.markdown(f"**{categoria}**")
    rejilla(
        [
            tarjeta(
                nombre,
                resumen=info["que_es"],
                detalle=[
                    ("Para qué sirve:", info["para_que"]),
                    ("Cómo funciona:", info["como_funciona"]),
                    ("Ejemplo:", info["ejemplo"]),
                ],
            )
            for nombre, info in modelos.items()
        ],
        ancho_min=300,
    )

st.divider()
if st.button("Ir al diagnóstico", icon="🎯", type="primary", key="ir_final"):
    st.switch_page("vistas/diagnostico.py")
