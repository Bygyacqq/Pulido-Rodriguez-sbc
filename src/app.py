import streamlit as st

from estilos import aplicar_estilos

st.set_page_config(
    page_title="Sistema Experto de Machine Learning",
    page_icon="🤖",
    layout="wide",
)

aplicar_estilos()

# El diagnóstico es la página por defecto; la guía queda en el menú de arriba.
diagnostico = st.Page("vistas/diagnostico.py", title="Diagnóstico", icon="🎯", default=True)
guia = st.Page("vistas/guia.py", title="Guía y conceptos", icon="📖")

pagina = st.navigation([diagnostico, guia], position="top")
pagina.run()
