def clamp(value, min, max):
   if value < min:
      return min
   elif value > max:
      return max
   else:
      return value

def max(*args):
  max = None
  for num in args:
    if max == None:
      max = num
    elif num > max:
      max = num
  return max

def min(*args):
  min = None
  for num in args:
    if min == None or num < min:
      min = num
  return min
