from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from ..services.csv_service import read_csv_file

router = APIRouter()

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    """
    Cette route permet à l'utilisateur de télécharger un fichier CSV, 
    puis renvoie son contenu sous forme de JSON.
    """
    try:
        # Lire le contenu du fichier téléchargé
        contents = await file.read()
        # Convertir le contenu en DataFrame
        df = read_csv_file(contents.decode("utf-8"))
        
        # Convertir le DataFrame en dictionnaire pour le renvoyer en réponse
        return JSONResponse(content=df.to_dict(orient="records"))
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")
