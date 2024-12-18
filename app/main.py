from fastapi import FastAPI
from .routers import csv_router

app = FastAPI()

# Inclure les routes pour manipuler les fichiers CSV
app.include_router(csv_router.router)
