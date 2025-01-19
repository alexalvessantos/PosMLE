from fastapi import APIRouter, HTTPException
from services.vitibrasil_service import fetch_data
from models.responses import DataResponse

router = APIRouter()

@router.get("/", response_model=DataResponse)
async def get_producao():
    """Consulta dados de Produção."""
    return await fetch_data("opt_01", "Dados de Produção obtidos com sucesso")
