from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Table, UniqueConstraint
from backend.database import Base
from sqlalchemy.orm import relationship


user_accounts = Table(
    "user_accounts",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("tag", String, ForeignKey("account__details.tag", ondelete="CASCADE"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    accounts = relationship("Account", secondary=user_accounts, back_populates="users")


class Account(Base):
    __tablename__ = "account__details"
    tag = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    exp_lvl = Column(Integer, nullable=False)
    town_hall_lvl = Column(Integer, nullable=False)
    trophies = Column(Integer, nullable=False)

    users = relationship("User", secondary=user_accounts, back_populates="accounts")

    building_details = relationship("Buildings", back_populates="player", cascade="all,delete-orphan")
    troop_details = relationship("HomeTroops", back_populates="player", cascade="all,delete-orphan")
    spell_details = relationship("Spells", back_populates="player", cascade="all,delete-orphan")
    helper_details = relationship("Helpers", back_populates="player", cascade="all,delete-orphan")
    trap_details = relationship("Traps", back_populates="player", cascade="all,delete-orphan")
    hero_details = relationship("Heroes", back_populates="player", cascade="all,delete-orphan")
    hero_equipment_details = relationship("HeroEquipment", back_populates="player", cascade="all,delete-orphan")
    # NOTE: bbtroop_details / BBtroops removed entirely.


class Buildings(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="building_details")

    building_type = Column(String, nullable=False)
    building_lvl = Column(Integer, nullable=False)
    building_cnt = Column(Integer, nullable=False, default=1)


class Traps(Base):
    __tablename__ = "traps"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="trap_details")

    trap_type = Column(String, nullable=False)
    trap_lvl = Column(Integer, nullable=False)
    trap_cnt = Column(Integer, nullable=False, default=1)


class Helpers(Base):
    __tablename__ = "helpers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="helper_details")

    helper_type = Column(String, nullable=False)
    helper_lvl = Column(Integer, nullable=False)


class HomeTroops(Base):
    __tablename__ = "troops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="troop_details")

    troop_type = Column(String, nullable=False)
    troop_lvl = Column(Integer, nullable=False)


class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="hero_details")

    hero_type = Column(String, nullable=False)
    hero_lvl = Column(Integer, nullable=False)


class HeroEquipment(Base):
    __tablename__ = "hero_equipment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="hero_equipment_details")

    equipment_type = Column(String, nullable=False)
    equipment_lvl = Column(Integer, nullable=False)


class Spells(Base):
    __tablename__ = "spells"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_tag = Column(String, ForeignKey("account__details.tag", ondelete="CASCADE"))
    player = relationship("Account", back_populates="spell_details")

    spell_type = Column(String, nullable=False)
    spell_lvl = Column(Integer, nullable=False)


class Id_to_name(Base):
    __tablename__ = "id_to_name"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class Levels_per_th_home(Base):
    __tablename__ = "levels_per_th_home"
    __table_args__ = (UniqueConstraint("thing", "category", "th_level"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    thing = Column(String, nullable=False)
    category = Column(String, nullable=False)
    th_level = Column(Integer, nullable=False)
    unlocked_level = Column(Integer, nullable=False, default=0)


class Time_per_th_home(Base):
    __tablename__ = "time_per_th_home"
    __table_args__ = (UniqueConstraint("thing", "category", "level"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    thing = Column(String, nullable=False)
    category = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    upgrade_time_seconds = Column(Integer, nullable=True)


class Time_per_level_hero_pet(Base):
    __tablename__ = "time_per_level_hero_pet"
    __table_args__ = (UniqueConstraint("thing", "category", "level"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    thing = Column(String, nullable=False)
    category = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    upgrade_time_seconds = Column(Integer, nullable=True)