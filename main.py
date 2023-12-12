from fastapi import FastAPI
from dotenv import load_dotenv
from routers.routers import todo_router


load_dotenv()
app = FastAPI()


app.include_router(todo_router)
