import os
import subprocess
import sys

def run(cmd):
    subprocess.check_call(cmd, shell=True)

# criar venv se não existir
if not os.path.exists("venv"):
    print("Criando ambiente virtual...")
    run(f"{sys.executable} -m venv venv")

# caminho do python dentro do venv
python_venv = os.path.join("venv", "Scripts", "python.exe")

print("Atualizando pip...")
run(f"{python_venv} -m pip install --upgrade pip")

print("Instalando dependências...")
run(f"{python_venv} -m pip install fastapi uvicorn")

print("Ambiente pronto!")
print("Ative com:")
print("venv\\Scripts\\activate")