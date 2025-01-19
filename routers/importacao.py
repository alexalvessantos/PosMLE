from fastapi import APIRouter, HTTPException
from services.vitibrasil_service import fetch_data
from models.responses import DataResponse

router = APIRouter()

@router.get("/", response_model=DataResponse)
async def get_importacao():
    """Consulta dados de Importação."""
    return await fetch_data("opt_04", "Dados de Importação obtidos com sucesso")
