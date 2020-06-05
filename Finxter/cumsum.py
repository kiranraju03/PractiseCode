#Cumultive Sum problem

def cumsum(l:list):
  sums = []
  sums.append(l[0])
  print(sums)
  return helper(sums, l[1:])


def helper(sums:list, xs:list):
  s = sums[len(sums) - 1]
  print(s)
  sums.append(s + xs[0])
  print(sums)
  if len(xs) > 1:
    return  helper(sums, xs[1:])
  return sums

xs = [1, 2, 3]
print(cumsum(xs))