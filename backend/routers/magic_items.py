from fastapi import FastAPI, Depends, HTTPException, APIRouter
from backend.schemas import schemas
from backend.services.account_related import _get_owned_account_or_403
from backend.services.database import store_magic_items
from backend import auth
from backend.models.models import Account, User, MagicItems

magic_items_router = APIRouter(prefix="/magic-items", tags=["magic-items"])

@magic_items_router.post("/count_each")
def magic_item_details(details: schemas.MagicItemDetails, user: auth.user_dependency, db: auth.db_dependency):
  tag = details.tag
  _get_owned_account_or_403(tag,user,db)
  account = db.query(Account).filter(Account.tag == tag).first()
  if not account:
      raise HTTPException(status_code=404, detail="Account not found")

  exists = db.query(MagicItems).filter(MagicItems.player_tag == tag).first()
  if exists:
    db.query(MagicItems).filter(MagicItems.player_tag == tag).delete()
    db.commit()
  store_magic_items(db, details.dict(), tag)

  return {"magic_item_details": details.dict()}
