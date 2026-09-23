from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base
from sqlalchemy.orm import relationship


class Account(Base):
    __tablename__ = "account__details"
    tag = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    exp_lvl = Column(Integer, nullable=False)
    town_hall_lvl = Column(Integer, nullable=False)
    trophies = Column(Integer, nullable=False)
    building_details = relationship("Buildings", back_populates="player", cascade="all,delete-orphan")
    troop_details = relationship("HomeTroops", back_populates="player", cascade="all,delete-orphan")
    spell_details = relationship("Spells", back_populates="player", cascade="all,delete-orphan")
    helper_details = relationship("Helpers", back_populates="player", cascade="all,delete-orphan")
    trap_details = relationship("Traps", back_populates="player", cascade="all,delete-orphan")
    bbtroop_details = relationship("BBtroops", back_populates="player", cascade="all,delete-orphan")
    hero_details = relationship("Heroes", back_populates="player", cascade="all,delete-orphan")

class Buildings(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="building_details")

    building_type = Column(String, nullable=False)
    building_lvl = Column(Integer, nullable=False)
    
class Traps(Base):
    __tablename__ = "traps"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="trap_details")

    tool_type = Column(String, nullable=False)
    tool_lvl = Column(Integer, nullable=False)

class Helpers(Base):
    __tablename__ = "helpers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="helper_details")

    builders_Apprentice_lvl = Column(Integer, default= 0, nullable=False)
    lab_Assistant_lvl = Column(Integer, default= 0, nullable=False)
    prospector_lvl = Column(Integer, default= 0, nullable=False)
    alchemist_lvl = Column(Integer, default= 0, nullable=False)

class HomeTroops(Base):
    __tablename__ = "troops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="troop_details")

    barbarian_lvl = Column(Integer, default= 0, nullable=False)
    archer_lvl = Column(Integer, default= 0, nullable=False)
    goblin_lvl = Column(Integer, default= 0, nullable=False)
    giant_lvl = Column(Integer, default= 0, nullable=False)
    wall_breaker_lvl = Column(Integer, default= 0, nullable=False)
    balloon_lvl = Column(Integer, default= 0, nullable=False)
    wizard_lvl = Column(Integer, default= 0, nullable=False)
    healer_lvl = Column(Integer, default= 0, nullable=False)
    dragon_lvl = Column(Integer, default= 0, nullable=False)
    pekka_lvl = Column(Integer, default= 0, nullable=False)
    minion_lvl = Column(Integer, default= 0, nullable=False)
    hog_rider_lvl = Column(Integer, default= 0, nullable=False)
    valkyrie_lvl = Column(Integer, default= 0, nullable=False)
    golem_lvl = Column(Integer, default= 0, nullable=False)
    witch_lvl = Column(Integer, default= 0, nullable=False)
    lava_hound_lvl = Column(Integer, default= 0, nullable=False)
    bowler_lvl = Column(Integer, default= 0, nullable=False)
    baby_dragon_lvl = Column(Integer, default= 0, nullable=False)
    miner_lvl = Column(Integer, default= 0, nullable=False)
    super_barbarian_lvl = Column(Integer, default= 0, nullable=False)
    super_archer_lvl = Column(Integer, default= 0, nullable=False)
    super_wall_breaker_lvl = Column(Integer, default= 0, nullable=False)
    super_giant_lvl = Column(Integer, default= 0, nullable=False)
    wall_wrecker_lvl = Column(Integer, default= 0, nullable=False)
    battle_blimp_lvl = Column(Integer, default= 0, nullable=False)
    yeti_lvl = Column(Integer, default= 0, nullable=False)
    sneaky_goblin_lvl = Column(Integer, default= 0, nullable=False)
    super_miner_lvl = Column(Integer, default= 0, nullable=False)
    rocket_balloon_lvl = Column(Integer, default= 0, nullable=False)
    ice_golem_lvl = Column(Integer, default= 0, nullable=False)
    electro_dragon_lvl = Column(Integer, default= 0, nullable=False)
    stone_slammer_lvl = Column(Integer, default= 0, nullable=False)
    inferno_dragon_lvl = Column(Integer, default= 0, nullable=False)
    super_valkyrie_lvl = Column(Integer, default= 0, nullable=False)
    dragon_rider_lvl = Column(Integer, default= 0, nullable=False)
    super_witch_lvl = Column(Integer, default= 0, nullable=False)
    siege_barracks_lvl = Column(Integer, default= 0, nullable=False)
    ice_hound_lvl = Column(Integer, default= 0, nullable=False)
    super_bowler_lvl = Column(Integer, default= 0, nullable=False)
    super_dragon_lvl = Column(Integer, default= 0, nullable=False)
    headhunter_lvl = Column(Integer, default= 0, nullable=False)
    super_wizard_lvl = Column(Integer, default= 0, nullable=False)
    super_minion_lvl = Column(Integer, default= 0, nullable=False)
    log_launcher_lvl = Column(Integer, default= 0, nullable=False)
    flame_flinger_lvl = Column(Integer, default= 0, nullable=False)
    battle_drill_lvl = Column(Integer, default= 0, nullable=False)
    electro_titan_lvl = Column(Integer, default= 0, nullable=False)
    apprentice_warden_lvl = Column(Integer, default= 0, nullable=False)
    super_hog_rider_lvl = Column(Integer, default= 0, nullable=False)
    ruin_witch_lvl = Column(Integer, default= 0, nullable=False)
    root_rider_lvl = Column(Integer, default= 0, nullable=False)
    druid_lvl = Column(Integer, default= 0, nullable=False)
    thrower_lvl = Column(Integer, default= 0, nullable=False)
    troop_launcher_lvl = Column(Integer, default= 0, nullable=False)
    super_yeti_lvl = Column(Integer, default= 0, nullable=False)
    furnace_lvl = Column(Integer, default= 0, nullable=False)
    meteor_golem_lvl = Column(Integer, default= 0, nullable=False)
    sky_wagon_lvl = Column(Integer, default= 0, nullable=False)
    lassi_lvl = Column(Integer, default= 0, nullable=False)
    mighty_yak_lvl = Column(Integer, default= 0, nullable=False)
    electro_owl_lvl = Column(Integer, default= 0, nullable=False)
    unicorn_lvl = Column(Integer, default= 0, nullable=False)
    phoenix_lvl = Column(Integer, default= 0, nullable=False)
    poison_lizard_lvl = Column(Integer, default= 0, nullable=False)
    diggy_lvl = Column(Integer, default= 0, nullable=False)
    frosty_lvl = Column(Integer, default= 0, nullable=False)
    spirit_fox_lvl = Column(Integer, default= 0, nullable=False)
    angry_jelly_lvl = Column(Integer, default= 0, nullable=False)
    sneezy_lvl = Column(Integer, default= 0, nullable=False)
    greedy_raven_lvl = Column(Integer, default= 0, nullable=False)

