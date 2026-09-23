from fastapi import FastAPI, Depends, HTTPException
from backend.schemas import schemas
from backend.database import engine, SessionLocal, Base
from backend.models import Account
from backend.config import settings
from backend.services.coc_api_calling import call_coc_api
from backend.services.database import store_in_db
from sqlalchemy import select, delete
import json

app = FastAPI() 
Base.metadata.create_all(engine)

session = SessionLocal()

@app.get("/")
def root():
  return "welcome to COC api"

@app.post("/village_data_json")
def get_json_data(village_data: schemas.village_data):

  if not village_data.tag:
    raise HTTPException(status_code=400, detail="Player tag is required")
  
  exist = None

  stmt = select(Account).where(Account.tag == village_data.tag)
  with engine.connect() as conn:
    exist = conn.execute(stmt).first()

  if exist:
    with engine.connect() as conn:
      with conn.begin():
        conn.execute(delete(Account).where(Account.tag == village_data.tag))

  village_data = village_data.model_dump()
  data = call_coc_api(village_data["tag"])
  store_in_db(village_data, data)

  return {"player_tag": village_data["tag"], "data": data} 
