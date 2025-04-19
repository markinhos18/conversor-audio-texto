from fastapi import FastAPI, File, UploadFile
import whisper
import os

app = FastAPI()
model = whisper.load_model("base")  # Troque para "small", "medium" se quiser mais precisão

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"
    
    with open(file_location, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(file_location)
    os.remove(file_location)
    
    return {"text": result["text"]}
