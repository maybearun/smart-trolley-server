from fastapi import Depends, FastAPI,Response,HTTPException,status
from sqlalchemy.orm import Session
import models, db
from db import get_db
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

models.Base.metadata.create_all(bind=db.engine) #This line will create the table in the database 

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductSchema(BaseModel):
    product_name: str
    price: str
    rfid_tag: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Products).all()
    return products

@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_products(payload:ProductSchema, db: Session = Depends(get_db)):
    print(payload.dict())
    new_product = models.Products(**payload.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products/{item_id}")
def return_item(product_id: int):
    product=db.query(models.Products).filter(models.Products.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'product with id {id} was not found')
    return product 


