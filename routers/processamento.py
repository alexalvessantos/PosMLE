from fastapi import APIRouter, HTTPException
from services.vitibrasil_service import fetch_data
from models.responses import DataResponse

router = APIRouter()

@router.get("/", response_model=DataResponse)
async def get_processamento():
    """Consulta dados de Processamento."""
    return await fetch_data("opt_02", "Dados de Processamento obtidos com sucesso")
