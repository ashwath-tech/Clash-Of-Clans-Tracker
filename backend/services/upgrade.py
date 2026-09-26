from backend.models.models import User, Account, Buildings, Levels_per_th_home, Traps, HomeTroops, Heroes, Spells, Time_per_th_home
from sqlalchemy import select, inspect
from backend import auth
from backend.database import SessionLocal

def get_unmaxed_things(tag : str, db ):

  db = SessionLocal()

  account = db.query(Account).filter(Account.tag == tag).first()

  th_lvl = account.town_hall_lvl 
  all_buildings = db.query(Buildings).filter(Buildings.player_tag == tag).all()
  all_traps = db.query(Traps).filter(Traps.player_tag == tag).all()

  home_troops = db.query(HomeTroops).filter(HomeTroops.player_tag == tag).first()
  home_spells = db.query(Spells).filter(Spells.player_tag == tag).first()
  col_name = f"th{th_lvl}"

  all_buildings_dc = [{"building": b.building_type, "level": b.building_lvl, "cnt": b.building_cnt, "type": "building"} for b in all_buildings]
  all_traps_dc = [{"building": b.trap_type, "level": b.trap_lvl, "cnt": b.trap_cnt, "type": "trap"} for b in all_traps]
  all_buildings_dc.extend(all_traps_dc)

  max_levels_for_th = db.query(Levels_per_th_home).all()

  max_levels_for_th_dc = {b.thing: getattr(b, col_name) for b in max_levels_for_th}

  troops_left = []
  maxed_troops = []
  for col in inspect(home_troops).mapper.column_attrs:
    if col.key[:-4] in max_levels_for_th_dc:
      if max_levels_for_th_dc[col.key[:-4]] == 0:
        print(f"max level for {col.key[:-4]} is 0, skipping")
        continue
      if getattr(home_troops, col.key) < max_levels_for_th_dc[col.key[:-4]]:
        troops_left.append({"troop" : col.key, "level": getattr(home_troops, col.key), "max_lvl": max_levels_for_th_dc[col.key[:-4]]})
      else:
        maxed_troops.append({"troop" : col.key, "level": getattr(home_troops, col.key), "max_lvl": getattr(home_troops, col.key)})
    else:
      print(f"troop {col.key[:-4]} not in max_levels_for_th_dc")

  spells_left = []
  maxed_spells = []
  for col in inspect(home_spells).mapper.column_attrs:
    if col.key[:-4] in max_levels_for_th_dc:
      if max_levels_for_th_dc[col.key[:-4]] == 0:
        print(f"max level for {col.key[:-4]} is 0, skipping")
        continue
      if getattr(home_spells, col.key) < max_levels_for_th_dc[col.key[:-4]]:
        spells_left.append({"spell" : col.key, "level": getattr(home_spells, col.key), "max_lvl": max_levels_for_th_dc[col.key[:-4]]})
      else:
        maxed_spells.append({"spell" : col.key, "level": getattr(home_spells, col.key), "max_lvl": getattr(home_spells, col.key)})
    else:
      print(f"spell {col.key[:-4]} not in max_levels_for_th_dc")
  #heroes
  heroes_left = []
  maxed_heroes = []
  
  heroes = db.query(Heroes).filter(Buildings.player_tag == tag).first()  
  all_heroes = {}
  all_heroes = {"barbarian_king_lvl": heroes.barbarian_king_lvl, "archer_queen_lvl": heroes.archer_queen_lvl, "grand_warden_lvl": heroes.grand_warden_lvl, "royal_champion_lvl": heroes.royal_champion_lvl, "dragon_duke_lvl": heroes.dragon_duke_lvl}

  for hero, level in all_heroes.items():
    if hero[:-4] in max_levels_for_th_dc:
      if max_levels_for_th_dc[hero[:-4]] == 0:
        print(f"max level for {hero[:-4]} is 0, skipping")
        continue
      if level < max_levels_for_th_dc[hero[:-4]]:
        heroes_left.append({"hero": hero, "level": level, "max_lvl": max_levels_for_th_dc[hero[:-4]]})
      else:
        maxed_heroes.append({"hero": hero, "level": level, "max_lvl": level})
    else:
      print(f"hero {hero[:-4]} not in max_levels_for_th_dc")

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
    if max_levels_for_th_dc[b] == 0:
      print(f"max level for {b} is 0, skipping")
      continue
    if l < max_levels_for_th_dc[b]:
      buildings_left.append({"building": b, "level": l, "max_lvl": max_levels_for_th_dc[b], "cnt": cnt, "type": t})
    else:
      maxed_buildings.append({"building": b, "level": l, "max_lvl": l, "cnt":  cnt, "type":t})
    
  db.close()
  return {"buildings_left": buildings_left, "maxed_buildings" :maxed_buildings, "troops_left" :troops_left, "maxed_troops": maxed_troops, "heroes_left": heroes_left, "maxed_heroes": maxed_heroes, "spells_left": spells_left, "maxed_spells": maxed_spells}

def get_building_time(building_list, db):
  total_time = 0
  time_details = {}

  print("----------------------------------")

  time_for_all = db.query(Time_per_th_home).all()
  time_for_all_dc = {
    b.thing: {
        col_name: getattr(b, col_name)
        for col_name in inspect(b).mapper.column_attrs.keys()
    }
    for b in time_for_all
  }

  for building in building_list:
    name = building["building"]
    level = building["level"]
    cnt = building["cnt"]
    max_level = building["max_lvl"]

    if name == "town_hall":
      continue

    if name not in time_for_all_dc:
      print(f"Building {name} not found in time_for_all_dc")
      continue

    if name not in time_details:
      time_details[name] = {"total_time": 0}

    building_time = 0

    for i in range(level, max_level):
      col_name = f"level{i+1}"
      step_key = f"{i}_to_{i+1}"

      if col_name not in time_for_all_dc[name]:
        print(f"Column {col_name} not found in time_for_all_dc for building {name}")
        continue

      unit_time = time_for_all_dc[name][col_name]

      if unit_time is None:
        print(f"No time data for {name} at {col_name}, skipping")
        continue

      contribution = unit_time * cnt

      if step_key in time_details[name]:
        time_details[name][step_key]["count"] += cnt
      else:
        time_details[name][step_key] = {
            "count": cnt,
            "time": unit_time
        }

      building_time += contribution
      print(f"Building {name} level {i} to {i+1} time: {unit_time} * count: {cnt} = {contribution}")

    time_details[name]["total_time"] += building_time

    total_time += building_time

  return total_time, time_details
 