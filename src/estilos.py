"""
Estilos y piezas de HTML compartidas por las páginas.

Los colores base y la fuente están en .streamlit/config.toml.
Aquí solo va lo que el tema de Streamlit no cubre: las tarjetas
que muestran su explicación al pasar el cursor.
"""

from html import escape

import streamlit as st

_CSS = """
<style>
:root {
    --superficie: #172437;
    --borde: #2A3B55;
    --texto: #E4ECF7;
    --apagado: #9CB0CA;
    --acento: #5BB8E8;
    --destacado: #E9B44C;
}

/* Rejilla que acomoda tantas columnas como quepan */
.rejilla {
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--ancho-min, 260px)), 1fr));
    align-items: start;
    margin: 4px 0 18px 0;
}

/* Tarjeta: muestra título y resumen; la explicación se abre con hover o al tocarla */
.tarjeta {
    background: var(--superficie);
    border: 1px solid var(--borde);
    border-radius: 10px;
    padding: 11px 14px;
    cursor: default;
    outline: none;
}

.tarjeta:hover,
.tarjeta:focus {
    border-color: var(--acento);
}

.tarjeta:focus-visible {
    box-shadow: 0 0 0 2px var(--acento);
}

.tarjeta .titulo {
    color: var(--texto);
    font-weight: 600;
    font-size: 0.97rem;
    line-height: 1.35;
}

.tarjeta .resumen {
    color: var(--apagado);
    font-size: 0.88rem;
    line-height: 1.5;
    margin-top: 3px;
}

.tarjeta .detalle {
    display: grid;
    grid-template-rows: 0fr;
    transition: grid-template-rows 0.2s ease;
}

.tarjeta .detalle > div {
    overflow: hidden;
}

.tarjeta:hover .detalle,
.tarjeta:focus .detalle {
    grid-template-rows: 1fr;
}

.tarjeta .detalle p {
    color: var(--texto);
    font-size: 0.88rem;
    line-height: 1.55;
    margin: 8px 0 0 0;
}

.tarjeta .detalle b {
    color: var(--acento);
    font-weight: 600;
}

.tarjeta.destacada {
    border-color: var(--destacado);
}

.tarjeta .etiqueta {
    display: inline-block;
    color: var(--destacado);
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 4px;
}

/* Pasos del proceso: ícono al lado del texto */
.paso {
    display: flex;
    gap: 10px;
    align-items: flex-start;
}

.paso .icono {
    font-size: 1.25rem;
    line-height: 1.3;
}

.pista {
    color: var(--apagado);
    font-size: 0.85rem;
    margin: -4px 0 6px 0;
}

.vacio {
    border: 1px dashed var(--borde);
    border-radius: 10px;
    padding: 28px 20px;
    color: var(--apagado);
    text-align: center;
    line-height: 1.6;
}

@media (prefers-reduced-motion: reduce) {
    .tarjeta .detalle { transition: none; }
}
</style>
"""


def aplicar_estilos():
    st.html(_CSS)


def tarjeta(titulo, resumen="", detalle=None, destacada=False, etiqueta=""):
    """
    Arma una tarjeta. `detalle` es una lista de (rótulo, texto) que se
    muestra al pasar el cursor o al tocar la tarjeta.
    """
    clase = "tarjeta destacada" if destacada else "tarjeta"
    partes = [f'<div class="{clase}" tabindex="0">']
    partes.append(f'<div class="titulo">{escape(titulo)}</div>')
    if etiqueta:
        partes.append(f'<div class="etiqueta">{escape(etiqueta)}</div>')
    if resumen:
        partes.append(f'<div class="resumen">{escape(resumen)}</div>')
    if detalle:
        parrafos = "".join(
            f"<p><b>{escape(rotulo)}</b> {escape(texto)}</p>" if rotulo
            else f"<p>{escape(texto)}</p>"
            for rotulo, texto in detalle
        )
        partes.append(f'<div class="detalle"><div>{parrafos}</div></div>')
    partes.append("</div>")
    return "".join(partes)


def rejilla(tarjetas, ancho_min=260):
    """Muestra una lista de tarjetas en una rejilla adaptable."""
    st.html(
        f'<div class="rejilla" style="--ancho-min: {ancho_min}px">'
        + "".join(tarjetas)
        + "</div>"
    )


def pasos_html(pasos):
    tarjetas = [
        f'<div class="tarjeta"><div class="paso"><span class="icono">{icono}</span>'
        f'<div><div class="titulo">{escape(titulo)}</div>'
        f'<div class="resumen">{escape(texto)}</div></div></div></div>'
        for icono, titulo, texto in pasos
    ]
    return '<div class="rejilla" style="--ancho-min: 220px">' + "".join(tarjetas) + "</div>"
