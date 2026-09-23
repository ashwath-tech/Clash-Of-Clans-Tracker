import json

def map_id_to_name(id :int):
  with open("backend/testing/idmapping.json", "r") as f:
    id_mapping = json.load(f)
    if str(id) in id_mapping:
      return id_mapping[str(id)]
    return "Unknown"
# while True:
# #   id = int(input("Enter the id to map: "))
# #   print(map_id_to_name(id))


# with open("backend/coc-api-test2.json", "r") as f:
#     data = dict(json.load(f))
#     for key, value in data.items():
#       if key == "spells":
#         for item in value:
#           print(f"{item['name'].lower().replace(' ', '_')}_lvl = Column(Integer, default= 0, nullable=False)")

# with open("backend/testing/coc-json-example.json", "r") as f:
#     data = dict(json.load(f))
#     for key, value in data.items():
#       if key == "traps":
#         for item in value:
#           print(f"{map_id_to_name(item['data']).lower().replace(' ', '_')}_lvl = Column(Integer, default= 0, nullable=False)")


# value = ['root_rider', 'thrower', 'meteor_golem', 'furnace', 'ruin_witch', 'frosty', 'diggy', 'poizon lizard', 'phoenix', 'spirit fox', 'angry jelly', 'sneezy', 'greedy raven', 'troop_launcher', 'battle_drill', 'sky_wagon', 'power_pekka', 'hog_glider', 'electrofire_wizard']
# for item in value:
#   print(f"{item.lower().replace(' ', '_')}_lvl = Column(Integer, default= 0, nullable=False)")

# value = ['meteor_staff', 'snake_bracelet', 'monolith_arrow', 'heroic_torch', 'lavaloon_puppet', 'frost_flake', haste_vial, fire_heart, flame_blower, ]
# for item in value:
#   print(f"{item.lower().replace(' ', '_')}_lvl = Column(Integer, default= 0, nullable=False)")

with open("backend/testing/idmapping.json", "r") as f:
  id_mapping = dict(json.load(f))
  for key, val in id_mapping.items():
    print(f'{{"id":{key},"name":"{val}"}},')
