dic=dict()
lnums=[1,2,1,4,1,6,7,8,9,0]


for i in lnums:
	dic[i]=dic.get(i, 0)+1
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())


for i,j in dic.items():
	print(i, j)


