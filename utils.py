def validate_string(string):
  array = ["W", "A", "D", "S"]
  for character in string:
    if character not in array:
      return False
  return True

def remove_empty_strings(array):
  return [item for item in array if item]

def get_punch_in_string(string, array):
  for item in array:
    if item in string:
      return item
  if string[len(string)-1] in ["P", "K"]:
    return  string[len(string)-1]
  else:
    return ""

def validate_move(string):
  move = str("".join(list(filter(validate_string, string))))
  if len(move) > 5:
    return ""
  else:
    return move

def validate_punch(string):
  if len(string) > 1:
    return ""
  else: return string


