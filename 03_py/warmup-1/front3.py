# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
  #base case: if string length is less than 3, three copies of the string is returned
  if len(str) < 3 :
    return str + str + str
  #if string length is longer than 3, a copy of the first 3 chars is returned
  else :
    return str[0:3] + str[0:3] + str[0:3] #[0:3] returns the 0th, 1st, and 2nd index


#Test Cases:
#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'
