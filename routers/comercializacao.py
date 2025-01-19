from fastapi import APIRouter, HTTPException
from services.vitibrasil_service import fetch_data
from models.responses import DataResponse

router = APIRouter()

@router.get("/", response_model=DataResponse)
async def get_comercializacao():
    """Consulta dados de Comercialização."""
    return await fetch_data("opt_03", "Dados de Comercialização obtidos com sucesso")
