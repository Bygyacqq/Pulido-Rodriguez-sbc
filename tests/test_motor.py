from src.base_conocimiento import crear_base_conocimiento
from src.motor_inferencia import (
    encadenamiento_hacia_adelante,
    explicar_razonamiento,
    porque
)
def test_base_conocimiento_contiene_15_reglas():
    reglas = crear_base_conocimiento()

    assert len(reglas) == 15

def test_encadenamiento_recomienda_regresion_logistica():
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    assert (
        "RecomendarModelo",
        "problema",
        "RegresionLogistica"
    ) in hechos_finales

    assert any(regla["id"] == "R1" for regla in reglas_aplicadas)

def test_encadenamiento_activa_varias_reglas():
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema"),
        ("Relaciones", "problema", "Complejas")
    }

    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    modelos_esperados = {
        "RegresionLogistica",
        "RandomForestClasificacion",
        "GradientBoostingClasificacion"
    }

    modelos_obtenidos = {
        hecho[2]
        for hecho in hechos_finales
        if hecho[0] == "RecomendarModelo"
    }

    assert modelos_esperados.issubset(modelos_obtenidos)

    reglas_esperadas = {"R1", "R3", "R4"}

    reglas_obtenidas = {
        regla["id"] for regla in reglas_aplicadas
    }

    assert reglas_esperadas.issubset(reglas_obtenidas)

def test_encadenamiento_sin_conclusiones():
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Desconocido")
    }

    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    assert hechos_finales == hechos_iniciales
    assert reglas_aplicadas == []

def test_advertencia_datos_no_etiquetados():
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("RequiereEtiquetas", "problema"),
        ("EstadoEtiquetas", "problema", "NoEtiquetados")
    }

    hechos_finales, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    assert (
        "AdvertenciaDatosNoEtiquetados",
        "problema"
    ) in hechos_finales

    assert any(regla["id"] == "R15" for regla in reglas_aplicadas)

def test_explicar_razonamiento_muestra_reglas_aplicadas(capsys):
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    _, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    explicar_razonamiento(reglas_aplicadas)

    salida = capsys.readouterr().out

    assert "Explicación del razonamiento" in salida
    assert "Regla aplicada: R1" in salida
    assert "RegresionLogistica" in salida
    assert "Fin del razonamiento" in salida
def test_porque_explicar_conclusion_especifica(capsys):
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    _, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    conclusion = (
        "RecomendarModelo",
        "problema",
        "RegresionLogistica"
    )

    porque(conclusion, reglas_aplicadas)

    salida = capsys.readouterr().out

    assert "Consulta de la explicación" in salida
    assert "Conclusión consultada:" in salida
    assert "Regla responsable: R1" in salida
    assert "Condiciones necesarias:" in salida
    assert "Fin de la explicación" in salida

def test_porque_sin_regla_responsable(capsys):
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    _, reglas_aplicadas = encadenamiento_hacia_adelante(
        hechos_iniciales,
        reglas
    )

    conclusion = (
        "RecomendarModelo",
        "problema",
        "DBSCAN"
    )

    porque(conclusion, reglas_aplicadas)

    salida = capsys.readouterr().out

    assert "No se encontró una regla aplicada" in salida
def test_logging_registra_eventos_del_motor(caplog):
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    with caplog.at_level("INFO"):
        encadenamiento_hacia_adelante(
            hechos_iniciales,
            reglas
        )

    mensajes = [registro.message for registro in caplog.records]

    assert any(
        "Se está iniciando el proceso de inferencia" in mensaje
        for mensaje in mensajes
    )

    assert any(
        "Regla activada: R1" in mensaje
        for mensaje in mensajes
    )

    assert any(
        "Proceso de inferencia finalizado" in mensaje
        for mensaje in mensajes
    )

def test_motor_respeta_limite_de_iteraciones(caplog):
    reglas = crear_base_conocimiento()

    hechos_iniciales = {
        ("Objetivo", "problema", "Clasificacion"),
        ("DatosTabulares", "problema")
    }

    with caplog.at_level("WARNING"):
        encadenamiento_hacia_adelante(
            hechos_iniciales,
            reglas,
            max_iteraciones=1
        )

    mensajes = [registro.message for registro in caplog.records]

    assert any(
        "El limite de iteraciones permitidas se ha alcanzado."
        in mensaje
        for mensaje in mensajes
    )
