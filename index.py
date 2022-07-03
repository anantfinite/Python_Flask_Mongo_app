from fastapi import FastAPI
from routes.user import user

app = FastAPI()
app.include_router(user)


































#to run server
#uvicorn index:app --reload

