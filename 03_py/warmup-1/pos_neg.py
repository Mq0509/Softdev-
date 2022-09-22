
#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  if negative == False :
    return a * b < 0 #if a times b is less than 0, one must be negative
  else:
    return a < 0 and b < 0 #must check if both are negative if negative is true

#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True