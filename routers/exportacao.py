from fastapi import APIRouter, HTTPException
from services.vitibrasil_service import fetch_data
from models.responses import DataResponse

router = APIRouter()

@router.get("/", response_model=DataResponse)
async def get_exportacao():
    """Consulta dados de Exportação."""
    return await fetch_data("opt_05", "Dados de Exportação obtidos com sucesso")
