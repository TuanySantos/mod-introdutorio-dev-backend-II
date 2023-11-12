from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/{name}')
def say_hello(name:str):
    if not name:
        pass
    return {'Hello' : name}

products = [
    Product(id=1, name='Tenis', description='Allstar', price=150.98)
]

@app.get('/api/products')
def get_products():
    return products