from ..models.task import Task, TaskEntity
from .exceptions.task_exceptions import UnfoundException, AlreadyCompletedException, UnknownException
from datetime import datetime
from sqlalchemy import desc


class TaskService:

    def __init__(self, db):
        self.db = db

    def create_task(self, task: Task) -> TaskEntity:
        """
        Créé une nouvelle task
        """
        try:
            new_task = TaskEntity(**task.model_dump())
            new_task.created_at = datetime.now()
            self.db.add(new_task)
            self.db.commit()
            self.db.refresh(new_task)
            return new_task
        except Exception as e:
            print(e)
            raise UnknownException

    def completeTask(self, task_id: int) -> TaskEntity:
        """
        Complète une task sélectionnée par son id
        """
        try:
            task = self.findOneById(task_id)
            if task.is_completed == True:
                raise AlreadyCompletedException()
            else:
                task.is_completed = True
                task.completed_at = datetime.now()
                task.updated_at = datetime.now()
                self.db.commit()
                self.db.refresh(task)
                return task
        except UnfoundException as e:
            raise UnfoundException
        except Exception as e:
            print(e)
            raise UnknownException

    def updateTask(self, task_id: int, updated_task: Task) -> TaskEntity:
        """
        Met à jour une task sélectionnée par son id
        """
        try:
            task = self.findOneById(task_id)
            # met à jour l'ensemble des champs de l'objet Task selon les valeurs transmises
            for key, value in updated_task.model_dump().items():
                setattr(task, key, value)
            task.updated_at = datetime.now()
            self.db.commit()
            self.db.refresh(task)
            return task
        except UnfoundException as e:
            raise UnfoundException
        except Exception as e:
            print(e)
            raise UnknownException

    def filterByUrgenceAndImportance(self, urgence: int = None, importance: int = None):
        """
        Récupère la liste des tasks par ordre de création décroissant filtrées par niveau d'importance et d'urgence
        """
        try:
            if urgence != None and importance != None:
                return self.db.query(TaskEntity).order_by(TaskEntity.id.desc()).filter(TaskEntity.importance == importance, TaskEntity.urgence == urgence).all()
            elif importance != None:
                return self.db.query(TaskEntity).order_by(TaskEntity.id.desc()).filter(TaskEntity.importance == importance).all()
            elif urgence != None:
                return self.db.query(TaskEntity).order_by(TaskEntity.id.desc()).filter(TaskEntity.urgence == urgence).all()
            else:
                raise BadDataException

        except Exception as e:
            print(e)
            raise UnknownException

    def findAll(self):
        """
        Récupère la liste des tasks par ordre de création décroissant
        """
        try:
            return self.db.query(TaskEntity).order_by(TaskEntity.id.desc()).all()
        except Exception as e:
            print(e)
            raise UnknownException

    def findAllCompleted(self):
        """
        Récupère la liste des tasks accomplies par ordre de création décroissant
        """
        try:
            return self.db.query(TaskEntity).where(TaskEntity.is_completed == True).order_by(TaskEntity.id.desc()).all()
        except Exception as e:
            print(e)
            raise UnknownException

    def findAllUncompleted(self):
        """
        Récupère la liste des tasks non-accomplies par ordre de création décroissant
        """
        try:
            return self.db.query(TaskEntity).where(TaskEntity.is_completed == False).order_by(TaskEntity.id.desc()).all()
        except Exception as e:
            print(e)
            raise UnknownException

    def findOneById(self, task_id: int):
        """
        Récupère une task par son id
        """
        task = self.db.query(TaskEntity).filter(
            TaskEntity.id == task_id).first()
        if not task:
            raise UnfoundException
        else:
            return task

    def delete(self, task_id: int):
        """
        Supprime une task sélectionnée selon son id
        """
        try:
            task = self.findOneById(task_id)
            self.db.delete(task)
            self.db.commit()
        except UnfoundException as e:
            raise UnfoundException
        except Exception as e:
            print(e)
            raise UnknownException
