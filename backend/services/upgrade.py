from backend.models.models import User, Account, Buildings, Levels_per_th_home, Traps, HomeTroops
from sqlalchemy import select, inspect
from backend import auth
from backend.database import SessionLocal

def get_unmaxed_things(tag : str, db ):

  db = SessionLocal()

  account = db.query(Account).filter(Account.tag == tag).first()

  th_lvl = account.town_hall_lvl 
  all_buildings = db.query(Buildings).filter(Buildings.player_tag == tag).all()
  all_traps = db.query(Traps).filter(Buildings.player_tag == tag).all()

  home_troops = db.query(HomeTroops).filter(Buildings.player_tag == tag).first()

  col_name = f"th{th_lvl}"

  all_buildings_dc = [{"building": b.building_type, "level": b.building_lvl, "cnt": b.building_cnt, "type": "building"} for b in all_buildings]
  all_traps_dc = [{"building": b.trap_type, "level": b.trap_lvl, "cnt": b.trap_cnt, "type": "trap"} for b in all_traps]
  all_buildings_dc.extend(all_traps_dc)
  home_troops_dc = [{"building": b.trap_type, "level": b.trap_lvl, "cnt": b.trap_cnt, "type": "trap"} for b in all_traps]

  max_levels_for_th = db.query(Levels_per_th_home).all()

  max_levels_for_th_dc = {b.thing: getattr(b, col_name) for b in max_levels_for_th}
  # print(max_levels_for_th_dc)
  troops_left = []
  maxed_troops = []
  for col in inspect(home_troops).mapper.column_attrs:
    if col.key[:-4] in max_levels_for_th_dc:
      if getattr(home_troops, col.key) < max_levels_for_th_dc[col.key[:-4]]:
        troops_left.append({"troop" : col.key, "level": getattr(home_troops, col.key), "max_lvl": max_levels_for_th_dc[col.key[:-4]]})
      else:
        maxed_troops.append({"troop" : col.key, "level": getattr(home_troops, col.key), "max_lvl": getattr(home_troops, col.key)})
    else:
      print(f"troop {col.key[:-4]} not in max_levels_for_th_dc")

  print(troops_left)

  buildings_left = []
  maxed_buildings = []

  for build in all_buildings_dc:
    b = build["building"]
    l = build["level"]
    cnt = build["cnt"]
    t = build["type"]
    if b not in max_levels_for_th_dc:
      print(f"Building {b} not found in max_level")
      continue
    if l < max_levels_for_th_dc[b]:
      buildings_left.append({"building": b, "level": l, "max_lvl": max_levels_for_th_dc[b], "cnt": cnt, "type": t})
    else:
      maxed_buildings.append({"building": b, "level": l, "max_lvl": l, "cnt":  cnt, "type":t})
    
  db.close()
  return {"buildings_left": buildings_left, "maxed_buildings" :maxed_buildings, "troops_left" :troops_left, "maxed_troops": maxed_troops}