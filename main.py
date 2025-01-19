from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import producao, processamento, comercializacao, importacao, exportacao

# Configurações iniciais
app = FastAPI(title="API Vitivinicultura")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(producao.router, prefix="/producao", tags=["Produção"])
app.include_router(processamento.router, prefix="/processamento", tags=["Processamento"])
app.include_router(comercializacao.router, prefix="/comercializacao", tags=["Comercialização"])
app.include_router(importacao.router, prefix="/importacao", tags=["Importação"])
app.include_router(exportacao.router, prefix="/exportacao", tags=["Exportação"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
