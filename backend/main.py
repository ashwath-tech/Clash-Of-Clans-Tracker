from fastapi import FastAPI, Depends, HTTPException
from backend.schemas import schemas
from backend.database import engine, SessionLocal, Base
from backend.models.models import Account, User
from backend.config import settings
from backend.services.coc_api_calling import call_coc_api
from backend.services.database import store_in_db
from sqlalchemy import select, delete
from backend.services import upgrade
import json
from backend import auth

app = FastAPI()
app.include_router(auth.router)
Base.metadata.create_all(engine)


def _get_owned_account_or_403(tag: str, user, db):
    """Raise 403 unless `tag` is one of this user's linked accounts."""
    print("tag",tag)
    if tag not in [a.tag for a in user.accounts]:
        raise HTTPException(status_code=403, detail="This account is not linked to your user")


@app.get("/")
def root():
    return "welcome to COC api"


@app.post("/village_data_json")
def get_json_data(village_data: schemas.village_data, user: auth.user_dependency, db: auth.db_dependency):
    if not village_data.tag:
        raise HTTPException(status_code=400, detail="Player tag is required")

    tag = village_data.tag

    existing_account = db.query(Account).filter(Account.tag == tag).first()
    previously_linked_user_ids = []
    if existing_account:
        previously_linked_user_ids = [u.id for u in existing_account.users]
        db.delete(existing_account)
        db.commit()

    village_data_dict = village_data.model_dump()
    data = call_coc_api(tag)
    store_in_db(db, village_data_dict, data)

    account = db.query(Account).filter(Account.tag == tag).first()

    linked_user_ids = set(previously_linked_user_ids) | {user.id}
    for uid in linked_user_ids:
        u = db.query(User).filter(User.id == uid).first()
        if u and account not in u.accounts:
            u.accounts.append(account)
            db.add(u)
    db.commit()

    return {"player_tag": tag, "data": data}

@app.post("/gold_paass_status")
def update_gold_pass_status(tag: str, has_gold_pass: bool, user: auth.user_dependency, db: auth.db_dependency):
    _get_owned_account_or_403(tag, user, db)
    account = db.query(Account).filter(Account.tag == tag).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    account.has_gold_pass = has_gold_pass
    db.commit()
    return {"player_tag": tag, "has_gold_pass": has_gold_pass}

@app.post("/unmaxed_buildings")
def unmaxed_buildings(tag: str, user: auth.user_dependency, db: auth.db_dependency):
    _get_owned_account_or_403(tag, user, db)
    details = upgrade.get_unmaxed_things(tag, db)
    return details


@app.get("/building_time")
def building_time(tag: str, user: auth.user_dependency, db: auth.db_dependency):
    _get_owned_account_or_403(tag, user, db)
    details = upgrade.get_unmaxed_things(tag, db)
    building_details = details.get("buildings_left", [])
    print(f"building_details: {building_details}")
    total_time, time_details = upgrade.get_building_time(building_details, db)

    return {"total_time": total_time, "building_time": time_details}


@app.get("/laboratory_time")
def laboratory_time(tag: str, user: auth.user_dependency, db: auth.db_dependency):
    _get_owned_account_or_403(tag, user, db)
    details = upgrade.get_unmaxed_things(tag, db)
    troop_details = details.get("troops_left", [])
    spell_details = details.get("spells_left", [])
    total_time, time_details = upgrade.get_lab_time(troop_details + spell_details, db)
    return {"total_time": total_time, "lab_time": time_details} 


@app.get("/setup_RAG")
def setup_rag(tag: str, user: auth.user_dependency, db: auth.db_dependency):
    if user.user_type != "admin":
        raise HTTPException(status_code=403, detail="You are not authorized to access this endpoint.")
    return "not yet implemented"


@app.get("/ask_question")
def ask_question(question: str, user: auth.user_dependency, db: auth.db_dependency):

    return {"question": question, "answer": "This feature is under development."}
# crafting station setup
# cost for building
# database is doesnt have all levels