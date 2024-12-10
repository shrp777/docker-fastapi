from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import ValidationError


from .routers import task_router

app = FastAPI()
app.include_router(task_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    masque les détails de l'erreur et retourne une erreur générique
    intercepte toutes les erreurs de validation générées par Pydantic
    """
    return JSONResponse({"detail": "Bad Request"}, status_code=400)


@app.get("/")
def read_root():
    """
    Racine de l'API
    """
    return {"message": "Kanban API"}
