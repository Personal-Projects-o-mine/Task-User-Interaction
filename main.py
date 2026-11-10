from fastapi import FastAPI, Request
import mockData
from dtos import ProductDTO

app = FastAPI()

@app.get("/home")
def home():
    return "Welcome"

@app.get("/hello")
def hello(request:Request):
    query_p = dict(request.query_params)
    return{
        "greet" : f"Hello {query_p.get("name")}, Your age is {query_p.get("age")}."
    }

@app.get("/product/{prod_id}")
def product(prod_id:int):
    for product in mockData.products:
        if product.get("id")==prod_id:
            return product
    return{"Note":"No Entry found."}

@app.get("/products")
def products():
    return mockData.products

@app.post("/create_prod")
def create_prod(body:ProductDTO):
    mockData.products.append(body.model_dump())
    return{
        "Product":"Created Successfully."
    }

@app.put("/update_prod")
def update_prod(body:ProductDTO):
    body = body.model_dump()
    id = body.get("id")
    for i,product in enumerate(mockData.products):
        if product.get("id")==id:
            mockData.products[i]=body
            return{
        "Product":"Updated Successfully."
            }
    return{
        "Product":"Not Updated."
    }

@app.delete("/delete_prod/{id}")
def delete_prod(id:int):
    for i, product in enumerate(mockData.products):
        if(product.get("id") == id):
            mockData.products.pop(i)
            return{
                "Product":"Deleted Successfully."
            }
    return{
        "Product":"Not Found."
    }

