from fastapi import FastAPI, Request

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