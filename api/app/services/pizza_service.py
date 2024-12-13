from ..models.pizza import PizzaEntity


class PizzaService:

    def __init__(self, db):
        self.db = db

    def find_all(self):
        """
        Récupère l'ensemble des pizzas
        """
        try:
            return self.db.query(PizzaEntity).all()
        except Exception as e:
            print(e)
            raise Exception("Can't find pizzas")

    def find_one_by_id(self, id: int):
        """
        Récupère une pizza selon son id
        """
        try:
            pizza = self.db.query(PizzaEntity).where(
                PizzaEntity.id == id).first()
            if not pizza:
                raise Exception("Pizza not found")
            else:
                return pizza
        except Exception as e:
            print(e)
            raise Exception("Not found")

    def search_by_name(self, name: str):
        """
        Recherche les pizzas selon la valeur de leur attribut name
        """
        try:
            return self.db.query(PizzaEntity).filter(PizzaEntity.name.ilike('%'+name+'%'))
        except Exception as e:
            print(e)
            raise Exception("Not found")
