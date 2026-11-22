
def crear_regla(identificador, condiciones, conclusion, descripcion):
    """
    Crea una regla de producción para el sistema:
    
    Parámetros:
    - identificador: Nombre o número de la regla.
    - condiciones: Hechos los cuáles se deben cumplir.
    - conclusiones: Hecho que se obtiene al aplicar la regla.
    - descripcion: Explicación del funcionamiento de la regla.

    Retorna:
    Un diccionario representativo de la regla.
    
    """
    return {
        "id": identificador,
        "condiciones": condiciones,
        "conclusion": conclusion,
        "descripcion": descripcion
    }



def crear_base_conocimiento():
    """
    Construye la base de conocimiento del sistema mediante
    15 reglas de producción.

    Retorna:
    Lista de reglas que utilizará el sistema experto.
    """

    reglas = [

        crear_regla(
            "R1",
            [
                ("Objetivo", "problema", "Clasificacion"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "RegresionLogistica"),
            "Recomendar regresión logística para clasificación con datos tabulares."
        ),

        crear_regla(
            "R2",
            [
                ("Objetivo", "problema", "Clasificacion"),
                ("RequiereInterpretabilidad", "problema")
            ],
            ("RecomendarModelo", "problema", "ArbolDecisionClasificacion"),
            "Recomendar árbol de decisión para clasificación cuando se requiere interpretabilidad."
        ),

        crear_regla(
            "R3",
            [
                ("Objetivo", "problema", "Clasificacion"),
                ("Relaciones", "problema", "Complejas")
            ],
            ("RecomendarModelo", "problema", "RandomForestClasificacion"),
            "Recomendar Random Forest para clasificación con relaciones complejas."
        ),

        crear_regla(
            "R4",
            [
                ("Objetivo", "problema", "Clasificacion"),
                ("Relaciones", "problema", "Complejas"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "GradientBoostingClasificacion"),
            "Recomendar Gradient Boosting para clasificación con datos tabulares y relaciones complejas."
        ),

        crear_regla(
            "R5",
            [
                ("Objetivo", "problema", "Clasificacion"),
                ("RequiereProbabilidades", "problema")
            ],
            ("RecomendarModelo", "problema", "RegresionLogistica"),
            "Recomendar regresión logística cuando se requieren probabilidades de clasificación."
        ),

        crear_regla(
            "R6",
            [
                ("Objetivo", "problema", "Regresion"),
                ("Relaciones", "problema", "Lineales")
            ],
            ("RecomendarModelo", "problema", "RegresionLineal"),
            "Recomendar regresión lineal cuando las relaciones entre las variables son lineales."
        ),

        crear_regla(
            "R7",
            [
                ("Objetivo", "problema", "Regresion"),
                ("RequiereInterpretabilidad", "problema")
            ],
            ("RecomendarModelo", "problema", "ArbolDecisionRegresion"),
            "Recomendar árbol de decisión para regresión cuando se requiere interpretabilidad."
        ),

        crear_regla(
            "R8",
            [
                ("Objetivo", "problema", "Regresion"),
                ("Relaciones", "problema", "Complejas"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "RandomForestRegresion"),
            "Recomendar Random Forest para regresión con datos tabulares y relaciones complejas."
        ),

        crear_regla(
            "R9",
            [
                ("Objetivo", "problema", "Regresion"),
                ("Relaciones", "problema", "Complejas"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "GradientBoostingRegresion"),
            "Recomendar Gradient Boosting para regresión con datos tabulares y relaciones complejas."
        ),

        crear_regla(
            "R10",
            [
                ("Objetivo", "problema", "Clustering"),
                ("EstructuraGrupos", "problema", "Compactos"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "KMeans"),
            "Recomendar K-Means para agrupaciones compactas con datos tabulares."
        ),

        crear_regla(
            "R11",
            [
                ("Objetivo", "problema", "Clustering"),
                ("EstructuraGrupos", "problema", "DensidadesVariables")
            ],
            ("RecomendarModelo", "problema", "DBSCAN"),
            "Recomendar DBSCAN para agrupaciones con densidades variables."
        ),

        crear_regla(
            "R12",
            [
                ("Objetivo", "problema", "Anomalias"),
                ("DatosTabulares", "problema")
            ],
            ("RecomendarModelo", "problema", "IsolationForest"),
            "Recomendar Isolation Forest para detección de anomalías con datos tabulares."
        ),

        crear_regla(
            "R13",
            [
                ("Objetivo", "problema", "Anomalias"),
                ("DatosEscalados", "problema")
            ],
            ("RecomendarModelo", "problema", "OneClassSVM"),
            "Recomendar One-Class SVM para detección de anomalías con datos escalados."
        ),

        crear_regla(
            "R14",
            [
                ("RequiereEtiquetas", "problema"),
                ("EstadoEtiquetas", "problema", "Etiquetados")
            ],
            ("ModeloSupervisado", "problema"),
            "Identificar el problema como apto para aprendizaje supervisado."
        ),

        crear_regla(
            "R15",
            [
                ("RequiereEtiquetas", "problema"),
                ("EstadoEtiquetas", "problema", "NoEtiquetados")
            ],
            ("AdvertenciaDatosNoEtiquetados", "problema"),
            "Advertir que no se dispone de datos etiquetados para entrenar modelos supervisados."
        )
    ]

    return reglas
