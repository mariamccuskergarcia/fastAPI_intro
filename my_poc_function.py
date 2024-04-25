from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2 import Error
import uvicorn

app = FastAPI()

class Product(BaseModel):
    name: str
    description: str
    cost_of_manufacture: float

def connect_to_database():
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="ce06-pg-service",
            password="Ablat@@ihgb4566",
            host="34.89.114.222",
            port="5432",
            database="postgres"
        )
        return connection
    except (Exception, Error) as error:
        raise HTTPException(status_code=500, detail="Error connecting to PostgreSQL")

def list_all_products():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        # Execute the SQL query to select all products from the table
        cursor.execute("SELECT * FROM product_catalogue")
        # Fetch all rows from the result set
        products = cursor.fetchall()
        return [{'name': product[0], 'description': product[1], 'cost_of_manufacture': product[2]} for product in products]
    except (Exception, Error) as error:
        raise HTTPException(status_code=500, detail="Error fetching products from PostgreSQL")
    finally:
        connection.close()

def add_product(product: Product):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        # Execute the SQL query to insert a new product into the table
        cursor.execute("INSERT INTO product_catalogue (name, description, cost_of_manufacture) VALUES (%s, %s, %s) RETURNING *", (product.name, product.description, product.cost_of_manufacture))
        # Fetch the newly added product
        added_product = cursor.fetchone()
        connection.commit()
        if added_product:
            return {'status': 'success', 'product': {'name': added_product[0], 'description': added_product[1], 'cost_of_manufacture': added_product[2]}}
        else:
            raise HTTPException(status_code=500, detail="Product insertion failed.")
    except (Exception, Error) as error:
        raise HTTPException(status_code=500, detail=f"Error adding product to PostgreSQL: {error}")
    finally:
        connection.close()

@app.get("/products/", response_model=List[Product])
async def get_products():
    return list_all_products()

@app.post("/products/", response_model=Product)
async def create_product(product: Product = Body(...)):
    return add_product(product)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="34.89.114.222", port=5432)  # Change the port here if needed

import requests

response = requests.get('http://34.89.114.222:5432/products/')
print(response.json())
