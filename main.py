from fastapi import FastAPI
from db import Base, engine
from routers import *


app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(banner_router, tags=['Banner'])
app.include_router(image_router, tags=['Image'])
app.include_router(qa_router, tags=['Qa'])
