from typing import Any
from sqlalchemy.orm import Session

class CRUDBase:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, db: Session, id: Any):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_by_name(self,db:Session,name:Any):
        return db.query(self.model).filter(self.model.name==name).all()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def remove(self, db: Session, name: Any):
        obj = db.query(self.model).get(name)
        db.delete(obj)
        db.commit()
        return obj
