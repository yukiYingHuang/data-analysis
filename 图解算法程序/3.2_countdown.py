def countdown(i):  #倒计时到0
  print(i)
  # base case
  if i <= 0:  #若想倒计时到1，则基线条件改为 if i<=1即可
    return
  # recursive case
  else:
    countdown(i-1)

countdown(3)

'''
3
2
1
0
'''
