import pandas as pd
import streamlit as st

from base_conocimiento import crear_base_conocimiento
from contenido import (
    ayudas,
    buscar_info_modelo,
    descripciones_modelos,
    descripciones_predicados,
    escenarios,
    nombres_modelos,
    opciones_etiquetas,
    opciones_grupos,
    opciones_objetivo,
    opciones_relaciones,
    pasos,
    rendimiento_modelos,
    valores_legibles,
)
from estilos import pasos_html, rejilla, tarjeta
from motor_inferencia import encadenamiento_hacia_adelante

base_conocimiento = crear_base_conocimiento()


# --------------------------------------------------
# Funciones de apoyo
# --------------------------------------------------

def aplicar_escenario():
    datos = escenarios.get(st.session_state["caso_prueba"])
    if datos:
        for campo, valor in datos.items():
            st.session_state[campo] = valor


def limpiar():
    st.session_state.clear()


def texto_condicion(condicion):
    descripcion = descripciones_predicados.get(condicion[0], condicion[0])
    if len(condicion) == 3:
        valor = valores_legibles.get(condicion[2], condicion[2])
        return f"{descripcion}: {valor}"
    return descripcion


def texto_conclusion(conclusion):
    if conclusion[0] == "RecomendarModelo":
        return f"Recomendar {nombres_modelos.get(conclusion[2], conclusion[2])}"
    if conclusion[0] == "ModeloSupervisado":
        return "El problema es apto para aprendizaje supervisado"
    if conclusion[0] == "AdvertenciaDatosNoEtiquetados":
        return "Faltan datos etiquetados para un modelo supervisado"
    return str(conclusion)


def ejecutar_diagnostico():
    s = st.session_state
    hechos = {
        ("Objetivo", "problema", s["objetivo"]),
        ("EstadoEtiquetas", "problema", s["etiquetas"]),
        ("Relaciones", "problema", s["relaciones"]),
        ("EstructuraGrupos", "problema", s["grupos"]),
    }
    marcables = {
        "tabulares": "DatosTabulares",
        "escalados": "DatosEscalados",
        "interpretabilidad": "RequiereInterpretabilidad",
        "probabilidades": "RequiereProbabilidades",
        "requiere_etiquetas": "RequiereEtiquetas",
    }
    for campo, predicado in marcables.items():
        if s.get(campo):
            hechos.add((predicado, "problema"))

    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(hechos, base_conocimiento)
    s["hechos_finales"] = hechos_finales
    s["reglas_aplicadas"] = reglas_aplicadas


# --------------------------------------------------
# Encabezado
# --------------------------------------------------

col_titulo, col_ayuda = st.columns([3, 1], vertical_alignment="bottom")

with col_titulo:
    st.title("🎯 Diagnóstico")
    st.caption(
        f"Describe tu problema y el sistema experto te sugiere modelos de "
        f"Machine Learning. Base de conocimiento: {len(base_conocimiento)} reglas."
    )

with col_ayuda:
    with st.popover("¿Cómo funciona?", icon="💡", width="stretch"):
        st.html(pasos_html(pasos))
        st.caption("Cada campo del formulario tiene un ícono ⓘ: pasa el cursor sobre él para ver la explicación.")
        st.page_link("vistas/guia.py", label="Ver guía completa y diccionario", icon="📖")


col_form, col_resultados = st.columns([5, 6], gap="large")


# --------------------------------------------------
# Formulario
# --------------------------------------------------

with col_form:
    st.selectbox(
        "Escenario de demostración",
        ["Personalizado", *escenarios.keys()],
        key="caso_prueba",
        on_change=aplicar_escenario,
        help=ayudas["escenario"],
    )

    with st.form("formulario_problema"):
        st.markdown("**Objetivo y datos**")

        c1, c2 = st.columns(2)
        c1.selectbox(
            "Objetivo del problema",
            list(opciones_objetivo),
            format_func=opciones_objetivo.get,
            key="objetivo",
            help=ayudas["objetivo"],
        )
        c2.selectbox(
            "Etiquetas de los datos",
            list(opciones_etiquetas),
            format_func=opciones_etiquetas.get,
            key="etiquetas",
            help=ayudas["etiquetas"],
        )

        c1, c2 = st.columns(2)
        c1.selectbox(
            "Relaciones entre variables",
            list(opciones_relaciones),
            format_func=opciones_relaciones.get,
            key="relaciones",
            help=ayudas["relaciones"],
        )
        c2.selectbox(
            "Distribución de los grupos",
            list(opciones_grupos),
            format_func=opciones_grupos.get,
            key="grupos",
            help=ayudas["grupos"],
        )

        c1, c2 = st.columns(2)
        c1.checkbox("Datos tabulares", key="tabulares", help=ayudas["tabulares"])
        c2.checkbox("Datos escalados", key="escalados", help=ayudas["escalados"])

        st.markdown("**Qué esperas del modelo**")

        c1, c2, c3 = st.columns(3)
        c1.checkbox("Interpretable", key="interpretabilidad", help=ayudas["interpretabilidad"])
        c2.checkbox("Probabilidades", key="probabilidades", help=ayudas["probabilidades"])
        c3.checkbox("Requiere etiquetas", key="requiere_etiquetas", help=ayudas["requiere_etiquetas"])

        b1, b2 = st.columns([2, 1])
        enviar = b1.form_submit_button("Generar recomendaciones", type="primary", width="stretch")
        b2.form_submit_button("Limpiar", on_click=limpiar, width="stretch")

    if enviar:
        ejecutar_diagnostico()


