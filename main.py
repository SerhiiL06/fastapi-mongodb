from fastapi import FastAPI
from src.blog.routers import blog_router
from src.users.routets import users_router


app = FastAPI()


app.include_router(blog_router)
app.include_router(users_router)
