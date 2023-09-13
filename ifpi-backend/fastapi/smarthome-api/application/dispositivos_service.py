from fastapi import HTTPException, status
from sqlalchemy import delete
from sqlmodel import Session, select, and_

from persistence.utils import obter_engine
from presentation.viewmodels.models import *

engine = obter_engine()

class DispositivosService():

    def __init__(self):
        self.session = engine
    
    def buscar_dispositivos_por_id(self, id: int, id_dis: int):
        session = Session(engine)
        instrucao = select(Dispositivo).where(and_(Dispositivo.id == id_dis, Ambiente.id == id))
        dispositivo = session.exec(instrucao).first()
        # para carregar relação "ambiente"
        dispositivo.ambiente
        session.close()
        return dispositivo
    
    def obter_dispositivos(self, id: int):
        # Buscar dispositivos
        session = Session(engine)
        inst = select(Dispositivo).where(Ambiente.id == id)
        
        dispositivos = session.exec(inst).fetchall()
        session.close()
        return dispositivos
