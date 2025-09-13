from fastapi import FastAPI
from app.routers import auth_routes, employees
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Employee Assessment API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(employees.router)

@app.get("/")
async def root():
    return {"message": "Employee Assessment API."}