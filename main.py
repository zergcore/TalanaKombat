import json
from battle_functions import fight_combat

if __name__ == "__main__":
  # Reading combat_json from file combat.json
  with open("combat.json") as f:
    combat_json = json.load(f)

  result = fight_combat(combat_json["player1"], combat_json["player2"])
  print(result)
