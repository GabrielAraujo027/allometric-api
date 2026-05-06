from enum import Enum

class GrupoAnimal(str, Enum):
    passeriforme = "passeriforme"
    nao_passeriforme = "nao_passeriforme"
    mamifero_placentario = "mamifero_placentario"
    marsupial = "marsupial"