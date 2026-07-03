from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
import model
from model import Product
import schemas

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post("/products")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
# GET API
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products