def remove_empty_strings(array):
  return [item for item in array if item]

def get_punch_in_string(string, array):
  for item in array:
    if item in string:
      return item
  return string[len(string)-1] if string[len(string)-1] in ["P", "K"] else ""

def validate_combination(string, valid_chars):
  return all(char in valid_chars for char in string)

def validate_move(string):
  move = str("".join([x for x in string if validate_combination(x,"WADS")]))
  return move if len(move) <= 5 else ""

def validate_punch(string):
  punch = str("".join([x for x in string if validate_combination(x,"PK")]))
  return punch if len(punch) <= 1 else ""
