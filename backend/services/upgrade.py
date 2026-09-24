from backend.models.models import User, Buildings
from sqlalchemy import select
from backend import auth
from backend.database import SessionLocal

def get_unmaxed_things(tag : str, db ):
  db = SessionLocal()
  buildings_left = db.query(Buildings).filter(Buildings.player_tag == tag).all()

  buildings_left_dc = [{"building": b.building_type, "level": b.building_lvl, "cnt": b.building_cnt} for b in buildings_left]

  db.close()
  return buildings_left_dc
