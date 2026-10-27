from fastapi import FastAPI, Depends, HTTPException, APIRouter
from backend.schemas import schemas

optimize_router = APIRouter(prefix="/optimize", tags=["optimize"])


#initial : Army-Storage-Defence-Hero-Collectors-Walls
# @optimize_router.post("/priority_order_buildings")
# def update_priority_order(tag: str, priority_order: str, user: auth.user_dependency, db: auth.db_dependency):
  
#     _get_owned_account_or_403(tag, user, db)
#     account = db.query(Account).filter(Account.tag == tag).first()
#     if not account:
#         raise HTTPException(status_code=404, detail="Account not found")
#     account.priority_order = priority_order
#     db.commit()
#     return {"player_tag": tag, "priority_order": priority_order}  