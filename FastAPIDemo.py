from typing import Optional
from fastapi import FastAPI

app = FastAPI(title='Python API 例子',description='简单例子')


@app.get("/",summary='接口1注释',description='接口1描述',tags=['Hello World'])
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}",summary='接口2注释',description='接口2描述',tags=['Hello World'])
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}