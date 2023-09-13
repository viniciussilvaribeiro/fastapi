from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, delete, select

from application.dispositivos_service import DispositivosService
from persistence.utils import obter_engine
from presentation.viewmodels.models import *

router = APIRouter()
prefix = '/ambientes/{ambiente_id}/dispositivos'

engine = obter_engine()

dispositivos_service = DispositivosService()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DispositivoBase)
def buscar_dispositivos_por_id(id: int, id_dis: int):
    return dispositivos_service.buscar_dispositivos_por_id(id, id_dis)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[DispositivoLeitura])
def obter_dispositivos(id: int):
    return dispositivos_service.obter_dispositivos(id)