class BBtroops(Base):
    __tablename__ = "bbtroops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="bbtroop_details")

    raged_barbarian_lvl = Column(Integer, default= 0, nullable=False)
    sneaky_archer_lvl = Column(Integer, default= 0, nullable=False)
    beta_minion_lvl = Column(Integer, default= 0, nullable=False)
    boxer_giant_lvl = Column(Integer, default= 0, nullable=False)
    bomber_lvl = Column(Integer, default= 0, nullable=False)
    power_pekka_lvl = Column(Integer, default= 0, nullable=False)
    cannon_cart_lvl = Column(Integer, default= 0, nullable=False)
    drop_ship_lvl = Column(Integer, default= 0, nullable=False)
    baby_dragon_lvl = Column(Integer, default= 0, nullable=False)
    night_witch_lvl = Column(Integer, default= 0, nullable=False)
    hog_glider_lvl = Column(Integer, default= 0, nullable=False)
    electrofire_wizard_lvl = Column(Integer, default= 0, nullable=False)

class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="hero_details")

    barbarian_king_lvl = Column(Integer, default= 0, nullable=False)
    archer_queen_lvl = Column(Integer, default= 0, nullable=False)
    grand_warden_lvl = Column(Integer, default= 0, nullable=False)
    battle_machine_lvl = Column(Integer, default= 0, nullable=False)
    royal_champion_lvl = Column(Integer, default= 0, nullable=False)
    battle_copter_lvl = Column(Integer, default= 0, nullable=False)
    minion_prince_lvl = Column(Integer, default= 0, nullable=False)
    dragon_duke_lvl = Column(Integer, default= 0, nullable=False)

    giant_gauntlet_lvl = Column(Integer, default= 0, nullable=False)
    rocket_spear_lvl = Column(Integer, default= 0, nullable=False)
    spiky_ball_lvl = Column(Integer, default= 0, nullable=False)
    frozen_arrow_lvl = Column(Integer, default= 0, nullable=False)
    monolith_arrow_lvl = Column(Integer, default= 0, nullable=False)
    heroic_torch_lvl = Column(Integer, default= 0, nullable=False)
    fireball_lvl = Column(Integer, default= 0, nullable=False)
    snake_bracelet_lvl = Column(Integer, default= 0, nullable=False)
    dark_crown_lvl = Column(Integer, default= 0, nullable=False)
    magic_mirror_lvl = Column(Integer, default= 0, nullable=False)
    electro_boots_lvl = Column(Integer, default= 0, nullable=False)
    lavaloon_puppet_lvl = Column(Integer, default= 0, nullable=False)
    action_figure_lvl = Column(Integer, default= 0, nullable=False)
    meteor_staff_lvl = Column(Integer, default= 0, nullable=False)
    frost_flake_lvl = Column(Integer, default= 0, nullable=False)
    stick_horse_lvl = Column(Integer, default= 0, nullable=False)
    rocket_backpack_lvl = Column(Integer, default= 0, nullable=False)
    revenge_deck_lvl = Column(Integer, default= 0, nullable=False)
    barbarian_puppet_lvl = Column(Integer, default= 0, nullable=False)
    rage_vial_lvl = Column(Integer, default= 0, nullable=False)
    archer_puppet_lvl = Column(Integer, default= 0, nullable=False)
    invisibility_vial_lvl = Column(Integer, default= 0, nullable=False)
    eternal_tome_lvl = Column(Integer, default= 0, nullable=False)
    life_gem_lvl = Column(Integer, default= 0, nullable=False)
    seeking_shield_lvl = Column(Integer, default= 0, nullable=False)
    royal_gem_lvl = Column(Integer, default= 0, nullable=False)
    earthquake_boots_lvl = Column(Integer, default= 0, nullable=False)
    hog_rider_puppet_lvl = Column(Integer, default= 0, nullable=False)
    vampstache_lvl = Column(Integer, default= 0, nullable=False)
    haste_vial_lvl = Column(Integer, default= 0, nullable=False)
    giant_arrow_lvl = Column(Integer, default= 0, nullable=False)
    healer_puppet_lvl = Column(Integer, default= 0, nullable=False)
    rage_gem_lvl = Column(Integer, default= 0, nullable=False)
    healing_tome_lvl = Column(Integer, default= 0, nullable=False)
    henchmen_puppet_lvl = Column(Integer, default= 0, nullable=False)
    dark_orb_lvl = Column(Integer, default= 0, nullable=False)
    metal_pants_lvl = Column(Integer, default= 0, nullable=False)
    noble_iron_lvl = Column(Integer, default= 0, nullable=False)
    fire_heart_lvl = Column(Integer, default= 0, nullable=False)
    stun_blaster_lvl = Column(Integer, default= 0, nullable=False)
    flame_blower_lvl = Column(Integer, default= 0, nullable=False)
    electro_fangs_lvl = Column(Integer, default= 0, nullable=False)

