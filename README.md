# API Vitivinicultura

Esta é uma API criada com **FastAPI** para consultar dados relacionados à vitivinicultura, abrangendo aspectos como produção, processamento, comercialização, importação e exportação. A API se conecta a um sistema externo para obter essas informações.

## Funcionalidades Principais
- **Consulta de dados de produção**: Retorna informações sobre a produção.
- **Consulta de dados de processamento**: Retorna informações sobre o processamento.
- **Consulta de dados de comercialização**: Dados relacionados à comercialização de produtos.
- **Consulta de importação e exportação**: Dados sobre importação e exportação.

## Tecnologias Utilizadas
- **Python 3.7+**
- **FastAPI**
- **HTTPX** para requisições assíncronas
- **Uvicorn** como servidor ASGI

## Estrutura do Projeto
```
project/
├── main.py                     # Arquivo principal da aplicação
├── routers/                    # Contém os módulos de rotas
│   ├── producao.py
│   ├── processamento.py
│   ├── comercializacao.py
│   ├── importacao.py
│   └── exportacao.py
├── services/                   # Lógica e comunicação com serviços externos
│   └── vitibrasil_service.py
├── models/                     # Modelos de dados
│   └── responses.py
├── utils/                      # Utilitários (autenticação, helpers)
│   └── auth.py
└── README.md                   # Documentação do projeto
```

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/api-vitivinicultura.git
cd api-vitivinicultura
```

### 2. Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
# Ativar o ambiente virtual:
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o Servidor
```bash
uvicorn main:app --reload
```

### 5. Acessar a Documentação
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints Disponíveis
Abaixo estão os principais endpoints da API:

| Endpoint             | Método | Descrição                            |
|----------------------|---------|------------------------------------|
| `/producao/`         | `GET`   | Consulta dados de produção          |
| `/processamento/`    | `GET`   | Consulta dados de processamento    |
| `/comercializacao/`  | `GET`   | Consulta dados de comercialização    |
| `/importacao/`       | `GET`   | Consulta dados de importação         |
| `/exportacao/`       | `GET`   | Consulta dados de exportação         |

## Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.
