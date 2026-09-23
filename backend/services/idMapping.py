from sqlalchemy import select
from backend.database import engine
from backend.models.models import Id_to_name


def map_id_to_name(id):
  stmt = select(Id_to_name).where(Id_to_name.id == id)
  with engine.connect() as conn:
    for row in conn.execute(stmt):
      return row.name.lower().replace(" ", "_")

def map_name_to_id(name):
  stmt = select(Id_to_name).where(Id_to_name.name == name)
  with engine.connect() as conn:
    for row in conn.execute(stmt):
      return row.id

