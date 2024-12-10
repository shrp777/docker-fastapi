from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from typing import List

from ..models.task import Task, TaskEntity

from ..db import get_db

from datetime import datetime

from ..services.task_service import TaskService
from ..services.exceptions.task_exceptions import AlreadyCompletedException, UnfoundException, BadDataException, UnknownException


router = APIRouter()


@router.get("/tasks", response_model=List[Task])
def get_all_tasks(db: Session = Depends(get_db)):
    """
    Récupère la liste des tasks
    """
    try:
        task_service = TaskService(db)
        return task_service.findAll()
    except UnknownException as e:
        print(e)
        raise HTTPException(status_code=500)


@router.get("/tasks/{id}", response_model=Task)
def get_one_task(id: int, db: Session = Depends(get_db)):
    """
    Récupère une task par son id
    """
    try:
        task_service = TaskService(db)
        return task_service.findOneById(id)
    except UnfoundException:
        raise HTTPException(status_code=404, detail="Task not found")
    except UnknownException as e:
        print(e)
        raise HTTPException(status_code=500)


@router.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task, db: Session = Depends(get_db)) -> TaskEntity:
    """
    Créé une nouvelle task
    """
    try:
        task_service = TaskService(db)
        return task_service.create_task(task)
    except BadDataException:
        raise HTTPException(status_code=400)
    except UnknownException as e:
        print(e)
        raise HTTPException(status_code=500)


@router.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: Task, db: Session = Depends(get_db)):
    """
    Met à jour une task sélectionnée par son id
    """
    try:
        task_service = TaskService(db)
        return task_service.updateTask(id, updated_task)
    except UnfoundException:
        raise HTTPException(status_code=404, detail="Task not found")
    except UnknownException as e:
        print(e)
        raise HTTPException(status_code=500)


@router.patch("/tasks/{id}", response_model=Task)
def complete_task(id: int, db: Session = Depends(get_db)):
    """
    Complète une task sélectionnée par son id
    """
    try:
        task_service = TaskService(db)
        return task_service.completeTask(id)
    except UnfoundException:
        raise HTTPException(status_code=404, detail="Task not found")
    except AlreadyCompletedException:
        raise HTTPException(
            status_code=409, detail="Task is already completed")
    except UnknownException as e:
        print(e)
        raise HTTPException(status_code=500)


@router.delete("/tasks/{id}", status_code=204)
def delete_pizza(id: int, db: Session = Depends(get_db)):
    """
    Supprime une task sélectionnée selon son id
    """
    try:
        task_service = TaskService(db)
        return task_service.delete(id)
    except UnfoundException:
        raise HTTPException(status_code=404, detail="Task not found")
    except UnknownException as e:
        print(e.with_traceback)
        raise HTTPException(status_code=500)
