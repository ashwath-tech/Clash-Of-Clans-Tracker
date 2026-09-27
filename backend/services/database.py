from sqlalchemy.orm import Session
from backend.models.models import (
    Account,
    Buildings,
    Traps,
    Helpers,
    HomeTroops,
    Heroes,
    HeroEquipment,
    Spells,
)
from backend.services.idMapping import map_id_to_name

# Maps the API's helper "data" id to our narrow helper_type string.
HELPER_ID_TO_TYPE = {
    93000000: "builders_apprentice",
    93000001: "lab_assistant",
    93000002: "alchemist",
    93000003: "prospector",
}


def _slugify(name: str) -> str:
    """'Wall Breaker' -> 'wall_breaker', 'P.E.K.K.A' -> 'p.e.k.k.a' (matches
    the `thing` naming used in levels_per_th_home / time_per_th_home)."""
    return name.lower().replace(" ", "_")


def create_account_obj(json_part, api_part):
    troops = api_part.get("troops", [])
    heroes = api_part.get("heroes", [])
    hero_equipment = api_part.get("heroEquipment", [])
    spells = api_part.get("spells", [])
    helpers = json_part.get("helpers", [])

    new_account = Account(
        tag=api_part["tag"],
        name=api_part["name"],
        exp_lvl=api_part["expLevel"],
        town_hall_lvl=api_part["townHallLevel"],
        trophies=api_part["trophies"],
        building_details=[
            Buildings(
                building_type=map_id_to_name(b["data"]),
                building_lvl=b.get("lvl") or 0,
                building_cnt=b.get("cnt") or 1,
            )
            for b in json_part["buildings"]
        ],
        trap_details=[
            Traps(
                trap_type=map_id_to_name(b["data"]),
                trap_lvl=b.get("lvl") or 0,
                trap_cnt=b.get("cnt") or 1,
            )
            for b in json_part["traps"]
        ],
        helper_details=[
            Helpers(helper_type=HELPER_ID_TO_TYPE[h["data"]], helper_lvl=h.get("level", 0))
            for h in helpers
            if h.get("data") in HELPER_ID_TO_TYPE and h.get("level", 0) > 0
        ],
        troop_details=[
            HomeTroops(troop_type=_slugify(t["name"]), troop_lvl=t.get("level", 0))
            for t in troops
            if t.get("village", "home") == "home" and t.get("level", 0) > 0
        ],
        hero_details=[
            Heroes(hero_type=_slugify(h["name"]), hero_lvl=h.get("level", 0))
            for h in heroes
            if h.get("level", 0) > 0
        ],
        hero_equipment_details=[
            HeroEquipment(equipment_type=_slugify(e["name"]), equipment_lvl=e.get("level", 0))
            for e in hero_equipment
            if e.get("level", 0) > 0
        ],
        spell_details=[
            Spells(spell_type=_slugify(s["name"]), spell_lvl=s.get("level", 0))
            for s in spells
            if s.get("level", 0) > 0
        ],
    )
    return new_account


def store_in_db(db: Session, json_part, api_part) -> Account:
    new_account = create_account_obj(json_part, api_part)
    try:
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
    except Exception:
        db.rollback()
        raise
    return new_account