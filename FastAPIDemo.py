from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # 创建数据库表

# Denpendency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title='Python API 示例',description='简单例子')


@app.get("/",summary='接口1注释',description='接口1描述',tags=['Hello World'])
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}",summary='接口2注释',description='接口2描述',tags=['Hello World'])
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/users", response_model=schemas.User, summary='创建用户',description='创建用户',tags=['数据库操作'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User], summary='获取用户列表',description='获取用户列表',tags=['数据库操作'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User, summary='获取用户',description='获取用户',tags=['数据库操作'])
def read_user(user_id: int = Query(None, description="用户Id"), db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item, summary='创建用户项目',description='创建用户项目',tags=['数据库操作'])
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item], summary='获取所有项目',description='获取所有项目',tags=['数据库操作'])
def read_items(skip: int = Query(0, description="页码"), limit: int = Query(100, description="每页数量"), db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items