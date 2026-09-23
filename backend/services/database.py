from backend.database import SessionLocal, engine
from backend.models import (
    Account,
    Buildings,
    Traps,
    Helpers,
    HomeTroops,
    BBtroops,
    Heroes,
    Spells,
)
from sqlalchemy import select, insert
from backend.models import Account
from backend.services.idMapping import map_id_to_name

db = SessionLocal()

def create_account_obj(json_part, api_part):
  troops = api_part.get("troops", [])
  heroes = api_part.get("heroes", [])
  hero_equipment = api_part.get("heroEquipment", [])
  spells = api_part.get("spells", [])
  troops = api_part.get("troops", [])

  def bb_troop_lvl(name: str) -> int:
    return next(
      (
        t.get("level", 0)
        for t in troops
        if t.get("name") == name and t.get("village") == "builderBase"
      ),
      0,
    )

  def spell_lvl(name: str) -> int:
      return next((s.get("level", 0) for s in spells if s.get("name") == name), 0)


  def get_lvl(items: list, name: str) -> int:
      return next((i.get("level", 0) for i in items if i.get("name") == name), 0)

  def hero_lvl(name: str) -> int:
      return get_lvl(heroes, name)

  def equip_lvl(name: str) -> int:
      return get_lvl(hero_equipment, name)

  def troop_lvl(name):
    return next(
      (t.get("level", 0) for t in troops
        if t.get("name") == name and t.get("village", "home") == "home"),
      0,
    )
  new_account = Account(
      tag=api_part["tag"],
      name=api_part["name"],
      exp_lvl=api_part["expLevel"],
      town_hall_lvl=api_part["townHallLevel"],
      trophies=api_part["trophies"],
      building_details = [
        Buildings(
          building_type=map_id_to_name(b["data"]),
          building_lvl=b.get("lvl") or 0
        ) for b in json_part["buildings"]
      ],
      trap_details = [
        Traps(
          tool_type=map_id_to_name(b["data"]),
          tool_lvl=b.get("lvl") or 0
        ) for b in json_part["traps"]
      ],
      helper_details = [
        Helpers(
          builders_Apprentice_lvl = next((h.get("level", 0) for h in json_part.get("helpers", []) if h.get("data") == 93000000),0),
          lab_Assistant_lvl = next((h.get("level", 0) for h in json_part.get("helpers", []) if h.get("data") == 93000001),0),
          prospector_lvl = next((h.get("level", 0) for h in json_part.get("helpers", []) if h.get("data") == 93000003),0),
          alchemist_lvl = next((h.get("level", 0) for h in json_part.get("helpers", []) if h.get("data") == 93000002),0),
        )
      ],
      troop_details=[
        HomeTroops(
          barbarian_lvl=troop_lvl("Barbarian"),
          archer_lvl=troop_lvl("Archer"),
          goblin_lvl=troop_lvl("Goblin"),
          giant_lvl=troop_lvl("Giant"),
          wall_breaker_lvl=troop_lvl("Wall Breaker"),
          balloon_lvl=troop_lvl("Balloon"),
          wizard_lvl=troop_lvl("Wizard"),
          healer_lvl=troop_lvl("Healer"),
          dragon_lvl=troop_lvl("Dragon"),
          pekka_lvl=troop_lvl("P.E.K.K.A"),
          minion_lvl=troop_lvl("Minion"),
          hog_rider_lvl=troop_lvl("Hog Rider"),
          valkyrie_lvl=troop_lvl("Valkyrie"),
          golem_lvl=troop_lvl("Golem"),
          witch_lvl=troop_lvl("Witch"),
          lava_hound_lvl=troop_lvl("Lava Hound"),
          bowler_lvl=troop_lvl("Bowler"),
          baby_dragon_lvl=troop_lvl("Baby Dragon"),
          miner_lvl=troop_lvl("Miner"),
          super_barbarian_lvl=troop_lvl("Super Barbarian"),
          super_archer_lvl=troop_lvl("Super Archer"),
          super_wall_breaker_lvl=troop_lvl("Super Wall Breaker"),
          super_giant_lvl=troop_lvl("Super Giant"),
          wall_wrecker_lvl=troop_lvl("Wall Wrecker"),
          battle_blimp_lvl=troop_lvl("Battle Blimp"),
          yeti_lvl=troop_lvl("Yeti"),
          sneaky_goblin_lvl=troop_lvl("Sneaky Goblin"),
          super_miner_lvl=troop_lvl("Super Miner"),
          rocket_balloon_lvl=troop_lvl("Rocket Balloon"),
          ice_golem_lvl=troop_lvl("Ice Golem"),
          electro_dragon_lvl=troop_lvl("Electro Dragon"),
          stone_slammer_lvl=troop_lvl("Stone Slammer"),
          inferno_dragon_lvl=troop_lvl("Inferno Dragon"),
          super_valkyrie_lvl=troop_lvl("Super Valkyrie"),
          dragon_rider_lvl=troop_lvl("Dragon Rider"),
          super_witch_lvl=troop_lvl("Super Witch"),
          siege_barracks_lvl=troop_lvl("Siege Barracks"),
          ice_hound_lvl=troop_lvl("Ice Hound"),
          super_bowler_lvl=troop_lvl("Super Bowler"),
          super_dragon_lvl=troop_lvl("Super Dragon"),
          headhunter_lvl=troop_lvl("Headhunter"),
          super_wizard_lvl=troop_lvl("Super Wizard"),
          super_minion_lvl=troop_lvl("Super Minion"),
          log_launcher_lvl=troop_lvl("Log Launcher"),
          flame_flinger_lvl=troop_lvl("Flame Flinger"),
          battle_drill_lvl=troop_lvl("Battle Drill"),
          electro_titan_lvl=troop_lvl("Electro Titan"),
          apprentice_warden_lvl=troop_lvl("Apprentice Warden"),
          super_hog_rider_lvl=troop_lvl("Super Hog Rider"),
          ruin_witch_lvl=troop_lvl("Ruin Witch"),
          root_rider_lvl=troop_lvl("Root Rider"),
          druid_lvl=troop_lvl("Druid"),
          thrower_lvl=troop_lvl("Thrower"),
          troop_launcher_lvl=troop_lvl("Troop Launcher"),
          super_yeti_lvl=troop_lvl("Super Yeti"),
          furnace_lvl=troop_lvl("Furnace"),
          meteor_golem_lvl=troop_lvl("Meteor Golem"),
          sky_wagon_lvl=troop_lvl("Sky Wagon"),
          lassi_lvl=troop_lvl("L.A.S.S.I"),
          mighty_yak_lvl=troop_lvl("Mighty Yak"),
          electro_owl_lvl=troop_lvl("Electro Owl"),
          unicorn_lvl=troop_lvl("Unicorn"),
          phoenix_lvl=troop_lvl("Phoenix"),
          poison_lizard_lvl=troop_lvl("Poison Lizard"),
          diggy_lvl=troop_lvl("Diggy"),
          frosty_lvl=troop_lvl("Frosty"),
          spirit_fox_lvl=troop_lvl("Spirit Fox"),
          angry_jelly_lvl=troop_lvl("Angry Jelly"),
          sneezy_lvl=troop_lvl("Sneezy"),
          greedy_raven_lvl=troop_lvl("Greedy Raven"),
        )
      ],
      hero_details=[
        Heroes(
          # Heroes
          barbarian_king_lvl=hero_lvl("Barbarian King"),
          archer_queen_lvl=hero_lvl("Archer Queen"),
          grand_warden_lvl=hero_lvl("Grand Warden"),
          battle_machine_lvl=hero_lvl("Battle Machine"),
          royal_champion_lvl=hero_lvl("Royal Champion"),
          battle_copter_lvl=hero_lvl("Battle Copter"),
          minion_prince_lvl=hero_lvl("Minion Prince"),
          dragon_duke_lvl=hero_lvl("Dragon Duke"),

          # Hero equipment
          giant_gauntlet_lvl=equip_lvl("Giant Gauntlet"),
          rocket_spear_lvl=equip_lvl("Rocket Spear"),
          spiky_ball_lvl=equip_lvl("Spiky Ball"),
          frozen_arrow_lvl=equip_lvl("Frozen Arrow"),
          monolith_arrow_lvl=equip_lvl("Monolith Arrow"),
          heroic_torch_lvl=equip_lvl("Heroic Torch"),
          fireball_lvl=equip_lvl("Fireball"),
          snake_bracelet_lvl=equip_lvl("Snake Bracelet"),
          dark_crown_lvl=equip_lvl("Dark Crown"),
          magic_mirror_lvl=equip_lvl("Magic Mirror"),
          electro_boots_lvl=equip_lvl("Electro Boots"),
          lavaloon_puppet_lvl=equip_lvl("Lavaloon Puppet"),
          action_figure_lvl=equip_lvl("Action Figure"),
          meteor_staff_lvl=equip_lvl("Meteor Staff"),
          frost_flake_lvl=equip_lvl("Frost Flake"),
          stick_horse_lvl=equip_lvl("Stick Horse"),
          rocket_backpack_lvl=equip_lvl("Rocket Backpack"),
          revenge_deck_lvl=equip_lvl("Revenge Deck"),
          barbarian_puppet_lvl=equip_lvl("Barbarian Puppet"),
          rage_vial_lvl=equip_lvl("Rage Vial"),
          archer_puppet_lvl=equip_lvl("Archer Puppet"),
          invisibility_vial_lvl=equip_lvl("Invisibility Vial"),
          eternal_tome_lvl=equip_lvl("Eternal Tome"),
          life_gem_lvl=equip_lvl("Life Gem"),
          seeking_shield_lvl=equip_lvl("Seeking Shield"),
          royal_gem_lvl=equip_lvl("Royal Gem"),
          earthquake_boots_lvl=equip_lvl("Earthquake Boots"),
          hog_rider_puppet_lvl=equip_lvl("Hog Rider Puppet"),
          vampstache_lvl=equip_lvl("Vampstache"),
          haste_vial_lvl=equip_lvl("Haste Vial"),
          giant_arrow_lvl=equip_lvl("Giant Arrow"),
          healer_puppet_lvl=equip_lvl("Healer Puppet"),
          rage_gem_lvl=equip_lvl("Rage Gem"),
          healing_tome_lvl=equip_lvl("Healing Tome"),
          henchmen_puppet_lvl=equip_lvl("Henchmen Puppet"),
          dark_orb_lvl=equip_lvl("Dark Orb"),
          metal_pants_lvl=equip_lvl("Metal Pants"),
          noble_iron_lvl=equip_lvl("Noble Iron"),
          fire_heart_lvl=equip_lvl("Fire Heart"),
          stun_blaster_lvl=equip_lvl("Stun Blaster"),
          flame_blower_lvl=equip_lvl("Flame Blower"),
          electro_fangs_lvl=equip_lvl("Electro Fangs"),
        )
      ],
      spell_details=[
        Spells(
          lightning_spell_lvl=spell_lvl("Lightning Spell"),
          healing_spell_lvl=spell_lvl("Healing Spell"),
          rage_spell_lvl=spell_lvl("Rage Spell"),
          jump_spell_lvl=spell_lvl("Jump Spell"),
          freeze_spell_lvl=spell_lvl("Freeze Spell"),
          poison_spell_lvl=spell_lvl("Poison Spell"),
          earthquake_spell_lvl=spell_lvl("Earthquake Spell"),
          haste_spell_lvl=spell_lvl("Haste Spell"),
          clone_spell_lvl=spell_lvl("Clone Spell"),
          skeleton_spell_lvl=spell_lvl("Skeleton Spell"),
          bat_spell_lvl=spell_lvl("Bat Spell"),
          invisibility_spell_lvl=spell_lvl("Invisibility Spell"),
          recall_spell_lvl=spell_lvl("Recall Spell"),
          overgrowth_spell_lvl=spell_lvl("Overgrowth Spell"),
          revive_spell_lvl=spell_lvl("Revive Spell"),
          ice_block_spell_lvl=spell_lvl("Ice Block Spell"),
          totem_spell_lvl=spell_lvl("Totem Spell"),
          angry_spell_lvl=spell_lvl("Angry Spell"),
        )
      ],
      bbtroop_details=[
        BBtroops(
          raged_barbarian_lvl=bb_troop_lvl("Raged Barbarian"),
          sneaky_archer_lvl=bb_troop_lvl("Sneaky Archer"),
          beta_minion_lvl=bb_troop_lvl("Beta Minion"),
          boxer_giant_lvl=bb_troop_lvl("Boxer Giant"),
          bomber_lvl=bb_troop_lvl("Bomber"),
          power_pekka_lvl=bb_troop_lvl("Power P.E.K.K.A"),
          cannon_cart_lvl=bb_troop_lvl("Cannon Cart"),
          drop_ship_lvl=bb_troop_lvl("Drop Ship"),
          baby_dragon_lvl=bb_troop_lvl("Baby Dragon"),
          night_witch_lvl=bb_troop_lvl("Night Witch"),
          hog_glider_lvl=bb_troop_lvl("Hog Glider"),
          electrofire_wizard_lvl=bb_troop_lvl("Electrofire Wizard"),
        )
      ],
  )
  return new_account

def store_in_db(json_part, api_part):
  new_account = create_account_obj(json_part, api_part)
  db.add(new_account)
  db.commit()
      