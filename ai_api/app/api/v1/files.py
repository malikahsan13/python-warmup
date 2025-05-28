from fastapi import APIRouter, File, UploadFile, HTTPException
import pdfplumber
import pandas as pd
import io
from app.vector_store.faiss_store import save_to_vector_store

router = APIRouter()

@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # ... (existing logic)
    with pdfplumber.open(io.BytesIO(await file.read())) as pdf:
        content = "".join([p.extract_text() for p in pdf.pages if p.extract_text()])
    save_to_vector_store(content)
    return {"message": "PDF uploaded and indexed."}

@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs allowed.")

    content = ""
    with pdfplumber.open(io.BytesIO(await file.read())) as pdf:
        for page in pdf.pages:
            content += page.extract_text() + "\n"

    return {"text": content[:1000]}  # return first 1000 chars as preview

@router.post("/upload/csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    
    df = pd.read_csv(io.BytesIO(await file.read()))
    return {"columns": df.columns.tolist(), "preview": df.head().to_dict(orient="records")}
