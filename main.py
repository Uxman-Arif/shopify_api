from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DB_FILE = "db.json"

# ----------------- Helpers -----------------
def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({"products": [], "orders": [], "customers": []}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ----------------- Models -----------------
class Product(BaseModel):
    title: str
    price: str
    inventory: int
    status: str = "active"

class Customer(BaseModel):
    name: str
    email: str

class LineItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    customer_id: int
    line_items: list[LineItem]

# ----------------- Endpoints -----------------

@app.get("/health")
def health():
    return {"status": "ok"}

# Products
@app.get("/products")
def get_products():
    db = load_db()
    return {"products": db["products"]}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    db = load_db()
    for p in db["products"]:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product: Product):
    db = load_db()
    new_id = len(db["products"]) + 1
    new_product = {"id": new_id, **product.dict()}
    db["products"].append(new_product)
    save_db(db)
    return {"success": True, "product_id": new_id}

# Customers
@app.get("/customers")
def get_customers():
    db = load_db()
    return {"customers": db["customers"]}

@app.post("/customers")
def create_customer(customer: Customer):
    db = load_db()
    new_id = len(db["customers"]) + 1
    new_customer = {"id": new_id, **customer.dict()}
    db["customers"].append(new_customer)
    save_db(db)
    return {"success": True, "customer_id": new_id}

# Orders
@app.get("/orders")
def get_orders():
    db = load_db()
    return {"orders": db["orders"]}

@app.post("/orders")
def create_order(order: Order):
    db = load_db()
    new_id = len(db["orders"]) + 1
    new_order = {"id": new_id, **order.dict()}
    db["orders"].append(new_order)
    save_db(db)
    return {"success": True, "order_id": new_id}
