from utils import get_punch_in_string, remove_empty_strings, validate_move, validate_punch

ENERGY_TABLE = {
    1: {
      "DSDP": {
        "energy":3,
        "name": "Taladoken"
      },
      "SDK": {
        "energy":2,
        "name": "Remuyuken"
      },
      "P": {
        "energy":1,
        "name": "Punno"
      },
      "K": {
        "energy":1,
        "name": "Patada"
      },
    },
    2: {
      "SAK": {
        "energy":3,
        "name": "Remuyuken"
      },
      "ASAP": {
        "energy":2,
        "name": "Taladoken"
      },
      "P": {
        "energy":1,
        "name": "Punno"
      },
      "K": {
        "energy":1,
        "name": "Patada"
      },
    }
  }

PLAYER_NAMES = {
    1: "Tonyn",
    2: "Arnaldor",
}

# Calculate priority of the players
def cal_total_buttons(moves, punches):
  buttons = "".join(moves) + "".join(punches)
  return len(buttons)

def cal_total_moves(moves):
  return len("".join(moves))

def cal_total_punches(player, moves, punches):
  possible_punches = ENERGY_TABLE[player].keys()
  punches = list(zip(moves, punches))
  final_punches = [get_punch_in_string(move+punch, possible_punches) for move, punch in punches]
  final_punches = remove_empty_strings(final_punches)
  return len(final_punches)

def cal_priority(player1, player2):
  p1_moves = player1["movimientos"]
  p2_moves = player2["movimientos"]
  p1_punches = player1["golpes"]
  p2_punches = player2["golpes"]

  p1_buttons = cal_total_buttons(p1_moves, p1_punches)
  p2_buttons = cal_total_buttons(p2_moves, p2_punches)
  if p1_buttons > p2_buttons:
    return 2
  elif p2_buttons > p1_buttons:
    return 1
  else:
    p1_quantity_moves = cal_total_moves(p1_moves)
    p2_quantity_moves = cal_total_moves(p2_moves)
    if p1_quantity_moves > p2_quantity_moves:
      return 2
    elif p2_quantity_moves > p1_quantity_moves:
      return 1
    else:
      p1_quantity_punches = cal_total_punches(1, p1_moves, p1_punches)
      p2_quantity_punches = cal_total_punches(2, p2_moves, p2_punches)
      if p1_quantity_punches > p2_quantity_punches:
        return 2
      else:
        return 1


# Execute movements and punches
def execute_move(player: int, move: str, punch: str):
  move_key = get_punch_in_string(str(move)+str(punch), ENERGY_TABLE[player].keys())
  if move_key:
    expended_energy = ENERGY_TABLE.get(player).get(move_key, 0).get("energy", 0)
    return expended_energy
  else:
    return 0


#Fight Narrative
def generate_narration(player, move, punch):

  player_name = PLAYER_NAMES.get(player, "")
  other_player = PLAYER_NAMES.get(2 if player == 1 else 1, "")

  move_key = get_punch_in_string(str(move)+str(punch), ENERGY_TABLE[player].keys())
  if move_key:
    move_name = ENERGY_TABLE.get(player).get(move_key, "").get("name", "")

  if move_name == "Remuyuken":
    narration = f" ➢ {player_name} conecta un {move_name}."
  elif move_name == "Taladoken":
    narration = f" ➢ {player_name} usa un {move_name}."
  elif move_name == "Patada":
    narration = f" ➢ {player_name} avanza y da una {move_name}."
  elif move_name == "Punno":
    narration = f" ➢ {player_name} le da un puñetazo al pobre {other_player}"
  else:
    narration = f" ➢ {player_name} se mueve."

  return narration


# Play
def fight_combat(player1, player2):
  attacker = cal_priority(player1, player2)

  p1_energy=6
  p2_energy=6

  p1_moves = list(map(validate_move, player1["movimientos"]))
  p2_moves = list(map(validate_move, player2["movimientos"]))

  p1_punches =  list(map(validate_punch, player1["golpes"]))
  p2_punches =  list(map(validate_punch, player2["golpes"]))

  index = 0
  narration = []

  while p1_energy > 0 and p2_energy > 0:
    if attacker == 1:
      p2_energy -= execute_move(1, p1_moves[index], p1_punches[index])
      narration.append(generate_narration(1, p1_moves[index], p1_punches[index]))
      if p2_energy <= 0:
        break
      p1_energy -= execute_move(2, p2_moves[index], p2_punches[index])
      narration.append(generate_narration(2, p2_moves[index], p2_punches[index]))
    else:
      p1_energy -= execute_move(2, p2_moves[index], p2_punches[index])
      narration.append(generate_narration(2, p2_moves[index], p2_punches[index]))
      if p1_energy <= 0:
        break
      p2_energy -= execute_move(1, p1_moves[index], p1_punches[index])
      narration.append(generate_narration(1, p1_moves[index], p1_punches[index]))

    index += 1

    if index >= min(len(p1_moves), len(p2_moves)):
      break

  if p1_energy > p2_energy: winner = 1
  elif p2_energy > p1_energy: winner = 2
  else: winner = None

  if winner: narration.append(" ➢ ✅ {} Gana la pelea y aun le queda {} de energía.".format(PLAYER_NAMES[winner], p1_energy if p1_energy > p2_energy else p2_energy))
  else: narration.append(" ➢ La pelea termina en empate.")

  return "\n".join(narration)