from backend.models.models import (
    User,
    Account,
    Buildings,
    Levels_per_th_home,
    Traps,
    HomeTroops,
    Heroes,
    HeroEquipment,
    Spells,
    Time_per_th_home,
)
from sqlalchemy import select, inspect
from backend import auth
from backend.database import SessionLocal


def get_unmaxed_things(tag: str, db):

    db = SessionLocal()

    account = db.query(Account).filter(Account.tag == tag).first()

    th_lvl = account.town_hall_lvl

    all_buildings = db.query(Buildings).filter(Buildings.player_tag == tag).all()
    all_traps = db.query(Traps).filter(Traps.player_tag == tag).all()

    home_troops = db.query(HomeTroops).filter(HomeTroops.player_tag == tag).all()
    home_spells = db.query(Spells).filter(Spells.player_tag == tag).all()
    home_heroes = db.query(Heroes).filter(Heroes.player_tag == tag).all()
    home_equipment = db.query(HeroEquipment).filter(HeroEquipment.player_tag == tag).all()

    all_buildings_dc = [
        {"building": b.building_type, "level": b.building_lvl, "cnt": b.building_cnt, "type": "building"}
        for b in all_buildings
    ]
    all_traps_dc = [
        {"building": b.trap_type, "level": b.trap_lvl, "cnt": b.trap_cnt, "type": "trap"}
        for b in all_traps
    ]
    all_buildings_dc.extend(all_traps_dc)

    # Levels_per_th_home is now narrow: one row per (thing, category, th_level)
    max_levels_for_th = db.query(Levels_per_th_home).filter(
        Levels_per_th_home.th_level == th_lvl
    ).all()
    max_levels_for_th_dc = {b.thing: b.unlocked_level for b in max_levels_for_th}

    # --- Troops (normalized: one row per troop) ---
    troops_left = []
    maxed_troops = []
    for troop in home_troops:
        name = troop.troop_type
        level = troop.troop_lvl

        if name not in max_levels_for_th_dc:
            print(f"troop {name} not in max_levels_for_th_dc")
            continue
        max_lvl = max_levels_for_th_dc[name]
        if max_lvl == 0:
            print(f"max level for {name} is 0, skipping")
            continue

        if level < max_lvl:
            troops_left.append({"troop": name, "level": level, "max_lvl": max_lvl})
        else:
            maxed_troops.append({"troop": name, "level": level, "max_lvl": level})

    # --- Spells (normalized: one row per spell) ---
    spells_left = []
    maxed_spells = []
    for spell in home_spells:
        name = spell.spell_type
        level = spell.spell_lvl

        if name not in max_levels_for_th_dc:
            print(f"spell {name} not in max_levels_for_th_dc")
            continue
        max_lvl = max_levels_for_th_dc[name]
        if max_lvl == 0:
            print(f"max level for {name} is 0, skipping")
            continue

        if level < max_lvl:
            spells_left.append({"spell": name, "level": level, "max_lvl": max_lvl})
        else:
            maxed_spells.append({"spell": name, "level": level, "max_lvl": level})

    # --- Heroes (normalized: one row per hero) ---
    heroes_left = []
    maxed_heroes = []
    for hero in home_heroes:
        name = hero.hero_type
        level = hero.hero_lvl

        if name not in max_levels_for_th_dc:
            print(f"hero {name} not in max_levels_for_th_dc")
            continue
        max_lvl = max_levels_for_th_dc[name]
        if max_lvl == 0:
            print(f"max level for {name} is 0, skipping")
            continue

        if level < max_lvl:
            heroes_left.append({"hero": name, "level": level, "max_lvl": max_lvl})
        else:
            maxed_heroes.append({"hero": name, "level": level, "max_lvl": level})

    # --- Hero equipment (new normalized table, split out of Heroes) ---
    equipment_left = []
    maxed_equipment = []
    for equipment in home_equipment:
        name = equipment.equipment_type
        level = equipment.equipment_lvl

        if name not in max_levels_for_th_dc:
            print(f"equipment {name} not in max_levels_for_th_dc")
            continue
        max_lvl = max_levels_for_th_dc[name]
        if max_lvl == 0:
            print(f"max level for {name} is 0, skipping")
            continue

        if level < max_lvl:
            equipment_left.append({"equipment": name, "level": level, "max_lvl": max_lvl})
        else:
            maxed_equipment.append({"equipment": name, "level": level, "max_lvl": level})

    # --- Buildings / traps (schema unchanged) ---
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
            maxed_buildings.append({"building": b, "level": l, "max_lvl": l, "cnt": cnt, "type": t})

    db.close()
    return {
        "buildings_left": buildings_left,
        "maxed_buildings": maxed_buildings,
        "troops_left": troops_left,
        "maxed_troops": maxed_troops,
        "heroes_left": heroes_left,
        "maxed_heroes": maxed_heroes,
        "spells_left": spells_left,
        "maxed_spells": maxed_spells,
        "equipment_left": equipment_left,
        "maxed_equipment": maxed_equipment,
    }


def _build_time_lookup(db):
    """Time_per_th_home is now narrow: one row per (thing, category, level).
    Build a {thing: {level: upgrade_time_seconds}} lookup."""
    time_for_all = db.query(Time_per_th_home).all()
    time_for_all_dc = {}
    for row in time_for_all:
        time_for_all_dc.setdefault(row.thing, {})[row.level] = row.upgrade_time_seconds
    return time_for_all_dc


def get_building_time(building_list, db):
    total_time = 0
    time_details = {}

    time_for_all_dc = _build_time_lookup(db)

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
            next_level = i + 1
            step_key = f"{i}_to_{next_level}"

            if next_level not in time_for_all_dc[name]:
                print(f"Level {next_level} not found in time_for_all_dc for building {name}")
                continue

            unit_time = time_for_all_dc[name][next_level]

            if unit_time is None:
                print(f"No time data for {name} at level {next_level}, skipping")
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
            print(f"Building {name} level {i} to {next_level} time: {unit_time} * count: {cnt} = {contribution}")

        time_details[name]["total_time"] += building_time

        total_time += building_time

    return total_time, time_details


def get_lab_time(troop_spell_list, db):
    total_time = 0
    time_details = {}

    time_for_all_dc = _build_time_lookup(db)

    for lab_object in troop_spell_list:
        # troop_type / spell_type are already clean names now (no "_lvl" suffix to strip)
        name = lab_object["troop"] if "troop" in lab_object else lab_object["spell"]
        level = lab_object["level"]
        max_level = lab_object["max_lvl"]

        if name not in time_for_all_dc:
            print(f"Building {name} not found in time_for_all_dc")
            continue

        if name not in time_details:
            time_details[name] = {"total_time": 0}

        building_time = 0

        for i in range(level, max_level):
            next_level = i + 1
            step_key = f"{i}_to_{next_level}"

            if next_level not in time_for_all_dc[name]:
                print(f"Level {next_level} not found in time_for_all_dc for building {name}")
                continue

            unit_time = time_for_all_dc[name][next_level]

            if unit_time is None:
                print(f"No time data for {name} at level {next_level}, skipping")
                continue

            contribution = unit_time

            if step_key in time_details[name]:
                time_details[name][step_key]["count"] += 1
            else:
                time_details[name][step_key] = {
                    "count": 1,
                    "time": unit_time
                }

            building_time += contribution

        time_details[name]["total_time"] += building_time

        total_time += building_time

    return total_time, time_details