class Spells(Base):
    __tablename__ = "spells"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="spell_details")

    lightning_spell_lvl = Column(Integer, default= 0, nullable=False)
    healing_spell_lvl = Column(Integer, default= 0, nullable=False)
    rage_spell_lvl = Column(Integer, default= 0, nullable=False)
    jump_spell_lvl = Column(Integer, default= 0, nullable=False)
    freeze_spell_lvl = Column(Integer, default= 0, nullable=False)
    poison_spell_lvl = Column(Integer, default= 0, nullable=False)
    earthquake_spell_lvl = Column(Integer, default= 0, nullable=False)
    haste_spell_lvl = Column(Integer, default= 0, nullable=False)
    clone_spell_lvl = Column(Integer, default= 0, nullable=False)
    skeleton_spell_lvl = Column(Integer, default= 0, nullable=False)
    bat_spell_lvl = Column(Integer, default= 0, nullable=False)
    invisibility_spell_lvl = Column(Integer, default= 0, nullable=False)
    recall_spell_lvl = Column(Integer, default= 0, nullable=False)
    overgrowth_spell_lvl = Column(Integer, default= 0, nullable=False)
    revive_spell_lvl = Column(Integer, default= 0, nullable=False)
    ice_block_spell_lvl = Column(Integer, default= 0, nullable=False)
    totem_spell_lvl = Column(Integer, default= 0, nullable=False)
    angry_spell_lvl = Column(Integer, default= 0, nullable=False)

class Id_to_name(Base):
    __tablename__ = "id_to_name"

    id = Column(Integer, primary_key=True, nullable = False)
    name = Column(String, nullable = False)

        



        

        