from fastapi import FastAPI, HTTPException, status
from models import *

app = FastAPI()

@app.post('/simulação', status_code=status.HTTP_200_OK)
def simulacao(simulacao: Simulacao):
    if simulacao.quantidade % 1000 != 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A quantidade de milhas deve ser múltiplo de 1000")
    elif simulacao.desconto < 0 or simulacao.desconto > 80:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O desconto deve ser de 0 até 80 por cento")
    elif simulacao.bonus < 0 or simulacao.bonus > 300:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O bônus deve ser de 0 até 300 por cento")
    simulacao.cacular_valores()
    return simulacao