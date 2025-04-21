# Conversor de Áudio para Texto

API para transcrição de áudio para texto utilizando FastAPI e Whisper.

## Requisitos

- Python 3.8+
- FastAPI
- Whisper
- uvicorn

## Instalação

### Usando Python local

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Usando Docker

1. Construa a imagem:
```bash
docker build -t conversor-audio-texto .
```

2. Execute o container:
```bash
docker run -p 8000:8000 conversor-audio-texto
```

## Como usar

1. Se estiver usando Python local, inicie o servidor:
```bash
uvicorn main:app --reload
```

2. Acesse a API em `http://localhost:8000/docs`
3. Use o endpoint `/transcribe/` para enviar um arquivo de áudio e receber a transcrição. 