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


# # metabolismo basal
# @app.get("/metabolism")
# def metabolismo(massa: float):
#     resultado = 70 * (massa ** 0.75)
    
#     return {"massa": massa, "metabolism": resultado}

# # frequência cardíaca
# @app.get("/heart-rate")
# def heart_rate(massa: float):
#     resultado = 241 * (massa ** -0.25)
    
#     return {"massa": massa, "heart_rate": resultado}

# # expectativa de vida
# @app.get("/lifespan")
# def lifespan(massa: float):
#     resultado = 11 * (massa ** 0.2)
    
#     return {"massa": massa, "lifespan": resultado}

# # massa cerebral aproximada
# @app.get("/brain-mass")
# def brain_mass(massa: float):
#     resultado = 0.12 * (massa ** 0.66)

#     return {"massa": massa, "brain_mass": resultado}