# --------------------------------------------------
# Resultados
# --------------------------------------------------

with col_resultados:
    if "hechos_finales" not in st.session_state:
        st.html(
            '<div class="vacio">Llena el formulario y pulsa <b>Generar recomendaciones</b>.<br>'
            "Los modelos sugeridos y su explicación aparecen aquí.</div>"
        )
        st.stop()

    hechos_finales = st.session_state["hechos_finales"]
    reglas_aplicadas = st.session_state["reglas_aplicadas"]

    modelos = sorted(
        {hecho[2] for hecho in hechos_finales if hecho[0] == "RecomendarModelo"},
        key=lambda m: rendimiento_modelos.get(m, 80),
        reverse=True,
    )

    tab_modelos, tab_porque, tab_reglas = st.tabs(
        ["Recomendaciones", "¿Por qué?", f"Reglas aplicadas ({len(reglas_aplicadas)})"]
    )

    with tab_modelos:
        if ("AdvertenciaDatosNoEtiquetados", "problema") in hechos_finales:
            st.warning(
                "Marcaste que el problema requiere etiquetas, pero tus datos no están "
                "etiquetados. Un modelo supervisado no se podría entrenar así."
            )
        elif ("ModeloSupervisado", "problema") in hechos_finales:
            st.caption("✅ Tus datos etiquetados permiten usar aprendizaje supervisado.")

        if not modelos:
            st.warning(
                "Ninguna regla coincide con estas características. Prueba marcando "
                "«Datos tabulares», cambiando el tipo de relaciones o cargando un "
                "escenario de demostración."
            )
        else:
            st.html('<p class="pista">Pasa el cursor sobre un modelo para ver para qué sirve y un ejemplo.</p>')

            tarjetas = []
            for i, modelo in enumerate(modelos):
                nombre = nombres_modelos.get(modelo, modelo)
                info = buscar_info_modelo(nombre)
                detalle = (
                    [("Para qué sirve:", info["para_que"]), ("Ejemplo:", info["ejemplo"])]
                    if info else None
                )
                tarjetas.append(
                    tarjeta(
                        nombre,
                        resumen=descripciones_modelos.get(modelo, ""),
                        detalle=detalle,
                        destacada=(i == 0),
                        etiqueta=(
                            f"🏆 Mayor rendimiento demostrativo: {rendimiento_modelos.get(modelo, 80)} %"
                            if i == 0 else ""
                        ),
                    )
                )
            rejilla(tarjetas, ancho_min=240)

            st.markdown("**Rendimiento demostrativo**")
            st.caption("Valores simulados con fines educativos. No son resultados de evaluaciones reales.")
            grafico = pd.DataFrame({
                "Modelo": [nombres_modelos.get(m, m) for m in modelos],
                "Rendimiento (%)": [rendimiento_modelos.get(m, 80) for m in modelos],
            })
            st.bar_chart(
                grafico,
                x="Modelo",
                y="Rendimiento (%)",
                x_label="",
                horizontal=True,
                sort="-Rendimiento (%)",
                height=60 + 45 * len(modelos),
            )

    with tab_porque:
        if not modelos:
            st.info("No hay recomendaciones que explicar con estas características.")
        else:
            seleccionado = st.selectbox(
                "Modelo",
                modelos,
                format_func=lambda m: nombres_modelos.get(m, m),
            )
            responsables = [
                r for r in reglas_aplicadas
                if r["conclusion"] == ("RecomendarModelo", "problema", seleccionado)
            ]
            for regla in responsables:
                with st.container(border=True):
                    st.markdown(f"**{regla['id']}** · {regla['descripcion']}")
                    st.markdown(
                        "\n".join(f"- {texto_condicion(c)}" for c in regla["condiciones"])
                    )

    with tab_reglas:
        if not reglas_aplicadas:
            st.info("No se activó ninguna regla.")
        for regla in reglas_aplicadas:
            with st.expander(f"{regla['id']} · {texto_conclusion(regla['conclusion'])}"):
                st.caption(regla["descripcion"])
                st.markdown(
                    "\n".join(f"- {texto_condicion(c)}" for c in regla["condiciones"])
                )
