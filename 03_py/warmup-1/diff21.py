#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  #if n is greater than 21, the difference times 2 is returned
  if n > 21 :
    return (n-21) * 2
  #if n is smaller than 21, the difference is returned
  else :
    return 21 - n
  
"""
Test Cases
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0 
"""

