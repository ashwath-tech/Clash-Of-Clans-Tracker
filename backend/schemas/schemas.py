from __future__ import annotations
from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict

class village_data(BaseModel):
  tag : str
  timestamp: int
  helpers: List[helper_data] | None = []
  buildings: List[building_data]
  traps: List[trap_data]
  decos: List[deco_data]
  obstacles: List[obstacle_data]
  units: List[troop_data]
  siege_machines: List[troop_data]
  heroes: List[troop_data]
  spells: List[troop_data]
  pets: List[troop_data]
  equipment: List[troop_data]
  house_parts: List[int]
  skins: List[int]
  sceneries: List[int]
  buildings2: List[building_data]
  traps2: List[trap_data]
  decos2: List[deco_data]
  obstacles2: List[obstacle_data]
  units2: List[troop_data]
  heroes2: List[troop_data]
  skins2: List[int]
  boosts: Dict[str, int]

  @field_validator("tag")
  def validate_tag(cls, tag : str):
    tag = tag.strip()
    if tag[0] != "#":
      raise ValueError("Tag must start with '#'")
    return tag
    
class helper_data(BaseModel):
  data: int
  lvl: int
  helper_cooldown: Optional[int] = None

class building_data(BaseModel):
  data: int
  lvl: Optional[int] = None
  cnt: Optional[int] = None
  weapon: Optional[int] = None
  gear_up: Optional[int] = None
  timer: Optional[int] = None
  helper_recurrent: Optional[int] = None
  types: Optional[List[CraftingStation_data]] = None

class CraftingStation_data(BaseModel):
  data: int
  modules: List[CraftingStation_level]

class CraftingStation_level(BaseModel):
  data: int
  lvl: int
  timer: Optional[int] = None
  helper_recurrent: Optional[bool] = None

class trap_data(BaseModel):
  data: int
  lvl: int
  cnt: Optional[int] = None
  timer: Optional[int] = None
  helper_recurrent: Optional[bool] = None

class deco_data(BaseModel):
  data: int
  cnt: int

class obstacle_data(BaseModel):
  data: int
  cnt: int

class troop_data(BaseModel):
  data: int
  lvl: int
  timer: Optional[int] = None
  helper_recurrent: Optional[bool] = None

