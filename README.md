# Conversor de Áudio para Texto

API para transcrição de áudio para texto utilizando FastAPI e Whisper.

## Requisitos

- Python 3.8+
- FastAPI
- Whisper
- uvicorn

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Inicie o servidor:
```bash
uvicorn main:app --reload
```

2. Acesse a API em `http://localhost:8000/docs`
3. Use o endpoint `/transcribe/` para enviar um arquivo de áudio e receber a transcrição. 