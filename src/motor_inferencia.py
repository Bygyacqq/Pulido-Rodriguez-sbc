import logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def verificar_condiciones(hechos, condiciones):
    """
    Verifica si todas las condiciones de una regla
    se encuentran dentro de los hechos disponibles.
    """
    return all(condicion in hechos for condicion in condiciones)

def encadenamiento_hacia_adelante(hechos_iniciales, base_conocimiento, max_iteraciones=100):
    """
    Aplica encadenamiento hacia adelante para poder obtener nuevas conclusiones a partir de los hechos inciales.

    Parámetros:
    hechos_inciales: Conjunto de hechos que ya se conocen.
    base_conocimineto: Lista de reglas de producción.

    Retorna:
    hechos: Cojunto de hechos inciales y derivados.
    reglas_aplicadas: Lista de las reglas que fueron utilizadas.
    
    """

    hechos = set(hechos_iniciales)
    reglas_aplicadas = []
    hubo_cambios = True
    iteracion = 0
    estados_visitados = set()
    logging.info("Se está iniciando el proceso de inferencia")


    while hubo_cambios:
        if iteracion >= max_iteraciones:
            logging.warning("El limite de iteraciones permitidas se ha alcanzado.")
            break
        estado_actual = frozenset(hechos)
        if estado_actual in estados_visitados:
            logging.warning("Existen estados repetidos. El proceso se detuvo por seguridad.")
            break
        estados_visitados.add(estado_actual)
        iteracion += 1
        hubo_cambios = False
        logging.info(f"Iteración {iteracion}.")
        for regla in base_conocimiento:
            condiciones = set(regla["condiciones"])
            conclusion = regla["conclusion"]
            if condiciones.issubset(hechos):
                if regla not in reglas_aplicadas:
                    reglas_aplicadas.append(regla)
                    logging.info(f"Regla activada: {regla['id']} ")
                if conclusion not in hechos:
                    hechos.add(conclusion)
                    hubo_cambios = True
                    logging.info(f"Nueva conclusión: {conclusion}")
    
    logging.info("Proceso de inferencia finalizado.")

    return hechos, reglas_aplicadas

def explicar_razonamiento(reglas_aplicadas):
    """
    Explica las reglas utilizadas por el sistema

    Parametros:
        reglas_aplicadas: Lista de las reglas activadas durante el endadenamiento hacia adelante. 
    """

    if not reglas_aplicadas:
        print("Las reglas no se aplicaron.")
        print("No es posible generar nuevas conclusiones.")
        return
    
    print("Explicación del razonamiento")
    print("-" * 40)

    for regla in reglas_aplicadas:
        print(f"\nRegla aplicada: {regla['id']}")
        print(f"Descripción: {regla['descripcion']}")
        print(f"Conclusión: {regla['conclusion']}")
    
    print("\nFin del razonamiento")

def porque(conclusion, reglas_aplicadas):
    """
    Explica el por qué se obtuvo al conclusión.
    """
    reglas_encontradas = [
        regla for regla in reglas_aplicadas
        if regla["conclusion"] == conclusion
    ]
    if not reglas_encontradas:
        print("No se encontró una regla aplicada la cuál genere esta conclusión.")
        return

    print("Consulta de la explicación")
    print("-" * 40)
    print(f"Conclusión consultada: {conclusion}")

    for regla in reglas_encontradas:
        print(f"\nRegla responsable: {regla['id']}")
        print(f"Descripción:{regla['descripcion']}")
        print(f"Condiciones necesarias:")

        for condicion in regla["condiciones"]:
            print(f"- {condicion}")
            
    print("\nFin de la explicación")

    