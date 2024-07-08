
def fac(num: int):
  a = 1
  for i in range(1, num + 1):

    a *= i
  return a

l1 = []

res = fac(3)

for j in range(res, 0, -1):
  res2= fac(j)
  l1.append(res2)


print(l1)