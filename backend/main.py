from fastapi import FastAPI, Depends, HTTPException
from backend.schemas import schemas
from backend.database import engine, SessionLocal, Base
from backend.models.models import Account, User
from backend.config import settings
from backend.services.coc_api_calling import call_coc_api
from backend.services.database import store_in_db
from sqlalchemy import select, delete
import json
from backend import auth

app = FastAPI() 
app.include_router(auth.router)
Base.metadata.create_all(engine)

@app.get("/")
def root():
  return "welcome to COC api"

@app.post("/village_data_json")
def get_json_data(village_data: schemas.village_data, user: auth.user_dependency, db: auth.db_dependency):
    if not village_data.tag:
        raise HTTPException(status_code=400, detail="Player tag is required")

    tag = village_data.tag

    owner = db.query(User).filter(User.tag == tag).first()
    if owner and owner.id != user.id:
        raise HTTPException(status_code=400, detail="This account is already linked to another user")

    existing_account = db.query(Account).filter(Account.tag == tag).first()
    if existing_account:
        db.delete(existing_account)
        db.commit()

    if user.tag and user.tag != tag:
        old_account = db.query(Account).filter(Account.tag == user.tag).first()
        if old_account:
            db.delete(old_account)
            db.commit()

    village_data_dict = village_data.model_dump()
    data = call_coc_api(tag)
    store_in_db(db, village_data_dict, data)

    user.tag = tag
    db.add(user)
    db.commit()

    return {"player_tag": tag, "data": data}
