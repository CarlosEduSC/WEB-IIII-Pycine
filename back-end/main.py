from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/hora")
def horaCerta():
    return {
        "hora": datetime.now(),
        "local": "BR"
    }

@app.get("/upper/{nome}")
def upper(nome):
    return {
        "nome": nome,
        "nomeUpper": nome.upper()
    }
    


# iniciar servidor web: uvicorn main:app --reload