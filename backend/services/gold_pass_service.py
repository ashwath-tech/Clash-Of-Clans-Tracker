
def reduce_time_buildings(percent : int, details):
  reduce = (1-percent/100)
  details["total_time"] *= reduce
  # print(details["building_time"])
  for thing, content in details["building_time"].items():
    details["building_time"][thing]["total_time"] *= reduce
    for key, val in content.items():
      if key != "total_time":
        details["building_time"][thing][key]["time"] *= reduce
  return details


def reduce_time_lab(percent : int, details):
  reduce = (1-percent/100)
  details["total_time"] *= reduce
  # print(details["building_time"])
  for thing, content in details["lab_time"].items():
    details["lab_time"][thing]["total_time"] *= reduce
    for key, val in content.items():
      if key != "total_time":
        details["lab_time"][thing][key]["time"] *= reduce
  return details