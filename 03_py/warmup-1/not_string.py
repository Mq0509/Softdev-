#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[0:3] == "not" :  #returns the string if it already contains not in the front
    return str
  else : # returns the string with not in front
    return "not" + " " + str

#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

