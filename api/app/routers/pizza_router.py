from fastapi import FastAPI, Response, APIRouter, HTTPException, Depends
from typing import Union

from sqlalchemy.orm import Session

from typing import List

from ..models.pizza import Pizza, PizzaEntity

from ..db import get_db

from datetime import datetime

from ..services.pizza_service import PizzaService

router = APIRouter(
    prefix="/pizzas",
    tags=["pizzas"]
)
# CREATE ITEM
# TODO:implémenter la route permettant de créer un item


@router.post("/")
def create_item(db: Session = Depends(get_db)):
    """
    Création d'un item
    """
    try:
        # TODO: route à implémenter
        return {"message": "To do"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

# READ ALL ITEMS


@router.get("/", response_model=List[Pizza])
def get_all_items(db: Session = Depends(get_db), name: str = None):
    """
    Lecture de tous les items
    """
    try:
        if name != None:
            # Si query param name renseigné dans l'URL
            # Effectue une recherche basée sur une variable name fournie en option dans l'URL
            #
            # Option A : Lecture directe dans la BDD avec l'ORM
            return db.query(PizzaEntity).filter(PizzaEntity.name.ilike('%'+name+'%'))
            #
            # Option B : Emploi de la classe PizzaService
            # service = PizzaService(db)
            # return service.search_by_name(name)
        else:
            # Sinon, récupère tous les items
            #
            # Option A : Lecture directe dans la BDD avec l'ORM
            return db.query(PizzaEntity).all()
            #
            # OU
            #
            # Option B : Emploi de la classe PizzaService
            # service = PizzaService(db)
            # return service.find_all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

# READ ONE ITEM


@router.get("/{id}", response_model=Pizza)
def get_one_item(id: int, db: Session = Depends(get_db)):
    """
    Lecture d'un item sélectionné selon son id
    """
    try:
        # Option A : Lecture directe dans la BDD avec l'ORM
        pizza = db.query(PizzaEntity).filter(PizzaEntity.id == id).first()
        #
        # OU
        #
        # Option B : Emploi de la classe PizzaService
        # service = PizzaService(db)
        # pizza = service.find_one_by_id(id)
        if not pizza:
            raise Exception('Not found')
        else:
            return pizza
    except Exception as e:
        if e.__eq__("Not found"):
            raise HTTPException(status_code=404, detail="Pizza not found")
        else:
            raise HTTPException(status_code=500)

# UPDATE
# TODO:implémenter la route permettant de mettre à jour un item


@router.put("/{id}")
def update_item(id: int, db: Session = Depends(get_db)):
    """
    Mise à jour complète d'un item sélectionné selon son id
    """
    try:
        # TODO: route à implémenter
        return {"message": "To do"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

# UPDATE
# TODO:implémenter la route permettant de mettre à jour partiellement un item


@router.patch("/{id}")
def update_item(id: int, db: Session = Depends(get_db)):
    """
    Mise à jour partielle d'un item sélectionné selon son id
    """
    try:
        # TODO: route à implémenter
        return {"message": "To do"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

# DELETE
# TODO:implémenter la route permettant de supprimer un item


@router.delete("/{id}")
def update_item(id: int, db: Session = Depends(get_db)):
    """
    Suppression d'un item sélectionné selon son id
    """
    try:
        # TODO: route à implémenter
        return {"message": "To do"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)
