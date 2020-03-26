def calc(num):
    count = 1

    for x in range(1, num+1):
        count = count * x
    return count

def calc_recursive(num):
   if num <= 0:
      return 1
   return num * calc_recursive(num - 1)


print(calc(6))
print(calc_recursive(6))