from fastapi import FastAPI, Request
import mockData

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

@app.post("/createprod")
def create_prod():
    id = input("Write new id.")
    title = input("Write new title.")
    price = input("Write new price.")
    product = {
        "id":id,
        "title":title,
        "price":price
    }
    mockData.products.append(product)
    return{
        "Product":"Created Successfully."
    }

