import httpx
from fastapi import HTTPException
from models.responses import DataResponse

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

async def fetch_data(option: str, success_message: str) -> DataResponse:
    """Consulta os dados da API externa."""
    async with httpx.AsyncClient() as client:
        try:
            url = f"{BASE_URL}?opcao={option}"
            print(f"Consultando URL: {url}")
            response = await client.get(url)
            response.raise_for_status()
            print(f"Resposta recebida para {option}: {response.text[:200]}...")  # Mostra os primeiros 200 caracteres
            
            # Tentar processar a resposta como JSON
            try:
                data = response.json()
            except ValueError:
                # Se não for JSON, retornar o conteúdo como texto
                data = {"html_content": response.text}

            return DataResponse(data=data, message=success_message)
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")
            raise HTTPException(status_code=503, detail="Erro ao acessar dados da Embrapa")