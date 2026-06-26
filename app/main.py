from fastapi import FastAPI

from routers import company,job


app = FastAPI()

app.include_router(company.router),(job.router)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"about": "This is about page"}

@app.get("/Admin")
def read_Admin():
    return {"Admin":"Balachandra"}