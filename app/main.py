from fastapi import FastAPI
from fastapi.responses import FileResponse
from .calculator import calcular_dose
from .models import GrupoAnimal
from .constants import GRUPOS

app = FastAPI(
    title="Calculadora Alométrica Veterinária",
    description="Cálculo de dose e frequência usando taxa metabólica basal (TMB)",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "mensagem": "API de cálculo alométrico funcionando",
        "documentacao": "/docs",
        "calculadora_web": "/calculadora"
    }

# home
@app.get("/calculadora")
def calculadora():
    return FileResponse("app/static/index.html")

# listar grupos
@app.get("/grupos")
def listar_grupos():
    return {"grupos": list(GRUPOS.keys())}

# ver constantes de um grupo
@app.get("/grupo/{grupo}")
def detalhes_grupo(grupo: GrupoAnimal):
    return GRUPOS[grupo.value]


# cálculo principal
@app.get("/calcular")
def calcular(
        grupo_modelo: GrupoAnimal,
        grupo_alvo: GrupoAnimal,
        peso_alvo: float
    ):
    resultado = calcular_dose(grupo_modelo.value, grupo_alvo.value, peso_alvo)

    return resultado
