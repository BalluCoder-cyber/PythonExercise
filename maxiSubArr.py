list = [4,2,-2,5,-9,8,44,23,-20]
sum = 0
sumj = 0
for i in range(0,len(list)):
  for j in range(i,len(list)):
    sumj += list[j]
if(list[i]+ sumj > sum):
  sum = list[i] + list[j]
  print(sum)    
