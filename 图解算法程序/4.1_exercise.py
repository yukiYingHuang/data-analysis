def sum(list):  #循环求和
  if list == []:
    return 0
  return list[0] + sum(list[1:])

def recurse_sum(list):  #递归求和
  l = list[0]
  newlist = list[1:]
  if newlist == []:
    return 0
  else:
    return l + sum(newlist)

def recurse_count(list):  #递归计数
  if list == []:
    return 0
  else:
    return 1 + recurse_count(list[1:])

def recurse_max(list):  #递归求最大值
  if list==[]:
    return None
  elif len(list)==1:
    return list[0]
  elif len(list)==2:
    return list[0] if list[0]>list[1] else list[1]
  else:
    sub_max = max(list[1:])
    return list[0] if list[0]>sub_max else sub_max


print(sum([1,2,3,4]))
print(recurse_sum([1,2,3,4]))
print(recurse_count([1,2,3,4]))
print(recurse_max([2,4,1,5]))
print(recurse_max([2]))
print(recurse_max([]))
