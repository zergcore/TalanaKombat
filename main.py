from battle_functions import fight_combat

# Ejemplo de uso:
# combat_json = {
#     "player1": {
#       "movimientos": ["D", "DSD", "S", "DSD", "SD"],
#       "golpes": ["K", "P", "", "K", "P"]
#     },
#     "player2": {
#       "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
#       "golpes": ["K", "", "K", "P", "P"]
#     }
# }

combat_json = {
  "player1":{
    "movimientos":["SDD", "DSD","SA", "DSD"],
		"golpes":["K", "P", "K", "P"],
		},
	"player2":{
		"movimientos":["DSD", "WSAW", "ASA", "", "ASA","SA"],
		"golpes":["P", "K", "K", "K", "P", "k"]
		}
}

if __name__ == "__main__":
  result = fight_combat(combat_json["player1"], combat_json["player2"])
  print(result)
