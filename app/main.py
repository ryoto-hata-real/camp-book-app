from fastapi import FastAPI
from routers import users, places, customers

app = FastAPI()
app.include_router(users.router)
app.include_router(places.router)
app.include_router(customers.router)

@app.get("/")
def read_root():
  return {"Hello": "World"}