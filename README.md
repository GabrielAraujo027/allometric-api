# Allometric Dose Calculator API

API para cálculo de dose medicamentosa entre espécies utilizando **Escalonamento Alométrico Interespecífico (Interspecific Allometric Scaling)** baseado na **Taxa Metabólica Basal (TMB)**.

O objetivo da aplicação é estimar a dose e o intervalo de administração de um medicamento para um **animal alvo**, a partir de dados conhecidos de um **animal modelo**.

Esse tipo de abordagem é amplamente utilizado em:

* Medicina veterinária
* Farmacologia comparativa
* Extrapolação de doses entre espécies
* Estudos fisiológicos interespecíficos

---

# Fundamento Científico

O método utiliza relações metabólicas baseadas na massa corporal.

## Peso metabólico

PM = M^0.75

Onde:

* **M** = massa corporal (kg)

## Taxa metabólica basal

TMB = K × PM

Onde:

* **K** = constante metabólica dependente do grupo taxonômico
* **PM** = peso metabólico

---

# Cálculo da Dose

Etapas utilizadas na aplicação:

### 1. TMB do modelo

TMB_modelo = K_modelo × (M_modelo^0.75)

### 2. TMB do alvo

TMB_alvo = K_alvo × (M_alvo^0.75)

### 3. Dose total do modelo

DT_modelo = Dose_modelo × Massa_modelo

### 4. Dose metabólica

DM = DT_modelo / TMB_modelo

### 5. Dose total do alvo

DT_alvo = DM × TMB_alvo

### 6. Dose por kg do alvo

Dose_alvo = DT_alvo / Massa_alvo

---

# Cálculo do Intervalo entre Doses

O intervalo é ajustado utilizando a **taxa metabólica específica (TME)**.

TME = TMB / Massa

Intervalo_alvo = (TME_modelo × Intervalo_modelo) / TME_alvo

---

# Estrutura do Projeto

```
allometric-api
│
├── app
│   ├── main.py
│   ├── calculator.py
│   ├── constants.py
│   └── static
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Instalação

Clone o repositório:

```
git clone <url-do-repositorio>
cd allometric-api
```

Crie um ambiente virtual:

```
python -m venv venv
```

Ative o ambiente virtual.

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

# Executando a API

Execute o servidor com:

```
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática (Swagger):

```
http://127.0.0.1:8000/docs
```

---

# Exemplo de Uso

Modelo:

* cão
* massa = **10 kg**
* dose = **15 mg/kg**
* intervalo = **12 horas**

Alvo:

* cobra
* massa = **0.45 kg**

Resultado aproximado:

* Dose alvo ≈ **5 mg/kg**
* Intervalo ≈ **39 horas**

---

# Observação Científica

Os resultados são **estimativas baseadas em modelos metabólicos interespecíficos**.

Eles **não substituem protocolos clínicos específicos para cada espécie ou medicamento**, devendo ser utilizados apenas como ferramenta de apoio ou estudo comparativo.

---

# Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn

---
