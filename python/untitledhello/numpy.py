num = list(map(int, input("Wirte the numbers:- ").split()))
num.reverse()
ans = []
for i in num:
  ans.append(float(i))
print(ans)
