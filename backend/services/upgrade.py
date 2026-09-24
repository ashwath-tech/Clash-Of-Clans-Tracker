from backend.models.models import User, Account, Buildings, Levels_per_th_home
from sqlalchemy import select
from backend import auth
from backend.database import SessionLocal

def get_unmaxed_things(tag : str, db ):
  db = SessionLocal()
  account = db.query(Account).filter(Account.tag == tag).first()
  th_lvl = account.town_hall_lvl 
  buildings_left = db.query(Buildings).filter(Buildings.player_tag == tag).all()
  max_levels_for_th = db.query(Levels_per_th_home).filter(Levels_per_th_home.th{})
  buildings_left_dc = [{"building": b.building_type, "level": b.building_lvl, "cnt": b.building_cnt} for b in buildings_left]
  



  db.close()
  return buildings_left_dc
