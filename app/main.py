from fastapi import FastAPI
from routers import users, places, customers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3001",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(places.router)
app.include_router(customers.router)

@app.get("/")
def read_root():
  return {"Hello": "World"}