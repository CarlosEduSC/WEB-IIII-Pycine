from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/dia_semana/{dia}/{mes}/{ano}")
def diaSemana(dia, mes , ano):

    dataHora = datetime(int(ano), int(mes), int(dia), 0, 0, 0)
    data = datetime.date(dataHora)
    dataDia = data.weekday()

    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"]

    diaSemana = dias[dataDia]

    return {
        "dia": dia,
        "mes": mes,
        "ano": ano,
        "dia_da_semana": diaSemana
    }

@app.get("/numero/{num}")
def numero(num):
    result = ""

    if int(num)%2 == 0:
        result = "PAR"
    else:
        result = "IMPAR"

    return {
        "numero": num,
        "par_ou_impar": result,
    }

@app.get("/hora_cidade/{cidade}")
def horaCidade(cidade):
    fusoToquio = pytz.timezone('Asia/Tokyo')
    fusoLondres = pytz.timezone('Europe/London')
    fusoLasVegas = pytz.timezone('America/Los_Angeles')

    cidade = cidade.upper()

    if cidade == "TOKYO":
        hora = datetime.now(fusoToquio)

    elif cidade == "LONDRES":
        hora = datetime.now(fusoLondres)

    elif cidade == "LASVEGAS":
        hora = datetime.now(fusoLasVegas)
        

    return {
        "cidade": cidade,
        "hora": hora
    }