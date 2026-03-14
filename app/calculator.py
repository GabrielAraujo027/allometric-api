from .constants import GRUPOS

EXPOENTE_ALOMETRICO = 0.75

def calcular_dose(grupo_modelo, grupo_alvo, peso_alvo):

    modelo = GRUPOS[grupo_modelo]
    alvo = GRUPOS[grupo_alvo]

    peso_modelo = modelo["peso_modelo"]
    dose_modelo = modelo["dose_tratamento"]

    constante_metabolica_modelo = modelo["constante_metabolica"]
    constante_metabolica_alvo = alvo["constante_metabolica"]

    frequencia = modelo["frequencia"]
    intervalo = modelo["intervalo_tratamento"]

    dose_ajustada = dose_modelo * (peso_alvo / peso_modelo) ** EXPOENTE_ALOMETRICO * (constante_metabolica_alvo / constante_metabolica_modelo)
    

    dose_total = dose_ajustada * peso_alvo

    return {
        "resultado": {
            "dose_ajustada": {"valor": round(dose_ajustada,3), "unidade": "mg/kg"},
            "dose_total": {"valor": round(dose_total,3), "unidade": "mg"},
            "frequencia": {"valor": frequencia, "unidade": "horas"},
            "intervalo_tratamento": {"valor": intervalo, "unidade": "dias"}
        }
    }