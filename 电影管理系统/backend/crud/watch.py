from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models import Watch as ModelsWatch
from typing import Any

class CRUDWatch(CRUDBase):

    def get_all_by_user_id(self, db:Session, user_id: Any):
        return db.query(self.model).filter(self.model.user_id == user_id).order_by(self.model.watchTime.desc())

    #通过用户验证hou，用电影名，观看时间，电影id创建观影记录
    def create(self, db:Session ,watch_params,user_id :Any):
        watch = ModelsWatch(
            user_id = user_id,
            movie_id = watch_params.movie_id,
            movie_name = watch_params.movie_name,
            movie_image = watch_params.movie_image
        )
        db.add(watch)
        db.commit()
        db.refresh(watch)
        return watch
    
    #通过观影记录id删除所有用户的某一个的观影记录
    def delete_watch_by_id(self,db:Session,id:Any):
         #get函数中的形参是主键的值，返回一个数据对象
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    
    #通过用户id删除所有用户的所有观影记录
    def delete_allwatch_by_user_id(self,db:Session,user_id:Any):
        objs = db.query(self.model).filter(self.model.user_id ==user_id)
        for obj  in objs:
            #delete只能删除一个数据，所以删除多个对象需要遍历
            db.delete(obj)
            db.commit()
        return obj
        
    #通过字符串获取包含改字段的观影记录
    def search(self,db:Session,movie_name:Any,user_id:Any):
        return db.query(self.model).filter(self.model.user_id==user_id).filter(self.model.movie_name.like('%'+movie_name + '%')).all()



crud_watch = CRUDWatch(ModelsWatch)