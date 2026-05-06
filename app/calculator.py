from .constants import GRUPOS

EXPOENTE_ALOMETRICO = 0.75

def calculo_alometrico(grupo_modelo, peso_modelo, grupo_alvo, peso_alvo, dose_modelo, intervalo):
    modelo = GRUPOS[grupo_modelo]
    alvo = GRUPOS[grupo_alvo]

    dose = calcular_dose(alvo, peso_alvo, peso_modelo, modelo, dose_modelo)
    frequencia = calcular_frequencia(peso_alvo, peso_modelo, intervalo, dose.tmb_modelo, dose.tmb_alvo)

    return {
        "resultado": {
            "dose_total": {"valor": round(dose["dose_total"],3), "unidade": "mg/kg"},
            "dose_por_kg": {"valor": round(dose["dose_por_kg"],3), "unidade": "mg/kg"},
            "frequencia": {"valor": frequencia, "unidade": "horas"}
        }
    }

def calcular_dose(alvo, peso_alvo, peso_modelo, modelo, dose):
    tmb_alvo = alvo * (peso_alvo ** EXPOENTE_ALOMETRICO)
    tmb_modelo = modelo * (peso_modelo ** EXPOENTE_ALOMETRICO)

    dose_total_modelo = dose * peso_modelo
    dm = dose_total_modelo / tmb_modelo
    dose_total_alvo = dm * tmb_alvo

    dkg_alvo = dose_total_alvo / peso_alvo;

    return {
        "tmb_alvo": tmb_alvo,
        "tmb_modelo": tmb_modelo,
        "dose_por_kg": dkg_alvo,
        "dose_total": dose_total_alvo
    }

def calcular_frequencia(peso_alvo, peso_modelo, intervalo, tmb_modelo, tmb_alvo):
    # taxa metabólica
    tmem = tmb_modelo / peso_modelo
    tmea = tmb_alvo / peso_alvo

    ix = tmem * intervalo
    ia = ix / tmea

    return ia