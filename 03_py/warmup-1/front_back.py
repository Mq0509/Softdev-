#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  #base case: if string is length 1, the string is returned
  if len(str) == 1 :
    return str
  #if string is longer than 1, the string with first and last chars swapped is returned
  else :
    return str[len(str)-1:] + str[1:len(str)-1] + str[0:1]

#Test Cases:
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'def front_back(str):
